from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ.get('CASES_DB_USER')
DB_PASSWORD = os.environ.get('CASES_DB_PASSWORD')
DB_SERVER = os.environ.get('CASES_DB_SERVER')
DB_NAME = os.environ.get('CASES_DB_NAME')
DB_PORT = os.environ.get('CASES_DB_PORT', default=5432)

DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'
