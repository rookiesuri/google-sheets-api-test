for i in range(1,10):
    print i

values=[[200],[100]]
print values
print type(values)
print type(values[1])
z={'k':values}
print(type(z))
print z

v=[]# small list
z=[]
for i in range(1,10):
    v=[]
    for j in range(1,10):
        if i==j:
            v.append(j)
        else:
            v.append(0)
    z.append(v)

print z

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from pprint import pprint
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
# for i in range(1,10):
#     for j in range(1,10):
#         if i==j:
#             print i
#         else:
#             print 0
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?''version=v4')



from apiclient import discovery
service = discovery.build('sheets', 'v4', http=http,discoveryServiceUrl=discoveryUrl)
print(service)
print(type(service))



### testing github gui
