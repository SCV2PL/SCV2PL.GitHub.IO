from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="TodaySum!D3").execute()
values = result.get('values', [])

RUN1 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","TodayCount!D3:D382")']]

request1 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="TodaySum!D3", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="TodaySum!H3").execute()
values = result.get('values', [])

RUN2 = [['17.11.2021 10:30:00']]

request2 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="TodaySum!H3", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="XY!F1").execute()
values = result.get('values', [])

RUN3 = [['={TodaySum!D3:D382}']]

request3 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="XY!F1", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()
                                                 
                                                 

print(request1, request2, request3)

# /home/luke_blue_lox/startupscript.sh
