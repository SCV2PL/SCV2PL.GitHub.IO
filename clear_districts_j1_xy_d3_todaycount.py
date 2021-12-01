from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

request1 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                                range="XY!J2:J380").execute()

request2 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                                range="TodayCount!D4:D382").execute()

print(request1, request2)

# python3 /home/luke_blue/Startup_Files/clear_districts_j1_xy_d3_todaycount.py