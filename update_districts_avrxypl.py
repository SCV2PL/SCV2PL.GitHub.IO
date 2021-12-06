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


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="avrxypl!J1").execute()
values = result.get('values', [])

RUN = [["=({'2021-12-01'!D2}+{'2021-12-02'!D2}+{'2021-12-03'!D2}+{'2021-12-04'!D2}+{'2021-12-05'!D2}+{'2021-12-06'!D2}+{'2021-12-07'!D2})/7"]]

request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="avrxypl!J1", valueInputOption="USER_ENTERED", body={"values":RUN}).execute()
                                                 
print(request)

# python3 /home/luke_blue/Startup_Files/daily_update/update_districts_avrxypl.py
