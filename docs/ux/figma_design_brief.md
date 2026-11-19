# Figma design brief (under one hour)

## Frames
Create four desktop frames at 1440×900 and four mobile frames at 390×844: Login, Dashboard, Add Child/Visit, Result + Explanation. Keep a 24 px page margin and 16 px spacing scale.

## Visual styles
- Primary: deep teal `#176B67`; surface `#FFFFFF`; page background `#F4F7F6`; text `#20312F`.
- Risk labels: green `#237A45` + “Low”; amber `#A96500` + “Moderate”; red `#B42318` + “High”. Always show text, not color alone.
- Typography: Inter; headings 24/32 semibold, body 16/24 regular, helper text 13/18.
- Cards: 12 px radius, subtle border, 16 px internal padding.

## Components
Text field with label/unit/helper/error; primary and secondary buttons; navigation tabs; metric card; risk badge with text; status card; data table; chart placeholder; disclaimer banner; empty state; toast/error message.

## Prototype flow
Login → Dashboard → Add Child → Visit Form → Result + Explanation → Dashboard. Add interactions for invalid login, required-field errors, successful save, result review and CSV export confirmation.

## Accessibility and usability
Use contrast-aware text, visible focus states, minimum 44 px touch targets, labels for every field, units beside measurement fields and no color-only meaning. On mobile stack forms and metric cards vertically. Keep the disclaimer visible on login and results.

## Build sequence
1. Create color and typography styles (5 min).
2. Create reusable field, button, badge and card components (10 min).
3. Design desktop login/dashboard/forms/results (20 min).
4. Adapt frames to mobile (10 min).
5. Wire prototype interactions (10 min).
