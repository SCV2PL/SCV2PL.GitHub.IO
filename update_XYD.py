from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="XY!F1").execute()
values = result.get('values', [])

RUN1 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c","XY!J1:D380")']]

request1 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="XY!F1", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()
                                                 
print(request1)

# /home/luke_blue_lox/startupscript.sh
