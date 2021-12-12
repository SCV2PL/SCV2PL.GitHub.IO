from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'
sheet_id = '0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


RUN1 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': 266,
            'endRowIndex': 273,
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': 273,
            'endRowIndex': 280,
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "pasteType": "Paste_FORMAT",

    }},

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=RUN1).execute()
print(request1)

RUN2 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': 266,
            'endRowIndex': 273,
            'startColumnIndex': 7,
            'endColumnIndex': 16,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': 273,
            'endRowIndex': 280,
            'startColumnIndex': 7,
            'endColumnIndex': 16,
        },
        "pasteType": "Paste_FORMULA",

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=RUN2).execute()
print(request2)

RUN3 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': 266,
            'endRowIndex': 273,
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': 266,
            'endRowIndex': 273,
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "pasteType": "Paste_VALUES",

    }},

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=RUN3).execute()
print(request3)

result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range="Średnia 7 dni SARS-CoV-2!A274").execute()
values = result.get('values', [])

RUN4 = [["=B273", "=C273", "=D273", "=E273", "=F273", "=G273",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!B2")'],

        ["=C273", "=D273", "=E273", "=F273", "=G273",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-14!B2")'],

        ["=D273", "=E273", "=F273", "=G273",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-14!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-15!B2")'],

        ["=E273", "=F273", "=G273",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-14!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-15!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-16!B2")'],

        ["=F273", "=G273",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-14!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-15!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-16!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-17!B2")'],

        ["=G273",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-14!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-15!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-16!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-17!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-18!B2")'],

        [
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-14!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-15!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-16!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-17!B2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-18!B2")',
            '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-119-12!B2")']]

request4 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                  range="Średnia 7 dni SARS-CoV-2!A274",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN4}).execute()
print(request4)

result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range="Średnia 7 dni SARS-CoV-2!M274").execute()
values = result.get('values', [])

RUN5 = [[
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!H2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-13!D2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-14!H2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-14!D2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-15!H2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-15!D2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-16!H2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-16!D2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-17!H2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-17!D2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-18!H2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-18!D2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-19!H2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "2021-12-19!D2"))']]

request5 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                  range="Średnia 7 dni SARS-CoV-2!M274",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN5}).execute()
print(request5)

# startup-script --- /home/luke_blue_lox/startupscript.sh
# python3 /home/luke_blue/Startup_Files/sunday_update/update_array_range_7_days.py
