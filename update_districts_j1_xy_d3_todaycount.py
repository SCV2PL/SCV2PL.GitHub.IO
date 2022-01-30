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
g = yesterday6.strftime('%Y-%m-%d')

yesterday7 = datetime.today() - timedelta(days=7)
h = yesterday7.strftime('%Y-%m-%d')

yesterday8 = datetime.today() - timedelta(days=8)
i = yesterday8.strftime('%Y-%m-%d')

yesterday9 = datetime.today() - timedelta(days=9)
j = yesterday9.strftime('%Y-%m-%d')

yesterday10 = datetime.today() - timedelta(days=10)
k = yesterday10.strftime('%Y-%m-%d')

yesterday11 = datetime.today() - timedelta(days=11)
l = yesterday11.strftime('%Y-%m-%d')

yesterday12 = datetime.today() - timedelta(days=12)
m = yesterday12.strftime('%Y-%m-%d')

yesterday13 = datetime.today() - timedelta(days=13)
n = yesterday13.strftime('%Y-%m-%d')    
    

SPREADSHEET_ID = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="XY!J1").execute()
values = result.get('values', [])

RUN1 = [["=({'"+str(n)+"'!E3}+{'"+str(m)+"'!E3}+{'"+str(l)+"'!E3}+{'"+str(k)+"'!E3}+{'"+str(j)+"'!E3}+{'"+str(i)+"'!E3}+{'"+str(h)+"'!E3}+{'"+str(g)+"'!E3}+{'"+str(f)+"'!E3}+{'"+str(e)+"'!E3}+{'"+str(d)+"'!E3}+{'"+str(c)+"'!E3}+{'"+str(b)+"'!E3}+{'"+str(a)+"'!E3})/K1"]]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                  range="XY!J1", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN1}).execute()

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="TodayCount!D3").execute()
values = result.get('values', [])

RUN2 = [["={'"+str(g)+"'!D3}+{'"+str(f)+"'!D3}+{'"+str(e)+"'!D3}+{'"+str(d)+"'!D3}+{'"+str(c)+"'!D3}+{'"+str(b)+"'!D3}+{'"+str(a)+"'!D3}"]]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                  range="TodayCount!D3", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN2}).execute()
print(request1, request2)

# python3 /home/luke_blue/Startup_Files/update_districts_j1_xy_d3_todaycount.py
