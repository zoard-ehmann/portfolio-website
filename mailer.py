import os

from smtplib import SMTP

class Mailer():

    def __init__(self):
        self.host = os.getenv('HOST')
        self.port = os.getenv('PORT')
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
    
    def send_mail(self, s_name:str, s_email:str, s_msg:str):
        with SMTP(host=self.host, port=self.port) as smtp:
            smtp.starttls()
            smtp.login(user=self.email, password=self.password)
            smtp.sendmail(
                from_addr=self.email,
                to_addrs=[self.email, s_email],
                msg=f'Subject:From Zoárd\'s Site\n\nName: {s_name}\nEmail: {s_email}\n\nMessage:\n{s_msg}'.encode('utf-8')
            )