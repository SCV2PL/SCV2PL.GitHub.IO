from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

request1 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Średnia 7 dni - Zakres 2 tygodnie!B4:C16").execute()
request2 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Średnia 7 dni - Zakres 4 tygodnie!B4:C30").execute()
request3 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Prognoza liczby zgonów - 21 dni do przodu!B4:C23").execute()
request4 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Karkonoski!B3:C15").execute()
request5 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Jelenia Góra!B3:C15").execute()
request6 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Dolnośląskie!B3:C15").execute()
request7 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Wrocław!B3:C15").execute()

print(request1, request2, request3, request4, request5,request6,request7)
