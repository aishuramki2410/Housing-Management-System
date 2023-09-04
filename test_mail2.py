import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "kaushalyaalacrityapartments@gmail.com"
receiver_email = "g.akash0704@gmail.com"
password = 'brtcxaaiddfafyda'
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email


text = "Welcome to Kaushalya Alacrity Apartments"+'\n'+'\n'+'Thanks for booking!!! Your login credentials are:'


# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")


message.attach(part1)


# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )