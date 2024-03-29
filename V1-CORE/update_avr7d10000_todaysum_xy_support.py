from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'
sheet_id = '50471916'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="TodayCount!D3").execute()
values = result.get('values', [])

RUN1 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c","TodayCount!D3:D382")']]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="TodayCount!D3", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="TodaySum!D3").execute()
values = result.get('values', [])

RUN11 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c","TodayCount!D3:D382")']]

request11 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="TodaySum!D3", valueInputOption="USER_ENTERED", body={"values":RUN11}).execute()

time.sleep(20)


RUN111 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 3,
            'endColumnIndex': 4,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 3,
            'endColumnIndex': 4,
        },
        "pasteType": "Paste_Values",

    }},

]}

request111 = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID, body=RUN111).execute()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="TodaySum!H3").execute()
values = result.get('values', [])

RUN2 = [['=NOW()']]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="TodaySum!H3", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 
RUN3 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': 2,
            'endRowIndex': 3,
            'startColumnIndex': 7,
            'endColumnIndex': 8,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': 2,
            'endRowIndex': 3,
            'startColumnIndex': 7,
            'endColumnIndex': 8,
        },
        "pasteType": "Paste_Values",

    }},

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID, body=RUN3).execute()
print(request3)

        
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="XY!F1").execute()
values = result.get('values', [])

RUN4 = [['={TodaySum!D3:D382}']]

request4 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="XY!F1", valueInputOption="USER_ENTERED", body={"values":RUN4}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="XY!C1").execute()
values = result.get('values', [])

RUN5 = [['={TodaySum!H3:H382}']]

request5 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="XY!C1", valueInputOption="USER_ENTERED", body={"values":RUN5}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="support!P1").execute()
values = result.get('values', [])

RUN6 = [['={TodaySum!H3:H382}']]

request6 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="support!P1", valueInputOption="USER_ENTERED", body={"values":RUN6}).execute()
                                                 
print(request1, request2, request3, request4, request5, request6)

# /app/update_avr7d10000_todaysum_xy_support.py
