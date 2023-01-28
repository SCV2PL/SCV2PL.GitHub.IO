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
from datetime import timedelta
import yaml

SERVICE_ACCOUNT_FILE = 'sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

config_vals = ""
with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
n = config_vals['n']
Source1 = config_vals['Source1']
Source2 = config_vals['Source2']
datetime = config_vals['datetime']
spreadsheet_id1 = config_vals['ID1V1']
spreadsheet_id2 = config_vals['ID2V1']

while n > 0:
    config_vals = ""
    with open("config_create_sheets.yaml", "r") \
            as cr:
        config_vals = yaml.full_load(cr)
        n = config_vals['n']

        day_n = datetime - timedelta(days=n)
        a = day_n.strftime('%Y%m%d')
        b = day_n.strftime('%Y-%m-%d')
        print(a)
        print(b)
        filepaths1 = ''+str(Source1)+''+str(a)+'.csv'
        filepaths2 = ''+str(Source2)+''+str(a)+'.csv'
        print(filepaths1)
        print(filepaths2)

    RUN1 = [['=IMPORTDATA("'+str(filepaths1)+'";",")']]
    request1 = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id1,
        range=""+str(b)+"!A1",
        valueInputOption="USER_ENTERED",
        body={"values": RUN1}).execute()
    print(request1)

    RUN2 = {'requests': [
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
    request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1,
        body=RUN2).execute()
    print(request2)

    RUN3 = {"requests": [
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
    request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1,
        body=RUN3).execute()
    print(request3)

    RUN31 = {'requests': [
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
    request31 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN31).execute()
    print(request31)

    RUN4 = [['=IMPORTDATA("'+str(filepaths2)+'",",")']]
    request4 = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id2,
        range=""+str(b)+"!A1",
        valueInputOption="USER_ENTERED",
        body={"values": RUN4}).execute()
    print(request4)

    RUN5 = {'requests': [
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
    request5 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2,
        body=RUN5).execute()
    print(request5)

    RUN6 = {"requests": [
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
    request6 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2,
        body=RUN6).execute()
    print(request6)

    RUN61 = {'requests': [
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
    request61 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN61).execute()
    print(request61)

    config_vals['n'] = n - 1
    with open("config_create_sheets.yaml",
              "w") as cw:
        yaml.dump(config_vals, cw, default_flow_style=True)

    continue

    break  # exit
