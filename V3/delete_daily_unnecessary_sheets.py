from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import time
import yaml

SERVICE_ACCOUNT_FILE = '/home/blox_land/Desktop/SCV2PL/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
spreadsheet_id1 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
spreadsheet_id2 = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'
spreadsheet_id3 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


config_vals = ""
with open("/home/blox_land/Desktop/SCV2PL/config_for_delete_daily_unnecessary_sheets_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

n = config_vals['n']


while n > 0:

  config_vals = ""
  with open("/home/blox_land/Desktop/SCV2PL/config_for_delete_daily_unnecessary_sheets_py.yaml", "r") as cr:
     config_vals = yaml.full_load(cr)

  a = config_vals['a']
  b = config_vals['b']
  c = config_vals['c']
  n = config_vals['n']

  yesterdayn = datetime.today() - timedelta(days=b)
  d = yesterdayn.strftime('%Y%m%d')

  yesterdayn = datetime.today() - timedelta(days=c)
  e = yesterdayn.strftime('%Y%m%d')


  RUN1 = {'requests': [
      {
      "deleteSheet": {
        "sheetId": str(a)
      }
    },

  ]}

  request1 = service.spreadsheets().batchUpdate(
          spreadsheetId=spreadsheet_id1, body=RUN1).execute()
        
  print(request1)
        

  RUN2 = {'requests': [
      {
      "deleteSheet": {
        "sheetId": str(d)
      }
    },

  ]}

  request2 = service.spreadsheets().batchUpdate(
          spreadsheetId=spreadsheet_id2, body=RUN2).execute()
        
  print(request2)
        
        
  RUN3 = {'requests': [
      {
      "deleteSheet": {
        "sheetId": str(e)
      }
    },

  ]}

  request3 = service.spreadsheets().batchUpdate(
          spreadsheetId=spreadsheet_id3, body=RUN3).execute()
        
  print(request3)
  
  
  config_vals['a'] = a + 1
  with open("/home/blox_land/Desktop/SCV2PL/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
     yaml.dump(config_vals, cw, default_flow_style=True)
  
  config_vals['b'] = b - 1
  with open("/home/blox_land/Desktop/SCV2PL/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
     yaml.dump(config_vals, cw, default_flow_style=True)

  config_vals['c'] = c - 1
  with open("/home/blox_land/Desktop/SCV2PL/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
     yaml.dump(config_vals, cw, default_flow_style=True)
  
  config_vals['n'] = n - 1
  with open("/home/blox_land/Desktop/SCV2PL/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
     yaml.dump(config_vals, cw, default_flow_style=True)


  print("(All Operations - Successfully!)")
  
  continue
  
  print("EXIT...")
  
# 235! skip to 237

  break #exit
