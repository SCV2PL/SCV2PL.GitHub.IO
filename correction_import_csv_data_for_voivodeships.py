from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
from datetime import datetime

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
        
a = datetime.today().strftime('%Y%m%d')
b = datetime.today().strftime('%Y-%m-%d')
        

spreadsheet_id1 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'
sheet_id1 = ''+str(a)+''

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


request1 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range=""+str(b)+"!A1:O18").execute()


result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range=""+str(b)+"!A19").execute()
values = result.get('values', [])

RUN2 = [['https://www.arcgis.com/sharing/rest/content/items/153a138859bb4c418156642b5b74925b/data'],

        ['=IMPORTDATA(A19)']]

request2 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range=""+str(b)+"!A19",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN2}).execute()
time.sleep(3)
result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range=""+str(b)+"!A1").execute()
values = result.get('values', [])

RUN3 = [['=SPLIT(A20;";")']]

request3 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range=""+str(b)+"!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN3}).execute()
print(request1, request2, request3)

RUN4 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 1,
        },

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN4).execute()
print(request4)
time.sleep(5)

RUN5 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 15,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 15,
        },
        "pasteType": "Paste_Values",

    }},

]}

request5 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN5).execute()
print(request5)


request6 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range=""+str(b)+"!A19:A20").execute()
print(request6, "(All Operations - Successfully!)")

# python3 /home/luke_blue/Startup_Files/correction_import_csv_data_for_voivodeships.py
