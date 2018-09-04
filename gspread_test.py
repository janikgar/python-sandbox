#!/usr/bin/env python3

import gspread
from pprint import pprint
from pydoc import help
import pickle

from google_auth_oauthlib import flow
from apiclient.discovery import build
# from google.oauth2 import credentials.credentials.credentials.Credentials.


AUTH_FILE = 'oauth2.json'
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SPREADSHEET_ID = '1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI'
URL = 'https://sheets.googleapis.com/v4/spreadsheets/' + SPREADSHEET_ID

def parse_google_auth(file):
  '''
  parse_goole_auth(file)
  :param: file is a String with a path (relative or absolute) to the given JSON file.

  This function requires a JSON file for a specific Google OAuth user.
  This can be received from the Google Cloud Console for the linked project.
  '''
  saved_token = open('token.bin', 'wb+')
  print(saved_token.read())
  if len(saved_token.read()) == 0:
    auth_flow = flow.InstalledAppFlow.from_client_secrets_file(file, scopes=SCOPES)
    creds = auth_flow.run_local_server(open_browser=True)
    pickle.dump(creds, saved_token)
    saved_token.close()
  else:
    # pass
    creds = pickle.load(saved_token)
    # saved_token.
    saved_token.close()

  print(creds)
  service = build('sheets', 'v4', credentials=creds)

parse_google_auth(AUTH_FILE)
