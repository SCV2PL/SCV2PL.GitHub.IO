from googleapiclient.discovery import build
from google.oauth2 import service_account
import yaml
from datetime import datetime, timedelta

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


config_vals = ""
with open("/app/config_for_update_avr7d_array_range_7d_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

a = config_vals['a']
b = config_vals['b']
c = config_vals['c']
d = config_vals['d']


nextday1 = datetime.today() + timedelta(days=1)
a1 = nextday1.strftime('%d.%m.%Y')

nextday2 = datetime.today() + timedelta(days=2)
b1 = nextday2.strftime('%d.%m.%Y')

nextday3 = datetime.today() + timedelta(days=3)
c1 = nextday3.strftime('%d.%m.%Y')

nextday4 = datetime.today() + timedelta(days=4)
d1 = nextday4.strftime('%d.%m.%Y')

nextday5 = datetime.today() + timedelta(days=5)
e1 = nextday5.strftime('%d.%m.%Y')

nextday6 = datetime.today() + timedelta(days=6)
f1 = nextday6.strftime('%d.%m.%Y')

nextday7 = datetime.today() + timedelta(days=7)
g1 = nextday7.strftime('%d.%m.%Y')


a2 = nextday1.strftime('%Y-%m-%d')

b2 = nextday2.strftime('%Y-%m-%d')

c2 = nextday3.strftime('%Y-%m-%d')

d2 = nextday4.strftime('%Y-%m-%d')

e2 = nextday5.strftime('%Y-%m-%d')

f2 = nextday6.strftime('%Y-%m-%d')

g2 = nextday7.strftime('%Y-%m-%d')


nextday22 = datetime.today() + timedelta(days=22)
a3 = nextday22.strftime('%d.%m.%Y')

nextday23 = datetime.today() + timedelta(days=23)
b3 = nextday23.strftime('%d.%m.%Y')

nextday24 = datetime.today() + timedelta(days=24)
c3 = nextday24.strftime('%d.%m.%Y')

nextday25 = datetime.today() + timedelta(days=25)
d3 = nextday25.strftime('%d.%m.%Y')

nextday26 = datetime.today() + timedelta(days=26)
e3 = nextday26.strftime('%d.%m.%Y')

nextday27 = datetime.today() + timedelta(days=27)
f3 = nextday27.strftime('%d.%m.%Y')

nextday28 = datetime.today() + timedelta(days=28)
g3 = nextday28.strftime('%d.%m.%Y')


spreadsheet_id = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'
sheet_id = '0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


RUN1 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': str(a),#+7
            'endRowIndex': str(b),#+7
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': str(b),#+7
            'endRowIndex': str(c),#+7
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "pasteType": "Paste_FORMAT",

    }},

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=RUN1).execute()
print(request1)

RUN2 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': str(a),#+7
            'endRowIndex': str(b),#+7
            'startColumnIndex': 7,
            'endColumnIndex': 16,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': str(b),#+7
            'endRowIndex': str(c),#+7
            'startColumnIndex': 7,
            'endColumnIndex': 16,
        },
        "pasteType": "Paste_FORMULA",

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=RUN2).execute()
print(request2)

RUN3 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': str(a),#+7
            'endRowIndex': str(b),#+7
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': str(a),#+7
            'endRowIndex': str(b),#+7
            'startColumnIndex': 0,
            'endColumnIndex': 16,
        },
        "pasteType": "Paste_VALUES",

    }},

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=RUN3).execute()
print(request3)

result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range="Średnia 7 dni SARS-CoV-2!A"+str(d)+"").execute()
values = result.get('values', [])

RUN4 = [["=B"+str(b)+"", "=C"+str(b)+"", "=D"+str(b)+"", "=E"+str(b)+"", "=F"+str(b)+"", "=G"+str(b)+"",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!E2")'],

        ["=C"+str(b)+"", "=D"+str(b)+"", "=E"+str(b)+"", "=F"+str(b)+"", "=G"+str(b)+"",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(b2)+'!E2")'],

        ["=D"+str(b)+"", "=E"+str(b)+"", "=F"+str(b)+"", "=G"+str(b)+"",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(b2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(c2)+'!E2")'],

        ["=E"+str(b)+"", "=F"+str(b)+"", "=G"+str(b)+"",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(b2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(c2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(d2)+'!E2")'],

        ["=F"+str(b)+"", "=G"+str(b)+"",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(b2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(c2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(d2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(e2)+'!E2")'],

        ["=G"+str(b)+"",
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(b2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(c2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(d2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(e2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(f2)+'!E2")'],

        [
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(b2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(c2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(d2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(e2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(f2)+'!E2")',
         '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(g2)+'!E2")']]

request4 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                  range="Średnia 7 dni SARS-CoV-2!A"+str(d)+"",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN4}).execute()
print(request4)

result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range="Średnia 7 dni SARS-CoV-2!M"+str(d)+"").execute()
values = result.get('values', [])

RUN5 = [[
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!M2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(a2)+'!I2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(b2)+'!M2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(b2)+'!I2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(c2)+'!M2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(c2)+'!I2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(d2)+'!M2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(d2)+'!I2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(e2)+'!M2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(e2)+'!I2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(f2)+'!M2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(f2)+'!I2"))'],

        [
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(g2)+'!M2"))',
            '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c", "'+str(g2)+'!I2"))']]

request5 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                  range="Średnia 7 dni SARS-CoV-2!M"+str(d)+"",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN5}).execute()
print(request5)


request6 = sheet.values().clear(spreadsheetId=spreadsheet_id,
                                range="Średnia 7 dni SARS-CoV-2!I"+str(d)+":I"+str(c)+"").execute()
print(request6)


result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range="Średnia 7 dni SARS-CoV-2!I"+str(d)+"").execute()
values = result.get('values', [])

RUN7 = [[
            '=IF(H:H="","","'+str(a1)+'")'],

        [
            '=IF(H:H="","","'+str(b1)+'")'],

        [
            '=IF(H:H="","","'+str(c1)+'")'],

        [
            '=IF(H:H="","","'+str(d1)+'")'],

        [
            '=IF(H:H="","","'+str(e1)+'")'],

        [
            '=IF(H:H="","","'+str(f1)+'")'],

        [
            '=IF(H:H="","","'+str(g1)+'")']]

request7 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                  range="Średnia 7 dni SARS-CoV-2!I"+str(d)+"",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN7}).execute()
print(request7)


request8 = sheet.values().clear(spreadsheetId=spreadsheet_id,
                                range="Średnia 7 dni SARS-CoV-2!O"+str(d)+":O"+str(c)+"").execute()
print(request8)


result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range="Średnia 7 dni SARS-CoV-2!O"+str(d)+"").execute()
values = result.get('values', [])

RUN9 = [[
            '=IF(N:N="","","'+str(a3)+'")'],

        [
            '=IF(N:N="","","'+str(b3)+'")'],

        [
            '=IF(N:N="","","'+str(c3)+'")'],

        [
            '=IF(N:N="","","'+str(d3)+'")'],

        [
            '=IF(N:N="","","'+str(e3)+'")'],

        [
            '=IF(N:N="","","'+str(f3)+'")'],

        [
            '=IF(N:N="","","'+str(g3)+'")']]

request9 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                  range="Średnia 7 dni SARS-CoV-2!O"+str(d)+"",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN9}).execute()
print(request9)


config_vals['a'] = a + 7
with open("/app/config_for_update_avr7d_array_range_7d_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['b'] = b + 7
with open("/app/config_for_update_avr7d_array_range_7d_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['c'] = c + 7
with open("/app/config_for_update_avr7d_array_range_7d_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)

config_vals['d'] = d + 7
with open("/app/config_for_update_avr7d_array_range_7d_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
print("(All Operations - Successfully!)")

# python3 /app/sunday_update/update_avr7d_array_range_7d.py
# https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM/edit#gid=0
