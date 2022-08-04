import os

from smtplib import SMTP

class Mailer():
    """Email sender service via SMTP.
    """

    def __init__(self):
        """Initializes variables for SMTP configuration.
        """
        self.host = os.getenv('HOST')
        self.port = os.getenv('PORT')
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
    
    def send_mail(self, s_subj:str, s_name:str, s_email:str, s_msg:str):
        """Sends an email to the address what has been set up during class initialization via SMTP.

        Args:
            s_subj (str): Subject of the email.
            s_name (str): Name of the sender.
            s_email (str): Email of the sender.
            s_msg (str): Email body.
        """
        with SMTP(host=self.host, port=self.port) as smtp:
            smtp.starttls()
            smtp.login(user=self.email, password=self.password)
            smtp.sendmail(
                from_addr=self.email,
                to_addrs=[self.email, s_email],
                msg=f'Subject:{s_subj}\n\nName: {s_name}\nEmail: {s_email}\n\nMessage:\n{s_msg}'.encode('utf-8')
            )