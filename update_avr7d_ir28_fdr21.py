from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="ir28!B3").execute()
values = result.get('values', [])

RUN1 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!H241:H268")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!I241:I268")']]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="ir28!B3", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="fdr21!B3").execute()
values = result.get('values', [])

RUN2 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!O248:O268")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!P248:P268")']]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="fdr21!B3", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="dr!A1").execute()
values = result.get('values', [])

RUN3 = [["='Średnia 7 dni SARS-CoV-2'!L268"]]

request3 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="dr!A1", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()                                                

print(request1, request2, request3)

# python3 /home/luke_blue/Startup_Files/update_avr7d_ir28_fdr21.py
