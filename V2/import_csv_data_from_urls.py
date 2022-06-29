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
                            range=""+str(b)+"!A19").execute()
values = result.get('values', [])

RUN1 = [['https://api.dane.gov.pl/resources/33185,aktualne-dane-dla-wojewodztw/file'],

        ['=IMPORTDATA(A19)']]

request1 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range=""+str(b)+"!A19",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN1}).execute()
time.sleep(3)
result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range=""+str(b)+"!A38").execute()
values = result.get('values', [])

RUN2 = [['=SPLIT(A20;";")']]

request2 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range=""+str(b)+"!A38",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN2}).execute()
print(request1, request2)
time.sleep(3)

RUN3 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id1,
            'startRowIndex': 37,
            'endRowIndex': 55,
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
            'startRowIndex': 37,
            'endRowIndex': 55,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 37,
            'endRowIndex': 55,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "pasteType": "Paste_Values",

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN4).execute()
print(request4)

RUN5 = [['=SUBSTITUTE(A38;"""";"")']]

request5 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range=""+str(b)+"!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN5}).execute()
print(request4)

RUN6 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },

    }},

]}

request6 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN6).execute()
print(request6)
time.sleep(5)

RUN7 = {'requests': [
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

request7 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN7).execute()
print(request7)

request8 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range=""+str(b)+"!A19:Z1000").execute()
print(request8)



result = sheet.values().get(spreadsheetId=spreadsheet_id2,
                            range=""+str(b)+"!A383").execute()
values = result.get('values', [])

RUN11 = [['https://api.dane.gov.pl/resources/33186,aktualne-dane-dla-powiatow/file'],

        ['=IMPORTDATA(A383)']]

request11 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id2,
                                                  range=""+str(b)+"!A383",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN11}).execute()
print(request1)
time.sleep(3)

result = sheet.values().get(spreadsheetId=spreadsheet_id2,
                            range=""+str(b)+"!A766").execute()
values = result.get('values', [])

RUN12 = [['=SPLIT(A384;";")']]

request12 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id2,
                                                  range=""+str(b)+"!A766",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN12}).execute()
print(request12)
time.sleep(3)

RUN13 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id2,
            'startRowIndex': 765,
            'endRowIndex': 1147,
            'startColumnIndex': 0,
            'endColumnIndex': 1,
        },

    }},

]}

request13 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN13).execute()
print(request13)
time.sleep(13)

RUN14= {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 765,
            'endRowIndex': 1147,
            'startColumnIndex': 0,
            'endColumnIndex': 21,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 765,
            'endRowIndex': 1147,
            'startColumnIndex': 0,
            'endColumnIndex': 21,
        },
        "pasteType": "Paste_Values",

    }},

]}

request14 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN14).execute()
print(request14)


RUN15 = [['=SUBSTITUTE(A766;"""";"")']]

request15 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id2,
                                                  range=""+str(b)+"!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN15}).execute()

RUN16 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 27,
        },

    }},

]}

request16 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN16).execute()
print(request16)
time.sleep(10)

RUN17 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 27,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 27,
        },
        "pasteType": "Paste_Values",

    }},

]}

request17 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN17).execute()
print(request17)

request18 = sheet.values().clear(spreadsheetId=spreadsheet_id2,
                                range=""+str(b)+"!A383:Z1200").execute()
print(request18)

print("(All Operations - Successfully!)")

# python3 /app/import_csv_data_from_urls.py
