from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id1 = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'
sheet_id1 = '335219542'

spreadsheet_id2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
sheet_id2 = '0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

RUN1 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 1,
            "title": '2021-12-03 - SUM',
        },

    }},

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN1).execute()
print(request1)


RUN2 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 1,
            "title": '2021-12-03 - SUM',
        },

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN2).execute()
print(request2)


RUN3 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 4,
            'endColumnIndex': 16,
        },
        "destination": {
            'sheetId': 1,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 4,
            'endColumnIndex': 16,
        },
        "pasteType": "Paste_Values",

    }},

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN3).execute()

RUN4 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 380,
            'startColumnIndex': 2,
            'endColumnIndex': 11,
        },
        "destination": {
            'sheetId': 1,
            'startRowIndex': 0,
            'endRowIndex': 380,
            'startColumnIndex': 2,
            'endColumnIndex': 11,
        },
        "pasteType": "Paste_Values",

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN4).execute()

print(request3, request4)

# python3 /home/luke_blue/Startup_Files/save_daily_sum.py
