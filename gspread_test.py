import gspread

# from google.auth import credentials
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = service_account.from_service_account_file('credentials.json', SCOPES)
gc = gspread.authorize(creds)

sheet = gc.open()