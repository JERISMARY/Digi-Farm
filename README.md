Digital Farm Management System

A web-based platform designed to streamline livestock farm operations by integrating biosecurity compliance, health/vaccination tracking, inspection logging, visitor monitoring, and automated email alerts.
Built for pig and poultry farms with role-based access for Admin, Farm Head, Inspector, and Veterinary Officer.

https://jerismary.github.io/Digi-Farm/

🚀 Features

✅ Farm Registration & Management

Add, view, and delete farms

Store farm details, login credentials, and operational data

Files: add a farm.html, viewFarms.html, deletefarms.html


✅ Biosecurity Compliance

10-point biosecurity checklist

Auto email alert if score is below threshold

Files: biosecurity_checklist.html, BioSecurity_reoprt.html, final_reportBS.html


✅ Health & Vaccination Tracking

Log animal health and vaccination details

Auto alerts if farm health score < 3

File: healthAndVaccine.html


✅ Inspection & CAPA

Record inspection details & corrective actions

Auto email notification to admin

File: inspection.html


✅ Visitor Management

Track all farm visitors for biosecurity and traceability

File: visitor.html


✅ Dashboard & Reporting

Central dashboard for all modules

Auto-generated reports for audits and monitoring

Files: dashboard.html, report.html


✅ User Authentication

Role-based login system

File: lolo.html


✅ Automated Email Alerts

Flask backend triggers emails for:

Low biosecurity score

Low health score

New inspection submitted


File: app.py





📁 Project Structure

📦 Digital-Farm-Management
├── add a farm.html
├── viewFarms.html
├── deletefarms.html
├── biosecurity_checklist.html
├── BioSecurity_reoprt.html
├── final_reportBS.html
├── BS.html
├── healthAndVaccine.html
├── inspection.html
├── visitor.html
├── dashboard.html
├── report.html
├── lolo.html
├── index.html
├── app.py
├── logo.jpg
└── ba.jpg




🛠 Tech Stack

Frontend

HTML5

CSS3

JavaScript


Backend

Python (Flask)

SMTP (Gmail) for email alerts


Storage

LocalStorage / JSON (or upgradeable to DB)





🎯 Core Benefits

Centralized farm operations

Improved biosecurity & animal health monitoring

Automated alerts for quick action

Easy reporting & inspections

User-friendly design for small and large farms





🚀 Future Improvements

Integration with MySQL / MongoDB

Dedicated mobile app

Real-time health prediction (AI/ML)

Auto CAPA follow-up reminders

Multi-language support
