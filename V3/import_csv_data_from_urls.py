"""PEP 8 – Style Guide for Python Code

https://peps.python.org/pep-0008

Is this style acceptable by convention and accepted by the python community ???
Łukasz "Luke Blue" Andruszkiewicz
✌💙💚♻️🌌🚀🌎🌍🌏🛰🌌♻️💚💙✌
2023-01-17 - After my #BrainFuck: my final interpretation of #Python #PEP8.
#PyCharm #IDE
✌💙💚♻️🌌🚀🌎🌍🌏🛰🌌♻️💚💙✌
"""
from google.oauth2 import service_account
from googleapiclient.discovery import build
import yaml
import time

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

SERVICE_ACCOUNT_FILE = ''+str(CORE)+'sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
Source1 = config_vals['Source1']
Source2 = config_vals['Source2']
t = config_vals['datetime']
spreadsheet_id1 = config_vals['ID1']
spreadsheet_id2 = config_vals['ID2']

a = t.strftime("%Y%m%d")
b = t
print(a)
print(b)
filepaths1 = '' + str(Source1) + '' + str(a) + '.csv'
filepaths2 = '' + str(Source2) + '' + str(a) + '.csv'
print(filepaths1)
print(filepaths2)

RUN = [['=IMPORTDATA("' + str(filepaths1) + '";",")']]
request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id1,
    range="" + str(b) + "!A1",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)
time.sleep(5)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': a,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 19
        },
        "destination": {
            'sheetId': a,
            'startRowIndex': 0,
            'endRowIndex': 18,
            'startColumnIndex': 0,
            'endColumnIndex': 19
        },
        "pasteType": "Paste_Values"
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id1,
    body=RUN).execute()
print(request)

RUN = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": a,
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
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id1,
    body=RUN).execute()
print(request)

RUN = {'requests': [
    {
        "deleteDimension": {
            "range": {
                "sheetId": a,
                "dimension": "ROWS",
                "startIndex": 18,
                "endIndex": 1000
            }
        }
    }
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id1, body=RUN).execute()
print(request)

RUN = {'requests': [
    {
        "deleteDimension": {
            "range": {
                "sheetId": a,
                "dimension": "COLUMNS",
                "startIndex": 19,
                "endIndex": 26
            }
        }
    }
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id1, body=RUN).execute()
print(request)

RUN = [['=IMPORTDATA("' + str(filepaths2) + '",",")']]
request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id2,
    range="" + str(b) + "!A1",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)
time.sleep(10)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': a,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 20
        },
        "destination": {
            'sheetId': a,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 20
        },
        "pasteType": "Paste_Values"
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id2,
    body=RUN).execute()
print(request)

RUN = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": a,
            "startRowIndex": 0,
            "endRowIndex": 382,
            "startColumnIndex": 19,
            "endColumnIndex": 20
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
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id2,
    body=RUN).execute()
print(request)

RUN = {'requests': [
    {
        "deleteDimension": {
            "range": {
                "sheetId": a,
                "dimension": "ROWS",
                "startIndex": 382,
                "endIndex": 1200
            }
        }
    }
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id2, body=RUN).execute()
print(request)

RUN = {'requests': [
    {
        "deleteDimension": {
            "range": {
                "sheetId": a,
                "dimension": "COLUMNS",
                "startIndex": 20,
                "endIndex": 26
            }
        }
    }
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id2, body=RUN).execute()
print(request)
