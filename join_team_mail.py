# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from decouple import config

# sender = config('EMAIL_SENDER')
# password = config('EMAIL_PASSWORD')

# def send_email(recipient: str, teamToken: str, documentTeamName: str, firstName: str):
#     if recipient.__contains__("string"):
#         print("This was a test user.")
#         return

#     message = MIMEMultipart()
#     message['From'] = sender
#     message['To'] = recipient
#     message['Subject'] = f"""{firstName} has shared a document with you in "{documentTeamName}"""""

#     body_content = f"""Hello,

# {firstName} has shared a document with you in "{documentTeamName}".

# Click the link below to securely access this document:

# http://localhost:8000/register?team_token={teamToken}

# Best Regards,
# RivetingAI
# This is a system-generated message. Do not reply.
# Copyright © 2024 Riveting Technology, Inc.
# """

#     message.attach(MIMEText(body_content, "plain"))

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#         smtp_server.login(sender, password)
#         smtp_server.sendmail(sender, recipient, message.as_string())
#     print("Message sent!")
import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from decouple import config

sender = config("EMAIL_SENDER")
password = config("EMAIL_PASSWORD")


def send_email(recipient: str, teamToken: str, documentTeamName: str, firstName: str):

    # Read the image file
    # with open("./static/logo.svg", "rb") as svg_file:
    #     encoded_svg = base64.b64encode(svg_file.read()).decode("utf-8")
    if recipient.__contains__("string"):
        print("This was a test user.")
        return

    # HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet" />
       <style>
      .emailsection {{
        width: 640px;
        padding: 32px;
        background-color: #fff;
      }}
      .emailsection .head {{
        display: flex;
        padding: 40px 32px 0px 32px;
        gap: 18px;
        align-items: flex-start;
      }}
      .emailsection .head h2 {{
        margin: 0;
        color: #000;
        /* Paragraph / 500 */
        font-family: Inter;
        font-size: 24px;
        font-style: normal;
        font-weight: 400;
        line-height: 32px; /* 133.333% */
      }}
      .emailsection .emailcontent {{
        padding: 0px 32px;
      }}
      .emailsection .emailcontent p {{
        font-family: Inter;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        line-height: 24px;
        margin: 17px 0;
      }}
      .emailsection .subcontent {{
        padding: 0 32px;
      }}
      .emailsection .firstlink {{
        padding: 8px 16px;
        max-width: 300px;
        margin: 0 0 23px 0;
        border-radius: 20px;
        border: 1px solid var(--Stroke-Default, rgba(0, 0, 0, 0.24));
        background: var(--Background-Primary, #2230F6);
      }}
      .emailsection .firstlink a.linkbtn {{
        color: var(--Text-White, #fff);
        font-family: Inter;
        font-size: 18px;
        font-style: normal;
        font-weight: 500;
        line-height: 24px; /* 133.333% */
        text-decoration: none;
      }}
      .secondlink a.link span {{
        color: #4D4AEA;
        font-family: Inter;
        font-size: 16px;
        font-style: normal;
        font-weight: 700;
        line-height: 24px;
        text-decoration-line: underline;
        display: block;
        margin: 0 0 23px 0;
      }}
      .secondlink a.link {{
        color: var(--Text-Light, #333);
        font-family: Inter;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        line-height: 24px; /* 150% */
        text-decoration-line: underline;
      }}
      .Regards p {{
        color: var(--Text-Light, #333);
        /* Paragraph / 300 */
        font-family: Inter;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        margin: 0;
        line-height: 24px; /* 150% */
        margin: 0 0 23px 0;
      }}
      .Regards p span {{
        color: var(--Text-Light, #333);
        /* Headline / 400 */
        font-family: Inter;
        font-size: 20px;
        font-style: normal;
        font-weight: 500;
        line-height: 24px;
        display: block;
      }}
      h3.reply {{
        color: var(--Text-Lightest, #999);
        /* Paragraph / 200 */
        font-family: Inter;
        font-size: 14px;
        font-style: normal;
        font-weight: 400;
        line-height: 20px; /* 142.857% */
        margin: 0;
      }}
      .copyright p {{
        font-family: Inter;
        font-size: 12px;
        font-style: normal;
        font-weight: 400;
        line-height: 16px; /* 133.333% */
        color: #999999;
      }}
      .copyright p span {{
        display: block;
      }}
    </style>
    </head>
    <body>
        <div class="emailsection">
            <div class="head">
                <img src="./static/logo.svg" alt="Static Image" />
                <h2>
                    <span>{firstName}</span> has shared a secure <br />
                    document with you in “{documentTeamName}”
                </h2>
            </div>
            <div class="emailcontent">
                <p>Hello,</p>
                <p>
                    <span>{firstName}</span> has shared a document with you in “{documentTeamName}.”
                </p>
                <p>Click the link below to securely access this document:</p>
            </div>
            <div class="subcontent">
                <div class="firstlink">
                    <a href="http://localhost:8000/register?team_token={teamToken}" class="linkbtn">Click to Access {firstName}'s Document</a>
                </div>
                <div class="secondlink">
                    <a href="#" class="link">Click this URL if the above button does not work:
                    <span>httpss://rivetingai.com/efefefewfeff</span></a>
                </div>
                <div class="Regards">
                    <p>Best Regards, <span>RivetingAI</span></p>
                </div>
                <h3 class="reply">This is a system generated message. Do not reply.</h3>
                <div class="copyright">
                    <p>
                        Copyright © 2024 Riveting Technology, Inc.
                        <span>Track time better with RivetingAI.com</span>
                    </p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # Create message container
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = (
        f"{firstName} has shared a document with you in '{documentTeamName}'"
    )
    message["Date"] = formatdate()

    # Attach HTML content
    html_part = MIMEText(html_content, "html")
    message.attach(html_part)

    # Connect to SMTP server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, message.as_string())

    print("Message sent!")


# Example usage
