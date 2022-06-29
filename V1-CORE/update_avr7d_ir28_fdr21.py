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

a = config_vals['a']
b = config_vals['b']
c = config_vals['c']
d = config_vals['d']

        

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

RUN2 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!O'+str(c)+':O'+str(b)+'")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!T'+str(c)+':T'+str(b)+'")']]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="fdr21!B3", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="dr!A1").execute()
values = result.get('values', [])

RUN3 = [["='Średnia 7 dni SARS-CoV-2'!L"+str(b)+""]]

request3 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="dr!A1", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()                                                



result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="ir2021-08-15-today!B3").execute()
values = result.get('values', [])

RUN4 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!H154:H'+str(b)+'")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!I154:I'+str(b)+'")']]

request4 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="ir2021-08-15-today!B3", valueInputOption="USER_ENTERED", body={"values":RUN4}).execute()
                                                 
                                                 
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="DIID-2021-08-15-today!B3").execute()
values = result.get('values', [])

RUN5 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!N154:N'+str(b)+'")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!I154:I'+str(b)+'")']]

request5 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="DIID-2021-08-15-today!B3", valueInputOption="USER_ENTERED", body={"values":RUN5}).execute()
                                                 


config_vals['a'] = a + 1
with open("/app/config_for_update_avr7d_ir28_fdr21_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['b'] = b + 1
with open("/app/config_for_update_avr7d_ir28_fdr21_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['c'] = c + 1
with open("/app/config_for_update_avr7d_ir28_fdr21_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['d'] = d + 1
with open("/app/config_for_update_avr7d_ir28_fdr21_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)


print(request1, request2, request3, request4, request5)

# python3 /app/update_avr7d_ir28_fdr21.py
