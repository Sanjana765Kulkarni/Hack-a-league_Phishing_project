import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "catalystccrew@gmail.com"
email_password = "sqsh jpxr ewud tngr"  # Use the app-specific password here
email_receiver = "nowtesting656@gmail.com"

subject = "Phishing"
body = """
It from python.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    try:
        smtp.login(email_sender, email_password)  # Add login step
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email sent successfully...")
    except Exception as e:
        print("Failure")
        print(f"Error: {e}")