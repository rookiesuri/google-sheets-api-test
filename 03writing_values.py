
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from pprint import pprint

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?''version=v4')
service = discovery.build('sheets', 'v4', http=http,discoveryServiceUrl=discoveryUrl)
spreadsheet_id = '1DjkMsalBBnr4_t9wYzEp2EYdXmGl4CQXZMstbP7aRxs'
ranges = 'Sheet1!A1:z'

#########mycode to create values list,throws erros if range small then values
values=[]
for i in range(1,10):
    v=[]
    for j in range(1,10):
        if i==j:
            v.append(j)
        else:
            v.append(0)
    values.append(v)
########################################
#values =[[500,12004],[1000]]
print(type(values))

Body = {
    'values' : values,
    }
request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=ranges,valueInputOption='RAW',body=Body)
# print(request)
response=request.execute()
#values = response.get('values', []) #extracts values from dict response
pprint(response)

# print(type(response))
# pprint(values)
# print(values)
# print(response)
