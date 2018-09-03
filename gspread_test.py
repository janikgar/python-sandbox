#!/usr/bin/env python3

import gspread
from pprint import pprint
from pydoc import help
import json

from google.auth import credentials
from oauthlib.oauth2 import BackendApplicationClient
import requests_oauthlib
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
  jsonfile = json.load(open(AUTH_FILE))
  json_installed = jsonfile['installed']
  # pprint(json_installed)
  client_id = json_installed['client_id']
  client_secret = json_installed['client_secret']
  redirect_uri = 'http://localhost'
  authorization_base_url = json_installed['auth_uri']
  token_url = json_installed['token_uri']
  sess = requests_oauthlib.OAuth2Session(client_id=client_id, scope = SCOPES, redirect_uri=redirect_uri)
  pprint(sess.access_token)

parse_google_auth(AUTH_FILE)
# pprint(help(BackendApplicationClient))

# creds = credentials.Credentials.
# creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
# creds = ServiceAccountCredentials.from_json_keyfile_name('oauth2.json', SCOPES)
# gc = gspread.authorize(creds)

# sheet = gc.open_by_key('1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI')
# pprint(sheet.worksheets)

# print(sheet)
