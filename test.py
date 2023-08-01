import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587

LOGIN_EMAIL = 'unrelieffundsprogram@outlook.com'
LOGIN_PASSWORD = 'jqsmwfnxsgsyapgj'

message = MIMEMultipart()
message['Subject'] = 'Subject of the email'
message['From'] = LOGIN_EMAIL
message['To'] = 'renuelroberts01@gmail.com'

text = MIMEText('The body of the email')
message.attach(text)

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(LOGIN_EMAIL, LOGIN_PASSWORD)
print ("login succesfully")
server.sendmail(LOGIN_EMAIL, 'recipient-email@domain.com', message.as_string())
server.quit()
