import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Notification:
    def __init__(self, host = '', api = '', sender = '', receiver = ''):
        self.mail_host = host
        self.mail_pass = api
        self.sender = sender
        self.receiver = receiver
    

    def send(self, subject, content):
        message = MIMEText(content, 'plain', 'utf-8')

        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = subject
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465) 
            smtpObj.login(self.sender, self.mail_pass) 
            smtpObj.sendmail(self.sender, self.receiver, message.as_string())
            smtpObj.quit()
            print('send notification success')
        except smtplib.SMTPException as e:
            print('send notification fail')
            print(e)