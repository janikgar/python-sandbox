#!/usr/bin/env python3

from pprint import pprint
from pydoc import help
import pickle
import json

from google_auth_oauthlib import flow
from apiclient.discovery import build

AUTH_FILE = 'oauth2.json'
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SPREADSHEET_ID = '1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI'
URL = 'https://sheets.googleapis.com/v4/spreadsheets/' + SPREADSHEET_ID
SHEET_NAMES = ["Transactions", "Categories", "Balance History"]

def parse_google_auth(file):
  """
  parse_goole_auth(file)
  :param: file is a String with a path (relative or absolute) to the given JSON file.

  This function requires a JSON file for a specific Google OAuth user.
  This can be received from the Google Cloud Console for the linked project.
  """

  try:
    saved_token = open('token.bin', 'rb')
    creds = pickle.load(saved_token)
  except:
    saved_token = open('token.bin', 'wb+')
    auth_flow = flow.InstalledAppFlow.from_client_secrets_file(file, scopes=SCOPES)
    creds = auth_flow.run_local_server(open_browser=True)
    pickle.dump(creds, saved_token)
  finally:
    saved_token.close()

  service = build('sheets', 'v4', credentials=creds)
  return service

def open_file(service, file_id, range_string):
  request = service.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=range_string)
  response = request.execute()
  savefile = open('{}.json'.format(range_string.lower()), 'w+')
  json.dump(response, savefile, indent=4, separators=[',', ': '])

SERVICE = parse_google_auth(AUTH_FILE)

for range_string in SHEET_NAMES:
  open_file(SERVICE, SPREADSHEET_ID, range_string)
