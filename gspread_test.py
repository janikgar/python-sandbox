#!/usr/bin/env python3

import gspread
from pprint import pprint
from pydoc import help
import json

from google_auth_oauthlib import flow

from google.auth import credentials
from oauthlib.oauth2 import BackendApplicationClient
import requests_oauthlib
import requests
# from google.oauth2 import service_account
# from oauth2client.service_account import ServiceAccountCredentials
# import oauth2client
# oauth2client.


AUTH_FILE = 'oauth2.json'
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = '1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI'

def parse_google_auth(file):
  '''
  parse_goole_auth(file)
  :param: file is a String with a path (relative or absolute) to the given JSON file.

  This function requires a JSON file for a specific Google OAuth user.
  This can be received from the Google Cloud Console for the linked project.
  '''
  auth_flow = flow.Flow.from_client_secrets_file(file, scopes=SCOPES)
  auth_flow.redirect_uri = 'http://localhost'
  auth_url, state = auth_flow.authorization_url(access_type='offline', include_granted_scopes='true')
  print(auth_url)

parse_google_auth(AUTH_FILE)
# pprint(help(BackendApplicationClient))

# creds = credentials.Credentials.
# creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
# creds = ServiceAccountCredentials.from_json_keyfile_name('oauth2.json', SCOPES)
# gc = gspread.authorize(creds)

# sheet = gc.open_by_key('1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI')
# pprint(sheet.worksheets)

# print(sheet)
