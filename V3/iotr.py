from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta
import time
import yaml

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

yesterday20 = datetime.today() - timedelta(days=20)
v = yesterday20.strftime('%Y-%m-%d')

yesterday21 = datetime.today() - timedelta(days=21)
w = yesterday21.strftime('%Y-%m-%d')

yesterday22 = datetime.today() - timedelta(days=22)
x = yesterday22.strftime('%Y-%m-%d')

yesterday23 = datetime.today() - timedelta(days=23)
y = yesterday23.strftime('%Y-%m-%d')

yesterday24 = datetime.today() - timedelta(days=24)
z = yesterday24.strftime('%Y-%m-%d')

yesterday25 = datetime.today() - timedelta(days=25)
aa = yesterday25.strftime('%Y-%m-%d')

yesterday26 = datetime.today() - timedelta(days=26)
ab = yesterday26.strftime('%Y-%m-%d')

yesterday27 = datetime.today() - timedelta(days=27)
ac = yesterday27.strftime('%Y-%m-%d')

yesterday28 = datetime.today() - timedelta(days=28)
ad = yesterday28.strftime('%Y-%m-%d')

yesterday29 = datetime.today() - timedelta(days=29)
ae = yesterday29.strftime('%Y-%m-%d')

yesterday30 = datetime.today() - timedelta(days=30)
af = yesterday30.strftime('%Y-%m-%d')

yesterday31 = datetime.today() - timedelta(days=31)
ag = yesterday31.strftime('%Y-%m-%d')

yesterday32 = datetime.today() - timedelta(days=32)
ah = yesterday32.strftime('%Y-%m-%d')

yesterday33 = datetime.today() - timedelta(days=33)
ai = yesterday33.strftime('%Y-%m-%d')  
    

SPREADSHEET_ID1 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'
SPREADSHEET_ID2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'
sheet_id2 = '934571935'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID1,
                            range="O!A1").execute()
values = result.get('values', [])

RUN1 = [["=({'"+str(ai)+"'!D2}+{'"+str(ah)+"'!D2}+{'"+str(ag)+"'!D2}+{'"+str(af)+"'!D2}+{'"+str(ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2})/7","=({'"+str(ai)+"'!K2}+{'"+str(ah)+"'!K2}+{'"+str(ag)+"'!K2}+{'"+str(af)+"'!K2}+{'"+str(ae)+"'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2})/7","=({'"+str(ai)+"'!N2}+{'"+str(ah)+"'!N2}+{'"+str(ag)+"'!N2}+{'"+str(af)+"'!N2}+{'"+str(ae)+"'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2})/7"],
["=({'"+str(ah)+"'!D2}+{'"+str(ag)+"'!D2}+{'"+str(af)+"'!D2}+{'"+str(ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2})/7","=({'"+str(ah)+"'!K2}+{'"+str(ag)+"'!K2}+{'"+str(af)+"'!K2}+{'"+str(ae)+"'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2})/7","=({'"+str(ah)+"'!N2}+{'"+str(ag)+"'!N2}+{'"+str(af)+"'!N2}+{'"+str(ae)+"'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2})/7"],
["=({'"+str(ag)+"'!D2}+{'"+str(af)+"'!D2}+{'"+str(ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2})/7","=({'"+str(ag)+"'!K2}+{'"+str(af)+"'!K2}+{'"+str(ae)+"'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2})/7","=({'"+str(ag)+"'!N2}+{'"+str(af)+"'!N2}+{'"+str(ae)+"'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2})/7"],
["=({'"+str(af)+"'!D2}+{'"+str(ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2})/7","=({'"+str(af)+"'!K2}+{'"+str(ae)+"'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2})/7","=({'"+str(af)+"'!N2}+{'"+str(ae)+"'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2})/7"],
["=({'"+str(ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(y)+"'!D2})/7","=({'"+str(ae)+"'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+"'!K2})/7","=({'"+str(ae)+"'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+"'!N2})/7"],
["=({'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+"'!D2})/7","=({'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+"'!K2})/7","=({'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+"'!N2})/7"],
["=({'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(w)+"'!D2})/7","=({'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+"'!K2})/7","=({'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+"'!N2})/7"],
["=({'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(w)+"'!D2}+{'"+str(v)+"'!D2})/7","=({'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+"'!K2})/7","=({'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+"'!N2})/7"],
["=({'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(u)+"'!D2})/7","=({'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+"'!K2})/7","=({'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+"'!N2}+{'"+str(u)+"'!N2})/7"],
["=({'"+str(z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(t)+"'!D2})/7","=({'"+str(z)+"'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+"'!K2})/7","=({'"+str(z)+"'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+"'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2})/7"],
["=({'"+str(y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2})/7","=({'"+str(y)+"'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2})/7","=({'"+str(y)+"'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+"'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2})/7"],
["=({'"+str(x)+"'!D2}+{'"+str(w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2})/7","=({'"+str(x)+"'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2})/7","=({'"+str(x)+"'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+"'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+"'!N2})/7"],
["=({'"+str(w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2})/7","=({'"+str(w)+"'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2})/7","=({'"+str(w)+"'!N2}+{'"+str(v)+"'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2})/7"],
["=({'"+str(v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2})/7","=({'"+str(v)+"'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2})/7","=({'"+str(v)+"'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2})/7"],
["=({'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2})/7","=({'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2})/7","=({'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2})/7"],
["=({'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(m)+"'!D2})/7","=({'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+"'!K2})/7","=({'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+"'!N2})/7"],
["=({'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(m)+"'!D2}+{'"+str(l)+"'!D2})/7","=({'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+"'!K2}+{'"+str(l)+"'!K2})/7","=({'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+"'!N2}+{'"+str(l)+"'!N2})/7"],
["=({'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(m)+"'!D2}+{'"+str(l)+"'!D2}+{'"+str(k)+"'!D2})/7","=({'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+"'!K2}+{'"+str(l)+"'!K2}+{'"+str(k)+"'!K2})/7","=({'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+"'!N2}+{'"+str(l)+"'!N2}+{'"+str(k)+"'!N2})/7"],
["=({'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(m)+"'!D2}+{'"+str(l)+"'!D2}+{'"+str(k)+"'!D2}+{'"+str(j)+"'!D2})/7","=({'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+"'!K2}+{'"+str(l)+"'!K2}+{'"+str(k)+"'!K2}+{'"+str(j)+"'!K2})/7","=({'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+"'!N2}+{'"+str(l)+"'!N2}+{'"+str(k)+"'!N2}+{'"+str(j)+"'!N2})/7"],
["=({'"+str(o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(m)+"'!D2}+{'"+str(l)+"'!D2}+{'"+str(k)+"'!D2}+{'"+str(j)+"'!D2}+{'"+str(i)+"'!D2})/7","=({'"+str(o)+"'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+"'!K2}+{'"+str(l)+"'!K2}+{'"+str(k)+"'!K2}+{'"+str(j)+"'!K2}+{'"+str(i)+"'!K2})/7","=({'"+str(o)+"'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+"'!N2}+{'"+str(l)+"'!N2}+{'"+str(k)+"'!N2}+{'"+str(j)+"'!N2}+{'"+str(i)+"'!N2})/7"]]

request1 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID1,
                                                  range="O!A1", valueInputOption="USER_ENTERED",
                                                  body={"values": RUN1}).execute()
                                                  
print(request1)
                                                  
                                  
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID2,
                            range="14D TREND - avrxypl-iot!A2").execute()
values = result.get('values', [])

RUN2 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A1:C1")',"","",str(ac)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A2:C2")',"","",str(ab)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A3:C3")',"","",str(aa)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A4:C4")',"","",str(z)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A5:C5")',"","",str(y)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A6:C6")',"","",str(x)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A7:C7")',"","",str(w)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A8:C8")',"","",str(v)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A9:C9")',"","",str(u)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A10:C10")',"","",str(t)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A11:C11")',"","",str(s)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A12:C12")',"","",str(r)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A13:C13")',"","",str(p)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A14:C14")',"","",str(o)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A15:C15")',"","",str(n)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A16:C16")',"","",str(m)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A17:C17")',"","",str(l)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A18:C18")',"","",str(k)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A19:C19")',"","",str(j)],
['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g","O!A20:C20")',"","",str(i)],
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
                                                  
time.sleep(15)
print(request2)


RUN3 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 29,
            'startColumnIndex': 0,
            'endColumnIndex': 4,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 29,
            'startColumnIndex': 0,
            'endColumnIndex': 4,
        },
        "pasteType": "Paste_Values",

    }},

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID2, body=RUN3).execute()

print(request3)


config_vals = ""
with open("/app/config_for_delete_daily_unnecessary_sheets_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

d = config_vals['d']

RUN4 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 29,
            'startColumnIndex': 0,
            'endColumnIndex': 13,
        },
        "destination": {
            'sheetId': str(d),
            'startRowIndex': 0,
            'endRowIndex': 29,
            'startColumnIndex': 12,
            'endColumnIndex': 25,
        },
        "pasteType": "Paste_Values",

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID2, body=RUN4).execute()

print(request4)

config_vals['d'] = d + 1
with open("/app/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)


print("(All Operations - Successfully!)")
