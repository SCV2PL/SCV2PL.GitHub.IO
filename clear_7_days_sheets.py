from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_green_player/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '11WYKo8wPV5qYkzddxyc7a4ICXhpo_bWKftBpJ-_3uMw'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

request1 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Dzień 1!B2:O18").execute()
request2 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Dzień 2!B2:O18").execute()
request3 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Dzień 3!B2:O18").execute()
request4 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Dzień 4!B2:O18").execute()
request5 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Dzień 5!B2:O18").execute()
request6 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Dzień 6!B2:O18").execute()
request7 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                               range="Dzień 7!B2:O18").execute()
request8 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Dzień 1 / 100000!B2:P382").execute()
request9 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Dzień 2 / 100000!B2:P382").execute()
request10 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Dzień 3 / 100000!B2:P382").execute()
request11 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Dzień 4 / 100000!B2:P382").execute()
request12 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Dzień 5 / 100000!B2:P382").execute()
request13 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Dzień 6 / 100000!B2:P382").execute()
request14 = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Dzień 7 / 100000!B2:P382").execute()

print(request1, request2, request3, request4, request5, request6, request7,request8, request9, request10, request11, request12, request13, request14)

#/home/luke_blue_lox/startupscript.sh
