from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint
from datawrapper import Datawrapper

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


range1 = 'support!M382'
range2 = 'support!N382'


request1 = service.spreadsheets().values().get(range=range1,spreadsheetId=spreadsheet_id, valueRenderOption='UNFORMATTED_VALUE').execute().get('values')
a = request1[0][0]

request2 = service.spreadsheets().values().get(range=range2,spreadsheetId=spreadsheet_id, valueRenderOption='UNFORMATTED_VALUE').execute().get('values')
b = request2[0][0]


pprint(a)
pprint(b)


# initialize the datawrapper library with your api token
dw = Datawrapper(access_token = "********************")

# Your chart id
dw_id = 'BdKRT'

# Highlight ranges
highlight_ranges = [
    [str(b), 0.5, str(b), 21.5],
    [26, str(a), 79, str(a)]
]

# Create string from highlight ranges ('str(b),0.5,str(b),21.5\n26,str(a),79,str(a)')
highlight_ranges_string = '\n'.join([','.join([str(x) for x in line]) for line in highlight_ranges])

# Prepare new metadata
metadata = {
    "visualize": {
        "highlight-range": highlight_ranges_string
    }
}

# Send request to datawrapper to update metadata
dw.update_metadata(dw_id, metadata)

# Fetch the metadata again and take a look that your change is there
properties = dw.chart_properties(dw_id)

print(properties)

# python3 /home/luke_blue/Startup_Files/test/datawrapper_api_update_custom_lines.py
