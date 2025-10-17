from flask import Flask, request
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # Allow local frontend JS to call this API

SENDER_EMAIL = "digifarm2025@gmail.com"
APP_PASSWORD = "pipj myax apbz mlzc"
ALERT_EMAIL = "jerismary@gmail.com"

@app.route("/send-alert", methods=["POST"])
def send_alert():
    data = request.get_json()
    # Inspection details
    if data.get('inspection'):
        farm = data.get('farm', '')
        inspector = data.get('inspector', '')
        date = data.get('date', '')
        observation = data.get('observation', '')
        capa = data.get('capa', '')
        followUp = data.get('followUp', '')
        message_text = f"""New Inspection Record Submitted:
Farm Type: {farm}
Inspector: {inspector}
Inspection Date: {date}
Observation/Issue: {observation}
CAPA Action: {capa}
Follow-up Date: {followUp}
"""
    else:
        site = data.get('site', 'Unknown Site')
        operator = data.get('operator', 'Unknown')
        score = data.get('score', 0)
        total = data.get('total', 0)
        notes = data.get('notes', '')
        # For healthAndVaccine.html
        animal = data.get('animal', '')
        date = data.get('date', '')
        health = data.get('health', '')
        vaccine = data.get('vaccine', '')
        nextDue = data.get('nextDue', '')
        farmScore = data.get('farmScore', data.get('farm_score', ''))

        if farmScore != '':
            message_text = f"""Farm Score Alert!
Farm Score: {farmScore}/5
Animal: {animal}
Date: {date}
Health: {health}
Vaccination: {vaccine}
Next Due: {nextDue}
Immediate attention required.
"""
        else:
            message_text = f"""Biosecurity checklist alert!
Site: {site}
Operator: {operator}
Score: {score}/{total}
Notes: {notes}
Immediate attention required.
"""

    msg = MIMEText(message_text)
    msg['Subject'] = "Farm/Biosecurity Alert Notification"
    msg['From'] = SENDER_EMAIL
    msg['To'] = ALERT_EMAIL

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, ALERT_EMAIL, msg.as_string())
        server.quit()
        return "🚨 Alert email sent to admin."
    except Exception as e:
        return f"Error sending alert email: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)