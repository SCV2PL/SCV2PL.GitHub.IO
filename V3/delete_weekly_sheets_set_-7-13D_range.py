from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
spreadsheet_id1 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


yesterdayn = datetime.today() - timedelta(days=7)
a = yesterdayn.strftime('%Y%m%d')

yesterdayn = datetime.today() - timedelta(days=8)
b = yesterdayn.strftime('%Y%m%d')

yesterdayn = datetime.today() - timedelta(days=9)
c = yesterdayn.strftime('%Y%m%d')

yesterdayn = datetime.today() - timedelta(days=10)
d = yesterdayn.strftime('%Y%m%d')

yesterdayn = datetime.today() - timedelta(days=11)
e = yesterdayn.strftime('%Y%m%d')

yesterdayn = datetime.today() - timedelta(days=12)
f = yesterdayn.strftime('%Y%m%d')

yesterdayn = datetime.today() - timedelta(days=13)
g = yesterdayn.strftime('%Y%m%d')


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
      "sheetId": str(b)
    }
  },

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN2).execute()
  
print(request2)

RUN3 = {'requests': [
    {
    "deleteSheet": {
      "sheetId": str(c)
    }
  },

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN3).execute()
  
print(request3)

RUN4 = {'requests': [
    {
    "deleteSheet": {
      "sheetId": str(d)
    }
  },

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN4).execute()
  
print(request4)

RUN5 = {'requests': [
    {
    "deleteSheet": {
      "sheetId": str(e)
    }
  },

]}

request5 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN5).execute()
  
print(request5)

RUN6 = {'requests': [
    {
    "deleteSheet": {
      "sheetId": str(f)
    }
  },

]}

request6 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN6).execute()
  
print(request6)
 
RUN7 = {'requests': [
    {
    "deleteSheet": {
      "sheetId": str(g)
    }
  },

]}

request7 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN7).execute()
  
print(request7)   

print("(All Operations - Successfully!)")
