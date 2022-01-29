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
sheet_id1 = a

spreadsheet_id2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
sheet_id2 = a

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range=""+str(b)+"!A19").execute()
values = result.get('values', [])

RUN1 = [['https://www.arcgis.com/sharing/rest/content/items/153a138859bb4c418156642b5b74925b/data'],

        ['=IMPORTDATA(A19)']]

request1 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range=""+str(b)+"!A19",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN1}).execute()
time.sleep(3)
result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range=""+str(b)+"!A1").execute()
values = result.get('values', [])

RUN2 = [['=SPLIT(A20;";")']]

request2 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range=""+str(b)+"!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN2}).execute()
print(request1, request2)

RUN3 = {'requests': [
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

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN3).execute()
print(request3)
time.sleep(5)

RUN4 = {'requests': [
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

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN4).execute()
print(request4)


result = sheet.values().get(spreadsheetId=spreadsheet_id2,
                            range=""+str(b)+"!A383").execute()
values = result.get('values', [])

RUN5 = [['https://www.arcgis.com/sharing/rest/content/items/6ff45d6b5b224632a672e764e04e8394/data'],

        ['=IMPORTDATA(A383)']]

request5 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id2,
                                                  range=""+str(b)+"!A383",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN5}).execute()

time.sleep(3)
result = sheet.values().get(spreadsheetId=spreadsheet_id2,
                            range=""+str(b)+"!A1").execute()
values = result.get('values', [])

RUN6 = [['=SPLIT(A384;";")']]

request6 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id2,
                                                  range=""+str(b)+"!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN6}).execute()
print(request5, request6)

RUN7 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 1,
        },

    }},

]}

request7 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN7).execute()
print(request7)
time.sleep(10)

RUN8 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "pasteType": "Paste_Values",

    }},

]}

request8 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN8).execute()
print(request8)      


request9 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range=""+str(b)+"!A19:A20").execute()

request10 = sheet.values().clear(spreadsheetId=spreadsheet_id2,
                                range=""+str(b)+"!A383:A384").execute()

print(request9, request10, "(All Operations - Successfully!)")

# python3 /home/luke_blue/Startup_Files/import_csv_data_from_urls.py
