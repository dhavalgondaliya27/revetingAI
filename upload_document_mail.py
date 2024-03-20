import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config

subject = "New Document Uploaded"
body = "Please click the following link to show a document: http://localhost:8000/document/"
sender = config('EMAIL_SENDER')
password = config('EMAIL_PASSWORD')

def send_email(recipient: str, team_id: int, documentTeamName: str, firstName: str):
    if recipient.__contains__("string"):
        print("This was a test user.")
        return
    
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = f"""{firstName} has invited you to {documentTeamName}"""

    body_content = f"""Hello,

You've been invited to join {firstName}'s document team titled "{documentTeamName}".

Click the link below to securely join this document team where you can access, review, and edit your team's documents:

{body}{team_id}

Best Regards,
RivetingAI
This is a system-generated message. Do not reply.
Copyright © 2024 Riveting Technology, Inc.
"""

    message.attach(MIMEText(body_content, "plain"))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, message.as_string())
    print("Message sent!")
