import os

import pandas as pd
import requests
import streamlit as st

API = os.getenv("API_URL", "http://localhost:8000")
st.set_page_config(page_title="NutriTrack", page_icon="🌱", layout="wide")
st.title("🌱 NutriTrack")
st.caption("Child growth screening and early-risk monitoring")
st.warning("Screening aid only, not a medical diagnosis.")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    st.subheader("Health worker demo login")
    username = st.text_input("Username", "demo")
    password = st.text_input("Password", "nutri-demo", type="password")
    if st.button("Login"):
        try:
            response = requests.post(
                f"{API}/login",
                json={"username": username, "password": password},
                timeout=8,
            )
            if response.ok:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error(response.json().get("detail", "Login failed"))
        except requests.RequestException:
            st.error("Cannot reach API. Start the backend and retry.")
else:
    tab1, tab2, tab3 = st.tabs(["Dashboard", "Add child", "Record visit"])
    with tab1:
        try:
            data = requests.get(f"{API}/dashboard", timeout=8).json()
            a, b = st.columns(2)
            a.metric("Children", data["children_count"])
            b.metric("Visits", data["visits_count"])
            st.subheader("Nutritional status distribution")
            st.bar_chart(pd.Series(data["risk_distribution"], name="Visits"))
            st.subheader("High-risk follow-up list")
            st.dataframe(pd.DataFrame(data["high_risk"]), use_container_width=True)
            st.download_button(
                "Export CSV",
                requests.get(f"{API}/export.csv", timeout=8).content,
                "nutritrack.csv",
            )
        except requests.RequestException:
            st.error("Dashboard unavailable. Check the API.")
    with tab2:
        with st.form("child_form"):
            code = st.text_input("Child code")
            name = st.text_input("Child name")
            age = st.number_input("Age (months)", 0, 60, 24)
            sex = st.selectbox("Sex", ["F", "M"])
            submitted = st.form_submit_button("Save child")
            if submitted:
                try:
                    r = requests.post(
                        f"{API}/children",
                        json={
                            "child_code": code,
                            "name": name,
                            "age_months": age,
                            "sex": sex,
                        },
                        timeout=8,
                    )
                    (
                        st.success(f"Saved child ID {r.json()['id']}")
                        if r.ok
                        else st.error(r.json().get("detail", "Could not save child"))
                    )
                except requests.RequestException:
                    st.error("API connection failed.")
    with tab3:
        try:
            children = requests.get(f"{API}/children", timeout=8).json()
        except requests.RequestException:
            children = []
        if not children:
            st.info("Add a child before recording a visit.")
        else:
            with st.form("visit_form"):
                child = st.selectbox(
                    "Child",
                    children,
                    format_func=lambda x: f'{x["name"]} ({x["child_code"]})',
                )
                age = st.number_input(
                    "Visit age (months)", 0, 60, int(child["age_months"])
                )
                weight = st.number_input("Weight (kg)", 1.0, 40.0, 9.0)
                height = st.number_input("Height (cm)", 40.0, 130.0, 75.0)
                muac = st.number_input("MUAC (cm)", 5.0, 25.0, 13.0)
                diversity = st.slider("Dietary diversity (food groups)", 0, 10, 4)
                illness = st.checkbox("Recent illness")
                submit = st.form_submit_button("Analyse visit")
                if submit:
                    payload = {
                        "child_id": child["id"],
                        "age_months": age,
                        "weight_kg": weight,
                        "height_cm": height,
                        "muac_cm": muac,
                        "dietary_diversity": diversity,
                        "recent_illness": int(illness),
                    }
                    try:
                        result = requests.post(
                            f"{API}/visits", json=payload, timeout=10
                        )
                        if result.ok:
                            data = result.json()
                            st.subheader(data["status"])
                            st.metric(
                                "Early-risk score",
                                f'{data["risk_score"]:.0%}',
                                data["risk_label"],
                            )
                            st.write(
                                "Growth z-scores:",
                                data["waz"],
                                data["haz"],
                                data["whz"],
                            )
                            st.write(
                                "Contributing factors:", ", ".join(data["factors"])
                            )
                            st.write("Recommendations:", data["recommendations"])
                            st.caption(data["disclaimer"])
                        else:
                            st.error(result.json().get("detail", "Visit rejected"))
                    except requests.RequestException:
                        st.error("API connection failed.")
