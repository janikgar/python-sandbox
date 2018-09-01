#!/usr/bin/env python3

# import requests
# from pydoc import help
from googleapiclient.discovery import build
from oauth2client import file, client, tools
from httplib2 import Http

SPREADSHEET_ID = "1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI"

SCOPES = "https://www.googleapis.com/auth/spreadsheets.readonly"

GID = {"transactions":"1040087283",
       "categories":"886661001",
       "balance_history":"1324484343"}

def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    result = service.spreadsheets()

# sheet = "https://docs.google.com/spreadsheets/d/1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI/export?format=csv&gid="

# transactions = requests.get(sheet+gid['transactions'])

# print(help(transactions.text))