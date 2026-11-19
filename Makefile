install:
	pip install -r requirements-dev.txt
train:
	python -m ml.data_gen
	python -m ml.train
test:
	pytest
run:
	uvicorn app.main:app --reload
frontend:
	streamlit run frontend/streamlit_app.py
