import httplib2
import sys, time

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

from dwarf.daemon.base import Daemon


# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = '/home/diegorubin/Downloads/client_secret.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

class DwarfDaemon(Daemon):
    def run(self):
        while True:
            print 'get messages...'
            #self.fetch_emails()

            time.sleep(30)

    def fetch_emails(self):
        # Start the OAuth flow to retrieve credentials
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
        http = httplib2.Http()

        # Try to retrieve credentials from storage or run the flow to generate them
        credentials = STORAGE.get()
        if credentials is None or credentials.invalid:
          credentials = run(flow, STORAGE, http=http)

        # Authorize the httplib2.Http object with our credentials
        http = credentials.authorize(http)

        # Build the Gmail service from discovery
        gmail_service = build('gmail', 'v1', http=http)

        # Retrieve a page of threads
        threads = gmail_service.users().messages().list(userId='me', q='Ruby Team').execute()

        # Print ID for each thread
        if threads['messages']:
          for thread in threads['messages']:
            message = gmail_service.users().messages().get(userId='me', id=thread['id']).execute()

            print message['payload']['headers'][0]['value'] + ': ' + message['snippet']

