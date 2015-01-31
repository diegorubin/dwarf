import httplib2
import sys, time
import getpass

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

from dwarf.daemon.base import Daemon
from dwarf.message import Message
from dwarf.spreadsheet import SpreadSheet


# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = '/home/diegorubin/google_api/client_secret.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

# Location of the credentials storage file
STORAGE = Storage('/home/diegorubin/google_api/gmail.storage')

TITLE = 'Ruby Team - Artefatos'

class DwarfDaemon(Daemon):
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):

        self.__email = raw_input("email: ")
        self.__password = getpass.getpass("password: ")

        # Start the OAuth flow to retrieve credentials
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
        self.__http = httplib2.Http()

        # Try to retrieve credentials from storage or run the flow to generate them
        self.__credentials = STORAGE.get()
        if self.__credentials is None or self.__credentials.invalid:
            self.__credentials = run(flow, STORAGE, http=self.__http)

        super(DwarfDaemon, self).__init__(pidfile, stdin, stdout, stderr)

    def run(self):

        while True:
            try:
                self.fetch_emails()
            except:
                print 'falhou'
            time.sleep(30)

    def fetch_emails(self):
        print 'get messages...'

        # Authorize the httplib2.Http object with our credentials
        self.__http = self.__credentials.authorize(self.__http)

        # Build the Gmail service from discovery
        gmail_service = build('gmail', 'v1', http=self.__http)

        # Retrieve a page of threads
        threads = gmail_service.users().messages().list(userId='me', q='Ruby Team').execute()

        # Get spreadsheet
        spread = SpreadSheet(TITLE, self.__email, self.__password)

        # Print ID for each thread
        if threads['messages']:
            for thread in threads['messages']:
                entry = gmail_service.users().messages().get(userId='me', id=thread['id']).execute()
                message = Message(entry['snippet'])

                for link in message.links():
                    spread.insert_link(link, '')

