from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
                               
request1 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="XY!K1:K380").execute()
                              

request2 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="XY!F1:F380").execute()
                               
print(request1, request2)
