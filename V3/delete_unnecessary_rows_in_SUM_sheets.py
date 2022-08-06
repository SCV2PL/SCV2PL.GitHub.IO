from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
from datetime import datetime, timedelta
import yaml

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
spreadsheet_id1 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
spreadsheet_id2 = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


while True:

  config_vals = ""
  with open("/app/config_for_delete_unnecessary_rows_in_SUM_sheets_py.yaml", "r") as cr:
     config_vals = yaml.full_load(cr)

  a = config_vals['a']
  b = config_vals['b']

  yesterdayn = datetime.today() - timedelta(days=b)
  c = yesterdayn.strftime('%Y%m%d')


  RUN1 = {'requests': [
      {
        "deleteDimension": {
          "range": {
            "sheetId": str(a),
            "dimension": "ROWS",
            "startIndex": 380,
            "endIndex": 1000
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
            "sheetId": str(c),
            "dimension": "ROWS",
            "startIndex": 382,
            "endIndex": 1000
          }
        }
      },

  ]}

  request2 = service.spreadsheets().batchUpdate(
          spreadsheetId=spreadsheet_id2, body=RUN2).execute()
  print(request2)


  config_vals['a'] = a - 1
  with open("/app/config_for_delete_unnecessary_rows_in_SUM_sheets_py.yaml", "w") as cw:
     yaml.dump(config_vals, cw, default_flow_style=True)
   
  config_vals['b'] = b + 1
  with open("/app/config_for_delete_unnecessary_rows_in_SUM_sheets_py.yaml", "w") as cw:
     yaml.dump(config_vals, cw, default_flow_style=True) 
   
  print("(All Operations - Successfully!)")

  check = input("Do you want to quit or start gain, enter Y to restart or another to end ?: ")

  if check.upper() == "Y": #go back to the top

    continue
  
  print("EXIT...")

  break #exit
