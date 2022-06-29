from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


nextday1 = datetime.today() + timedelta(days=1)
a = nextday1.strftime('%Y%m%d')

nextday2 = datetime.today() + timedelta(days=1)
b = nextday2.strftime('%Y-%m-%d')

nextday3 = datetime.today() + timedelta(days=2)
c = nextday3.strftime('%Y%m%d')

nextday4 = datetime.today() + timedelta(days=2)
d = nextday4.strftime('%Y-%m-%d')

nextday5 = datetime.today() + timedelta(days=3)
e = nextday5.strftime('%Y%m%d')

nextday6 = datetime.today() + timedelta(days=3)
f = nextday6.strftime('%Y-%m-%d')

nextday7 = datetime.today() + timedelta(days=4)
g = nextday7.strftime('%Y%m%d')

nextday8 = datetime.today() + timedelta(days=4)
h = nextday8.strftime('%Y-%m-%d')

nextday9 = datetime.today() + timedelta(days=5)
i = nextday9.strftime('%Y%m%d')

nextday10 = datetime.today() + timedelta(days=5)
j = nextday10.strftime('%Y-%m-%d')

nextday11 = datetime.today() + timedelta(days=6)
k = nextday11.strftime('%Y%m%d')

nextday12 = datetime.today() + timedelta(days=6)
l = nextday12.strftime('%Y-%m-%d')

nextday13 = datetime.today() + timedelta(days=7)
m = nextday13.strftime('%Y%m%d')

nextday14 = datetime.today() + timedelta(days=7)
n = nextday14.strftime('%Y-%m-%d')


spreadsheet_id1 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'

spreadsheet_id2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

RUN1 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(a),
            "title": ''+str(b)+'',
        },

    }},

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN1).execute()
print(request1)

RUN2 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(c),
            "title": ''+str(d)+'',
        },

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN2).execute()
print(request2)

RUN3 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(e),
            "title": ''+str(f)+'',
        },

    }},

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN3).execute()
print(request3)

RUN4 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(g),
            "title": ''+str(h)+'',
        },

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN4).execute()
print(request4)

RUN5 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(i),
            "title": ''+str(j)+'',
        },

    }},

]}

request5 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN5).execute()
print(request5)

RUN6 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(k),
            "title": ''+str(l)+'',
        },

    }},

]}

request6 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN6).execute()
print(request6)

RUN7 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(m),
            "title": ''+str(n)+'',
        },

    }},

]}

request7 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN7).execute()
print(request7)

RUN8 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(a),
            "title": ''+str(b)+'',
        },

    }},
    
    {"appendDimension": {
        "sheetId": str(a),
        "dimension": "ROWS",
        "length": 200
        },
     },

]}

request8 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN8).execute()
print(request8)

RUN9 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(c),
            "title": ''+str(d)+'',
        },

    }},
    
    {"appendDimension": {
        "sheetId": str(c),
        "dimension": "ROWS",
        "length": 200
        },
     },

]}

request9 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN9).execute()
print(request9)

RUN10 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(e),
            "title": ''+str(f)+'',
        },

    }},
    
    {"appendDimension": {
        "sheetId": str(e),
        "dimension": "ROWS",
        "length": 200
        },
     },

]}

request10 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN10).execute()
print(request10)

RUN11 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(g),
            "title": ''+str(h)+'',
        },

    }},
    
    {"appendDimension": {
        "sheetId": str(g),
        "dimension": "ROWS",
        "length": 200
        },
     },

]}

request11 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN11).execute()
print(request11)

RUN12 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(i),
            "title": ''+str(j)+'',
        },

    }},
    
    {"appendDimension": {
        "sheetId": str(i),
        "dimension": "ROWS",
        "length": 200
        },
     },

]}

request12 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN12).execute()
print(request12)

RUN13 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(k),
            "title": ''+str(l)+'',
        },

    }},
    
    {"appendDimension": {
        "sheetId": str(k),
        "dimension": "ROWS",
        "length": 200
        },
     },

]}

request13 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN13).execute()
print(request13)

RUN14 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": str(m),
            "title": ''+str(n)+'',
        },

    }},
    
    {"appendDimension": {
        "sheetId": str(m),
        "dimension": "ROWS",
        "length": 200
        },
     },

]}

request14 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN14).execute()
print(request14)

# python3 /app/sunday_update/add_weekly_sheets_set.py
# 'deleteSheet'
