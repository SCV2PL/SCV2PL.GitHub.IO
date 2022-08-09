from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
spreadsheet_id1 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
spreadsheet_id2 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


a = datetime.today().strftime('%Y%m%d')


RUN1 = {'requests': [
    {
      "deleteDimension": {
        "range": {
          "sheetId": str(a),
          "dimension": "ROWS",
          "startIndex": 382,
          "endIndex": 1200
        }
      }
    },

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN1).execute()

print(request1)


RUN2 = {'requests': [
    {
      "deleteDimension": {
        "range": {
          "sheetId": str(a),
          "dimension": "ROWS",
          "startIndex": 18,
          "endIndex": 1000
        }
      }
    },

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN2).execute()

print(request2)
   

print("(All Operations - Successfully!)")
