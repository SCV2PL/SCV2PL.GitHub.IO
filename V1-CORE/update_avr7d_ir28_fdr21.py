from googleapiclient.discovery import build
from google.oauth2 import service_account
import yaml

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
        
config_vals = ""
with open("/home/luke_blue/Startup_Files/config_for_update_avr7d_ir28_fdr21_py.yaml", "r") as cr:
   config_vals = yaml.load(cr)

a = config_vals['a']
b = config_vals['b']
c = config_vals['c']
        

SPREADSHEET_ID = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="ir28!B3").execute()
values = result.get('values', [])

RUN1 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!H'+str(a)+':H'+str(b)+'")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!I'+str(a)+':I'+str(b)+'")']]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="ir28!B3", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="fdr21!B3").execute()
values = result.get('values', [])

RUN2 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!O'+str(c)+':O'+str(b)+'")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!P'+str(c)+':P'+str(b)+'")']]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="fdr21!B3", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="dr!A1").execute()
values = result.get('values', [])

RUN3 = [["='Średnia 7 dni SARS-CoV-2'!L"+str(b)+""]]

request3 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="dr!A1", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()                                                


config_vals['a'] = a + 1
with open("/home/luke_blue/Startup_Files/config_for_update_avr7d_ir28_fdr21_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['b'] = b + 1
with open("/home/luke_blue/Startup_Files/config_for_update_avr7d_ir28_fdr21_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['c'] = c + 1
with open("/home/luke_blue/Startup_Files/config_for_update_avr7d_ir28_fdr21_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)


print(request1, request2, request3)

# python3 /home/luke_blue/Startup_Files/update_avr7d_ir28_fdr21.py
