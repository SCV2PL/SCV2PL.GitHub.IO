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
                            range="XY!C1").execute()
values = result.get('values', [])

RUN1 = [['=NOW()']]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="XY!C1", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="XY!K1").execute()
values = result.get('values', [])

RUN2 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","support!G1:G380")']]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="XY!K1", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="XY!F1").execute()
values = result.get('values', [])

RUN3 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c","XY!J1:J380")']]

request3 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="XY!F1", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()
                                                 
print(request1, request2, request3)

# python3 /home/luke_blue/Startup_Files/update_districts_date_xy.py
