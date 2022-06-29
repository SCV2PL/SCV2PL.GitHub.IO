from googleapiclient.discovery import build
from google.oauth2 import service_account
import yaml

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
config_vals = ""
with open("/app/config_for_update_avr7d_ir28_fdr21_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

d = config_vals['d']

SPREADSHEET_ID = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


request1 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="ir28!B4:C30").execute()
request2 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="fdr21!B4:C23").execute()
request3 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="ir2021-08-15-today!B3:C"+str(d)+"").execute()
request4 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="DIID-2021-08-15-today!B3:C"+str(d)+"").execute()

print(request1, request2, request3, request4)
