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
                            range="XY!J1").execute()
values = result.get('values', [])

RUN1 = [["=({'2021-11-24'!E3}+{'2021-11-25'!E3}+{'2021-11-26'!E3}+{'2021-11-27'!E3}+{'2021-11-28'!E3}+{'2021-11-29'!E3}+{'2021-11-30'!E3}+{'2021-12-01'!E3}+{'2021-12-02'!E3}+{'2021-12-03'!E3}+{'2021-12-04'!E3}+{'2021-12-05'!E3}+{'2021-12-06'!E3}+{'2021-12-07'!E3})/K1"]]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                  range="XY!J1", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN1}).execute()

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="TodayCount!D3").execute()
values = result.get('values', [])

RUN2 = [["={'2021-12-01'!D3}+{'2021-12-02'!D3}+{'2021-12-03'!D3}+{'2021-12-04'!D3}+{'2021-12-05'!D3}+{'2021-12-06'!D3}+{'2021-12-07'!D3}"]]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                  range="TodayCount!D3", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN2}).execute()
print(request1, request2)

# python3 /home/luke_blue/Startup_Files/update_districts_j1_xy_d3_todaycount.py