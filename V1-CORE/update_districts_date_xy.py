from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
sheet_id = '0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="XY!C1").execute()
values = result.get('values', [])

RUN1 = [['=NOW()']]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="XY!C1", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()
                                                 
RUN2 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': 0,
            'endRowIndex': 1,
            'startColumnIndex': 2,
            'endColumnIndex': 3,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': 0,
            'endRowIndex': 1,
            'startColumnIndex': 2,
            'endColumnIndex': 3,
        },
        "pasteType": "Paste_Values",

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID, body=RUN2).execute()
print(request2)

                                                 
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="XY!K1").execute()
values = result.get('values', [])

RUN3 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","support!G1:G380")']]

request3 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="XY!K1", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="XY!F1").execute()
values = result.get('values', [])

RUN4 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c","XY!J1:J380")']]

request4 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="XY!F1", valueInputOption="USER_ENTERED", body={"values":RUN4}).execute()
                                                 
print(request1, request2, request3, request4)

# python3 /home/luke_blue/Startup_Files/update_districts_date_xy.py
