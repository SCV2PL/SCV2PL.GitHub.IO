from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
from datetime import datetime

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
a = datetime.today().strftime('%Y%m%d') #'20220208'
b = datetime.today().strftime('%Y-%m-%d') #'2022-02-08'
spreadsheet_id1 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'
sheet_id1 = a

spreadsheet_id2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
sheet_id2 = a

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range=""+str(b)+"!A1").execute()
values = result.get('values', [])

RUN1 = [['=QUERY(IMPORTDATA("https://api.dane.gov.pl/resources/33185,aktualne-dane-dla-wojewodztw/file";",";";");"Select Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,Col11,Col12,Col13,Col14,Col15,Col16,Col17,Col18,Col19,Col20")']]

request1 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range=""+str(b)+"!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN1}).execute()
time.sleep(6)
print(request1)

RUN2 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "pasteType": "Paste_Values",

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN2).execute()
print(request2)


result = sheet.values().get(spreadsheetId=spreadsheet_id2,
                            range=""+str(b)+"!A1").execute()
values = result.get('values', [])

RUN3 = [['=QUERY(IMPORTDATA("https://api.dane.gov.pl/resources/33186,aktualne-dane-dla-powiatow/file",",";";"),"Select Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,Col11,Col12,Col13,Col14,Col15,Col16,Col17,Col18,Col19,Col20,Col21")']]

request3 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id2,
                                                  range=""+str(b)+"!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN3}).execute()
time.sleep(6)
print(request3)

result = sheet.values().get(spreadsheetId=spreadsheet_id2,
                            range=""+str(b)+"!A766").execute()
values = result.get('values', [])


RUN4= {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 21,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 21,
        },
        "pasteType": "Paste_Values",

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN4).execute()
print(request4)


print("(All Operations - Successfully!)")
