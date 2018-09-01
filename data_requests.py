#!/usr/bin/env python3

# import requests
from pydoc import help
import google.auth
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

SPREADSHEET_ID = "1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
URL = "https://sheets.googleapis.com/v4/spreadsheets/" + SPREADSHEET_ID
# GID = {"transactions":"1040087283",
#        "categories":"886661001",
#        "balance_history":"1324484343"}

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # credentials, project = google.auth.default()
    credentials = service_account.Credentials.from_service_account_file('credentials.json').with_scopes(SCOPES)
    authed_session = AuthorizedSession(credentials)
    # print(scope)
    response = authed_session.get(URL)
    print(response.text)

if __name__ == '__main__':
    main()
