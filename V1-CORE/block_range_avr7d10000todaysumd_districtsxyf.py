from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id1 = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'
sheet_id1 = '50471916'

spreadsheet_id2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
sheet_id2 = '0'

service = build('sheets', 'v4', credentials=creds)

RUN1 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 3,
            'endColumnIndex': 4,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 3,
            'endColumnIndex': 4,
        },
        "pasteType": "Paste_Values",

    }},

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN1).execute()

RUN2 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 380,
            'startColumnIndex': 5,
            'endColumnIndex': 6,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 380,
            'startColumnIndex': 5,
            'endColumnIndex': 6,
        },
        "pasteType": "Paste_Values",

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN2).execute()

print(request1, request2)

# python3 /app/block_range_avr7d10000todaysumd_districtsxyf.py
