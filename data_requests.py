#!/usr/bin/env python3

from pydoc import help
from google.oauth2 import credentials
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import json
from google.auth.transport.requests import AuthorizedSession
from pprint import pprint

SPREADSHEET_ID = "1wbnG31Z5QBm2fuyzZOY9XkSij0EERtX92wEHq9LbPiI"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
URL = "https://sheets.googleapis.com/v4/spreadsheets/" + SPREADSHEET_ID
AUTH_FILE = json.load(open('oauth2.json'))['installed']


def main():
    # pprint(AUTH_FILE)
    client = BackendApplicationClient(client_id=AUTH_FILE['client_id'])
    oauth = OAuth2Session(client=client)
    authorization_url = oauth.authorization_url(url=AUTH_FILE['auth_uri'])
    print(authorization_url)
    # print(help(oauth.fetch_token))
    # token = oauth.fetch_token(
    #     token_url=AUTH_FILE['token_uri'],
    #     client_id=AUTH_FILE['client_id'],
    #     client_secret=AUTH_FILE['client_secret']
    # )
    # creds = credentials.Credentials(token)
    # sess = AuthorizedSession(creds)
    # response = sess.get(URL)
    # print(response.text)

if __name__ == '__main__':
    main()
