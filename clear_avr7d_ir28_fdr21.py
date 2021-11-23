from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

request1 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="ir28!B4:C30").execute()
request2 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="fdr21!B4:C23").execute()

print(request1, request2)
