from email.message import EmailMessage
import ssl
import smtplib

class email_sender(object):
    def __init__(self):
        self.my_address = 'starveyourbin@gmail.com'
        self.my_password = 'kfxhhmeplvvmewip'
        
        
    def send_email(self, destination_address, subject, body):
        em = EmailMessage()
        em['From'] = self.my_address
        em['To'] = destination_address
        em['Subject'] = subject
        em.set_content(body)
        
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.my_address, self.my_password)
            smtp.sendmail(self.my_address, destination_address, em.as_string())
            
            
    def expiry_reminer(self, destination_address, days_left, item_name):
        subject = f"You have an item expiring in {days_left} days"
        body = f"""Your {item_name} is set to expire in {days_left} day(s).
Please login to view your items and search for recipes."""
        
        self.send_email(destination_address, subject, body)
        
    def expired_warning(self, destination_address, item_name):
        subject = f"WARNING!!!- Your {item_name} has expired"
        body = f"""Your {item_name} has expired.
Please do not use your {item_name}, it could be harmful for you (or just not taste very nice).
In future use our recipe finder to use up your food before it expires."""

        self.send_email(destination_address, subject, body)
        
        
    def account_creation(self, destination_address):
        subject = "Welcome"
        body = """Welcome to Starve Your Bin!
        
You have just registered this email address with your acount.
With us, you will save food, money and most importantly, the environment :)"""

        self.send_email(destination_address, subject, body)
        
        
    def account_deletion(self, destination_address):
        subject = "Sorry to see you go :("
        body = """Oh no, you seem to have deleted your account.
        
We hope you had a good time with us and we are sorry to see you go :(
Good luck in all your future food waste reduction endeavors."""

        self.send_email(destination_address, subject, body)
    

