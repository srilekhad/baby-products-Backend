import os
from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')
SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')


# Database name
DATABASE_NAME = 'Baby_Products_App'
