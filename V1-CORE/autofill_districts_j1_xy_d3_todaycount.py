from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
sheet_id1 = '0'
sheet_id2 = '14006599'

service = build('sheets', 'v4', credentials=creds)

RUN1 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 380,
            'startColumnIndex': 9,
            'endColumnIndex': 10,
        },

    }},

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=RUN1).execute()

RUN2 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id2,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 3,
            'endColumnIndex': 4,
        },

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=RUN2).execute()

print(request1, request2)

# python3 /app/autofill_districts_j1_xy_d3_todaycount.py
