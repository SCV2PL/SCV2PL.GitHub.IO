from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


request1 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="TodayCount!D3:D382").execute()

request2 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="TodaySum!D3:D382").execute()
                               
"""request3 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="TodaySum!H3:H382").execute()"""
                               
request4 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="XY!F1:D380").execute()
                               
request5 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="XY!C1:C380").execute()
                               
request6 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="support!P1:P380").execute()

print(request1, request2, request3, request4, request5, request6)
