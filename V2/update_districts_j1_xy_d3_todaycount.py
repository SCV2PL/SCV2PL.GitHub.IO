from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
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

RUN1 = [["=({'"+str(n)+"'!I3}+{'"+str(m)+"'!I3}+{'"+str(l)+"'!I3}+{'"+str(k)+"'!I3}+{'"+str(j)+"'!I3}+{'"+str(i)+"'!I3}+{'"+str(h)+"'!I3}+{'"+str(g)+"'!I3}+{'"+str(f)+"'!I3}+{'"+str(e)+"'!I3}+{'"+str(d)+"'!I3}+{'"+str(c)+"'!I3}+{'"+str(b)+"'!I3}+{'"+str(a)+"'!I3})/K1"]]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                  range="XY!J1", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN1}).execute()

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="TodayCount!D3").execute()
values = result.get('values', [])

RUN2 = [["={'"+str(g)+"'!H3}+{'"+str(f)+"'!H3}+{'"+str(e)+"'!H3}+{'"+str(d)+"'!H3}+{'"+str(c)+"'!H3}+{'"+str(b)+"'!H3}+{'"+str(a)+"'!H3}"]]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                  range="TodayCount!D3", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN2}).execute()
print(request1, request2)

# python3 /app/update_districts_j1_xy_d3_todaycount.py
