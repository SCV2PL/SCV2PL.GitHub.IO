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

yesterday14 = datetime.today() - timedelta(days=14)
o = yesterday14.strftime('%Y-%m-%d')


SPREADSHEET_ID = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


request1 = sheet.values().clear(spreadsheetId=SPREADSHEET_ID,
                               range="Support - 7DAVRDLR14D!R2:AF2").execute()

print(request1)

RUN2 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(o)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(n)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(m)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(l)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(k)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(j)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(i)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(h)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(g)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(f)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(e)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(d)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(c)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(b)+' - SUM!M1:M380")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0","'+str(a)+' - SUM!M1:M380")',]]

request2 = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                  range="Support - 7DAVRDLR14D!R2",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN2}).execute()
print(request2)

print("(All Operations - Successfully!)")
