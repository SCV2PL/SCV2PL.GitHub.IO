from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
from datetime import datetime

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

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
            'endColumnIndex': 19,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 19,
        },
        "pasteType": "Paste_Values",

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN2).execute()
print(request2)

RUN3 = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": sheet_id1,
            "startRowIndex": 0,
            "endRowIndex": 18,
            "startColumnIndex": 18,
            "endColumnIndex": 19
        },
        "cell": {
            "userEnteredFormat": {
                "numberFormat": {
                    "type": "DATE_TIME",
                    "pattern": "yyyy-mm-dd"
                }
            }
        },
        "fields": "userEnteredFormat.numberFormat"

    }},

]}

request3 = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id1, body=RUN3).execute()
print(request3)


RUN4 = [['=QUERY(IMPORTDATA("https://api.dane.gov.pl/resources/33186,aktualne-dane-dla-powiatow/file",",";";"),"Select Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,Col11,Col12,Col13,Col14,Col15,Col16,Col17,Col18,Col19,Col20,Col21")']]

request4 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id2,
                                                  range=""+str(b)+"!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN4}).execute()
time.sleep(6)
print(request4)

RUN5= {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "pasteType": "Paste_Values",

    }},

]}

request5 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN5).execute()
print(request5)

RUN6 = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": sheet_id2,
            "startRowIndex": 0,
            "endRowIndex": 382,
            "startColumnIndex": 19,
            "endColumnIndex": 20,
        },
        "cell": {
            "userEnteredFormat": {
                "numberFormat": {
                    "type": "DATE_TIME",
                    "pattern": "yyyy-mm-dd"
                }
            }
        },
        "fields": "userEnteredFormat.numberFormat"

    }},

]}

request6 = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id2, body=RUN6).execute()
print(request6)


print("(All Operations - Successfully!)")