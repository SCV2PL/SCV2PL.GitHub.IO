from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
from datetime import datetime
import yaml


SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
a = datetime.today().strftime('%Y%m%d')
b = datetime.today().strftime('%Y-%m-%d')


config_vals = ""
with open("/app/config_for_save_daily_sum_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

c = config_vals['c']


spreadsheet_id1 = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'
sheet_id1 = '335219542'

spreadsheet_id2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
sheet_id2 = '0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

RUN1 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(a),
            "title": ''+str(b)+' - SUM',
        },

    }},

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN1).execute()
print(request1)

RUN11 = {'requests': [
    {
      "deleteDimension": {
        "range": {
          "sheetId": str(a),
          "dimension": "ROWS",
          "startIndex": 382,
          "endIndex": 1000
        }
      }
    },

]}

request11 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN11).execute()
print(request11)


RUN2 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(c),
            "title": ''+str(b)+' - SUM',
        },

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN2).execute()
print(request2)

RUN22 = {'requests': [
    {
      "deleteDimension": {
        "range": {
          "sheetId": str(c),
          "dimension": "ROWS",
          "startIndex": 380,
          "endIndex": 1000
        }
      }
    },

]}

request22 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN22).execute()
print(request22)


RUN3 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 4,
            'endColumnIndex': 17,
        },
        "destination": {
            'sheetId': str(a),
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 4,
            'endColumnIndex': 17,
        },
        "pasteType": "Paste_Values",

    }},

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN3).execute()
        

RUN4 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 380,
            'startColumnIndex': 2,
            'endColumnIndex': 11,
        },
        "destination": {
            'sheetId': str(c),
            'startRowIndex': 0,
            'endRowIndex': 380,
            'startColumnIndex': 2,
            'endColumnIndex': 11,
        },
        "pasteType": "Paste_Values",

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN4).execute()

print(request3, request4)


RUN5 = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": str(a),
            "startRowIndex": 0,
            "endRowIndex": 382,
            "startColumnIndex": 15,
            "endColumnIndex": 17
        },
        "cell": {
            "userEnteredFormat": {
                "numberFormat": {
                    "type": "DATE_TIME",
                    "pattern": "yyyy-mm-dd hh:mm:ss am/pm"
                }
            }
        },
        "fields": "userEnteredFormat.numberFormat"

    }},

]}

request5 = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id1, body=RUN5).execute()
print(request5)

RUN6 = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": str(c),
            "startRowIndex": 0,
            "endRowIndex": 380,
            "startColumnIndex": 2,
            "endColumnIndex": 3
        },
        "cell": {
            "userEnteredFormat": {
                "numberFormat": {
                    "type": "DATE_TIME",
                    "pattern": "yyyy-mm-dd hh:mm:ss am/pm"
                }
            }
        },
        "fields": "userEnteredFormat.numberFormat"

    }},

]}

request6 = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id2, body=RUN6).execute()
print(request6)


config_vals['c'] = c + 1
with open("/app/config_for_save_daily_sum_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
   
print("(All Operations - Successfully!)")
   
# python3 /app/save_daily_sum.py
