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
        
spreadsheet_id1 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

config_vals = ""
with open("/app/config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

n = config_vals['n']


while n > 0:

  config_vals = ""
  with open("/app/config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml", "r") as cr:
     config_vals = yaml.full_load(cr)

  a = config_vals['a']
  n = config_vals['n']

  yesterdayn = datetime.today() - timedelta(days=a)
  b = yesterdayn.strftime('%Y%m%d')


  RUN1 = {'requests': [
      {
        "deleteDimension": {
          "range": {
            "sheetId": str(b),
            "dimension": "ROWS",
            "startIndex": 18,
            "endIndex": 1000
          }
        }
      },

  ]}

  request1 = service.spreadsheets().batchUpdate(
          spreadsheetId=spreadsheet_id1, body=RUN1).execute()
  print(request1)


  config_vals['a'] = a + 1
  with open("/app/config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml", "w") as cw:
     yaml.dump(config_vals, cw, default_flow_style=True) 
   
  config_vals['n'] = n - 1
  with open("/app/config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml", "w") as cw:
     yaml.dump(config_vals, cw, default_flow_style=True) 
   
  print("(All Operations - Successfully!)")

  continue
  
  print("EXIT...")

  break #exit
