import smtplib, ssl
from email.message import EmailMessage
import json

with open("config.json") as f:
    cfg = json.load(f)

def enviar_email(path):
    msg = EmailMessage()
    msg["Subject"] = "Reporte diario COVID"
    msg["From"] = cfg["email"]["sender"]
    msg["To"] = cfg["email"]["receiver"]
    msg.set_content("Adjunto el reporte diario de COVID-19.")

    with open(path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=path.split("/")[-1])

    ctx = ssl.create_default_context()
    s = cfg["email"]
    with smtplib.SMTP_SSL(s["smtp_server"], s["port"], context=ctx) as server:
        server.login(s["sender"], s["password"])
        server.send_message(msg)

