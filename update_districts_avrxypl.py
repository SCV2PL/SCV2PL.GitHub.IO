from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
        
a = datetime.today().strftime('%Y-%m-%d')

yesterday1 = datetime.today() - timedelta(days=1)
b = yesterday1.strftime('%Y-%m-%d')

yesterday2 = datetime.today() - timedelta(days=2)
c = yesterday2.strftime('%Y-%m-%d')

yesterday3 = datetime.today() - timedelta(days=3)
d = yesterday3.strftime('%Y-%m-%d')

yesterday4 = datetime.today() - timedelta(days=4)
e = yesterday4.strftime('%Y-%m-%d')

yesterday5 = datetime.today() - timedelta(days=5)
f = yesterday5.strftime('%Y-%m-%d')

yesterday6 = datetime.today() - timedelta(days=6)
g = yesterday6.strftime('%Y-%m-%d'
        

SPREADSHEET_ID = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="avrxypl!J1").execute()
values = result.get('values', [])

RUN = [["=({'"+str(g)+"'!D2}+{'"+str(f)+"'!D2}+{'"+str(e)+"'!D2}+{'"+str(d)+"'!D2}+{'"+str(c)+"'!D2}+{'"+str(b)+"'!D2}+{'"+str(a)+"'!D2})/7"]]

request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range="avrxypl!J1", valueInputOption="USER_ENTERED", body={"values":RUN}).execute()
                                                 
print(request)

# python3 /home/luke_blue/Startup_Files/daily_update/update_districts_avrxypl.py
