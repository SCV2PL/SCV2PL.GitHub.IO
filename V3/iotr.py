from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta

SERVICE_ACCOUNT_FILE = '/home/blox_land/scv2pl/sars-cov-2-poland.json'
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

yesterday14 = datetime.today() - timedelta(days=14)
o = yesterday14.strftime('%Y-%m-%d')

yesterday15 = datetime.today() - timedelta(days=15)
p = yesterday15.strftime('%Y-%m-%d')

yesterday16 = datetime.today() - timedelta(days=16)
r = yesterday16.strftime('%Y-%m-%d')

yesterday17 = datetime.today() - timedelta(days=17)
s = yesterday17.strftime('%Y-%m-%d')

yesterday18 = datetime.today() - timedelta(days=18)
t = yesterday18.strftime('%Y-%m-%d')

yesterday19 = datetime.today() - timedelta(days=19)
u = yesterday19.strftime('%Y-%m-%d')   
    

SPREADSHEET_ID1 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'
SPREADSHEET_ID2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID1,
                            range="O!A1").execute()
values = result.get('values', [])

RUN1 = [["=({'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2})/7","=({'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2})/7","=({'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2})/7"]]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID1,
                                                  range="O!A1", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN1}).execute()
                                                  
                                  
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID2,
                            range="14D TREND - avrxypl-iot!A2").execute()
values = result.get('values', [])

RUN2 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A1:C1")',"","",str(n)],
["=({'"+str(t)+"'!E2}+{'"+str(s)+"'!E2}+{'"+str(r)+"'!E2}+{'"+str(p)+"'!E2}+{'"+str(o)+"'!E2}+{'"+str(n)+"'!E2}+{'"+str(m)+"'!E2})/7","=({'"+str(t)+"'!L2}+{'"+str(s)+"'!L2}+{'"+str(r)+"'!L2}+{'"+str(p)+"'!L2}+{'"+str(o)+"'!L2}+{'"+str(n)+"'!L2}+{'"+str(m)+"'!L2})/7","=({'"+str(t)+"'!O2}+{'"+str(s)+"'!O2}+{'"+str(r)+"'!O2}+{'"+str(p)+"'!O2}+{'"+str(o)+"'!O2}+{'"+str(n)+"'!O2}+{'"+str(m)+"'!O2})/7",str(m)],
["=({'"+str(s)+"'!E2}+{'"+str(r)+"'!E2}+{'"+str(p)+"'!E2}+{'"+str(o)+"'!E2}+{'"+str(n)+"'!E2}+{'"+str(m)+"'!E2}+{'"+str(l)+"'!E2})/7","=({'"+str(s)+"'!L2}+{'"+str(r)+"'!L2}+{'"+str(p)+"'!L2}+{'"+str(o)+"'!L2}+{'"+str(n)+"'!L2}+{'"+str(m)+"'!L2}+{'"+str(l)+"'!L2})/7","=({'"+str(s)+"'!O2}+{'"+str(r)+"'!O2}+{'"+str(p)+"'!O2}+{'"+str(o)+"'!O2}+{'"+str(n)+"'!O2}+{'"+str(m)+"'!O2}+{'"+str(l)+"'!O2})/7",str(l)],
["=({'"+str(r)+"'!E2}+{'"+str(p)+"'!E2}+{'"+str(o)+"'!E2}+{'"+str(n)+"'!E2}+{'"+str(m)+"'!E2}+{'"+str(l)+"'!E2}+{'"+str(k)+"'!E2})/7","=({'"+str(r)+"'!L2}+{'"+str(p)+"'!L2}+{'"+str(o)+"'!L2}+{'"+str(n)+"'!L2}+{'"+str(m)+"'!L2}+{'"+str(l)+"'!L2}+{'"+str(k)+"'!L2})/7","=({'"+str(r)+"'!O2}+{'"+str(p)+"'!O2}+{'"+str(o)+"'!O2}+{'"+str(n)+"'!O2}+{'"+str(m)+"'!O2}+{'"+str(l)+"'!O2}+{'"+str(k)+"'!O2})/7",str(k)],
["=({'"+str(p)+"'!E2}+{'"+str(o)+"'!E2}+{'"+str(n)+"'!E2}+{'"+str(m)+"'!E2}+{'"+str(l)+"'!E2}+{'"+str(k)+"'!E2}+{'"+str(j)+"'!E2})/7","=({'"+str(p)+"'!L2}+{'"+str(o)+"'!L2}+{'"+str(n)+"'!L2}+{'"+str(m)+"'!L2}+{'"+str(l)+"'!L2}+{'"+str(k)+"'!L2}+{'"+str(j)+"'!L2})/7","=({'"+str(p)+"'!O2}+{'"+str(o)+"'!O2}+{'"+str(n)+"'!O2}+{'"+str(m)+"'!O2}+{'"+str(l)+"'!O2}+{'"+str(k)+"'!O2}+{'"+str(j)+"'!O2})/7",str(j)],
["=({'"+str(o)+"'!E2}+{'"+str(n)+"'!E2}+{'"+str(m)+"'!E2}+{'"+str(l)+"'!E2}+{'"+str(k)+"'!E2}+{'"+str(j)+"'!E2}+{'"+str(i)+"'!E2})/7","=({'"+str(o)+"'!L2}+{'"+str(n)+"'!L2}+{'"+str(m)+"'!L2}+{'"+str(l)+"'!L2}+{'"+str(k)+"'!L2}+{'"+str(j)+"'!L2}+{'"+str(i)+"'!L2})/7","=({'"+str(o)+"'!O2}+{'"+str(n)+"'!O2}+{'"+str(m)+"'!O2}+{'"+str(l)+"'!O2}+{'"+str(k)+"'!O2}+{'"+str(j)+"'!O2}+{'"+str(i)+"'!O2})/7",str(i)],
["=({'"+str(n)+"'!E2}+{'"+str(m)+"'!E2}+{'"+str(l)+"'!E2}+{'"+str(k)+"'!E2}+{'"+str(j)+"'!E2}+{'"+str(i)+"'!E2}+{'"+str(h)+"'!E2})/7","=({'"+str(n)+"'!L2}+{'"+str(m)+"'!L2}+{'"+str(l)+"'!L2}+{'"+str(k)+"'!L2}+{'"+str(j)+"'!L2}+{'"+str(i)+"'!L2}+{'"+str(h)+"'!L2})/7","=({'"+str(n)+"'!O2}+{'"+str(m)+"'!O2}+{'"+str(l)+"'!O2}+{'"+str(k)+"'!O2}+{'"+str(j)+"'!O2}+{'"+str(i)+"'!O2}+{'"+str(h)+"'!O2})/7",str(h)],
["=({'"+str(m)+"'!E2}+{'"+str(l)+"'!E2}+{'"+str(k)+"'!E2}+{'"+str(j)+"'!E2}+{'"+str(i)+"'!E2}+{'"+str(h)+"'!E2}+{'"+str(g)+"'!E2})/7","=({'"+str(m)+"'!L2}+{'"+str(l)+"'!L2}+{'"+str(k)+"'!L2}+{'"+str(j)+"'!L2}+{'"+str(i)+"'!L2}+{'"+str(h)+"'!L2}+{'"+str(g)+"'!L2})/7","=({'"+str(m)+"'!O2}+{'"+str(l)+"'!O2}+{'"+str(k)+"'!O2}+{'"+str(j)+"'!O2}+{'"+str(i)+"'!O2}+{'"+str(h)+"'!O2}+{'"+str(g)+"'!O2})/7",str(g)],
["=({'"+str(l)+"'!E2}+{'"+str(k)+"'!E2}+{'"+str(j)+"'!E2}+{'"+str(i)+"'!E2}+{'"+str(h)+"'!E2}+{'"+str(g)+"'!E2}+{'"+str(f)+"'!E2})/7","=({'"+str(l)+"'!L2}+{'"+str(k)+"'!L2}+{'"+str(j)+"'!L2}+{'"+str(i)+"'!L2}+{'"+str(h)+"'!L2}+{'"+str(g)+"'!L2}+{'"+str(f)+"'!L2})/7","=({'"+str(l)+"'!O2}+{'"+str(k)+"'!O2}+{'"+str(j)+"'!O2}+{'"+str(i)+"'!O2}+{'"+str(h)+"'!O2}+{'"+str(g)+"'!O2}+{'"+str(f)+"'!O2})/7",str(f)],
["=({'"+str(k)+"'!E2}+{'"+str(j)+"'!E2}+{'"+str(i)+"'!E2}+{'"+str(h)+"'!E2}+{'"+str(g)+"'!E2}+{'"+str(f)+"'!E2}+{'"+str(e)+"'!E2})/7","=({'"+str(k)+"'!L2}+{'"+str(j)+"'!L2}+{'"+str(i)+"'!L2}+{'"+str(h)+"'!L2}+{'"+str(g)+"'!L2}+{'"+str(f)+"'!L2}+{'"+str(e)+"'!L2})/7","=({'"+str(k)+"'!O2}+{'"+str(j)+"'!O2}+{'"+str(i)+"'!O2}+{'"+str(h)+"'!O2}+{'"+str(g)+"'!O2}+{'"+str(f)+"'!O2}+{'"+str(e)+"'!O2})/7",str(e)],
["=({'"+str(j)+"'!E2}+{'"+str(i)+"'!E2}+{'"+str(h)+"'!E2}+{'"+str(g)+"'!E2}+{'"+str(f)+"'!E2}+{'"+str(e)+"'!E2}+{'"+str(d)+"'!E2})/7","=({'"+str(j)+"'!L2}+{'"+str(i)+"'!L2}+{'"+str(h)+"'!L2}+{'"+str(g)+"'!L2}+{'"+str(f)+"'!L2}+{'"+str(e)+"'!L2}+{'"+str(d)+"'!L2})/7","=({'"+str(j)+"'!O2}+{'"+str(i)+"'!O2}+{'"+str(h)+"'!O2}+{'"+str(g)+"'!O2}+{'"+str(f)+"'!O2}+{'"+str(e)+"'!O2}+{'"+str(d)+"'!O2})/7",str(d)],
["=({'"+str(i)+"'!E2}+{'"+str(h)+"'!E2}+{'"+str(g)+"'!E2}+{'"+str(f)+"'!E2}+{'"+str(e)+"'!E2}+{'"+str(d)+"'!E2}+{'"+str(c)+"'!E2})/7","=({'"+str(i)+"'!L2}+{'"+str(h)+"'!L2}+{'"+str(g)+"'!L2}+{'"+str(f)+"'!L2}+{'"+str(e)+"'!L2}+{'"+str(d)+"'!L2}+{'"+str(c)+"'!L2})/7","=({'"+str(i)+"'!O2}+{'"+str(h)+"'!O2}+{'"+str(g)+"'!O2}+{'"+str(f)+"'!O2}+{'"+str(e)+"'!O2}+{'"+str(d)+"'!O2}+{'"+str(c)+"'!O2})/7",str(c)],
["=({'"+str(h)+"'!E2}+{'"+str(g)+"'!E2}+{'"+str(f)+"'!E2}+{'"+str(e)+"'!E2}+{'"+str(d)+"'!E2}+{'"+str(c)+"'!E2}+{'"+str(b)+"'!E2})/7","=({'"+str(h)+"'!L2}+{'"+str(g)+"'!L2}+{'"+str(f)+"'!L2}+{'"+str(e)+"'!L2}+{'"+str(d)+"'!L2}+{'"+str(c)+"'!L2}+{'"+str(b)+"'!L2})/7","=({'"+str(h)+"'!O2}+{'"+str(g)+"'!O2}+{'"+str(f)+"'!O2}+{'"+str(e)+"'!O2}+{'"+str(d)+"'!O2}+{'"+str(c)+"'!O2}+{'"+str(b)+"'!O2})/7",str(b)],
["=({'"+str(g)+"'!E2}+{'"+str(f)+"'!E2}+{'"+str(e)+"'!E2}+{'"+str(d)+"'!E2}+{'"+str(c)+"'!E2}+{'"+str(b)+"'!E2}+{'"+str(a)+"'!E2})/7","=({'"+str(g)+"'!L2}+{'"+str(f)+"'!L2}+{'"+str(e)+"'!L2}+{'"+str(d)+"'!L2}+{'"+str(c)+"'!L2}+{'"+str(b)+"'!L2}+{'"+str(a)+"'!L2})/7","=({'"+str(g)+"'!O2}+{'"+str(f)+"'!O2}+{'"+str(e)+"'!O2}+{'"+str(d)+"'!O2}+{'"+str(c)+"'!O2}+{'"+str(b)+"'!O2}+{'"+str(a)+"'!O2})/7",str(a)]]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID2,
                                                  range="14D TREND - avrxypl-iot!A2", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN2}).execute()
