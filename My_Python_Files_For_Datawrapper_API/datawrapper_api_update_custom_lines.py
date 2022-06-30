from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint
from datawrapper import Datawrapper

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
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


dw = Datawrapper(access_token = "********************")

dw_id = 'gRs82'

highlight_ranges = [
    [str(b), 0, str(b), 9.5],
    [35, str(a), 75, str(a)]
]

highlight_ranges_string = '\n'.join([','.join([str(x) for x in line]) for line in highlight_ranges])

metadata = {
    "visualize": {
        "highlight-range": highlight_ranges_string
    }
}

dw.update_metadata(dw_id, metadata)

dw_id = 'qGF2F'

highlight_ranges = [
    [str(b), 0, str(b), 9.5],
    [35, str(a), 75, str(a)]
]

highlight_ranges_string = '\n'.join([','.join([str(x) for x in line]) for line in highlight_ranges])

metadata = {
    "visualize": {
        "highlight-range": highlight_ranges_string
    }
}

dw.update_metadata(dw_id, metadata)


dw_id = 'BF3jL'

highlight_ranges = [
    [str(b), 0, str(b), 4.5]
]

highlight_ranges_string = '\n'.join([','.join([str(x) for x in line]) for line in highlight_ranges])

metadata = {
    "visualize": {
        "highlight-range": highlight_ranges_string
    }
}

dw.update_metadata(dw_id, metadata)

dw_id = 'HyYXt'

highlight_ranges = [
    [str(b), 0, str(b), 4.5]
]

highlight_ranges_string = '\n'.join([','.join([str(x) for x in line]) for line in highlight_ranges])

metadata = {
    "visualize": {
        "highlight-range": highlight_ranges_string
    }
}

dw.update_metadata(dw_id, metadata)

# python3 /app/datawrapper_api_update_custom_lines.py
