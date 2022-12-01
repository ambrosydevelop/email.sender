import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(message,subject,from_email,password,to_email,file) -> None:
    """Send email message,5 arg"""
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(from_email,password)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject 
    part1 = MIMEText(message, 'plain')
    with open('web/your_html.html','r') as f:
        part2 = MIMEText(f.read(), 'html')
    msg.attach(part1)
    if file:
        msg.attach(part2)
    smtpObj.sendmail(from_email,to_email,msg.as_string()) 
