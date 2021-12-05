from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id1 = '1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g'

spreadsheet_id2 = '1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

RUN1 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211206,
            "title": '2021-12-06',
        },

    }},

]}

request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN1).execute()
print(request1)

RUN2 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211207,
            "title": '2021-12-07',
        },

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN2).execute()
print(request2)

RUN3 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211208,
            "title": '2021-12-08',
        },

    }},

]}

request3 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN3).execute()
print(request3)

RUN4 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211209,
            "title": '2021-12-09',
        },

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN4).execute()
print(request4)

RUN5 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211210,
            "title": '2021-12-10',
        },

    }},

]}

request5 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN5).execute()
print(request5)

RUN6 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211211,
            "title": '2021-12-11',
        },

    }},

]}

request6 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN6).execute()
print(request6)

RUN7 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211212,
            "title": '2021-12-12',
        },

    }},

]}

request7 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN7).execute()
print(request7)


RUN8 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211206,
            "title": '2021-12-06',
        },

    }},

]}

request8 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN8).execute()
print(request8)

RUN9 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211207,
            "title": '2021-12-07',
        },

    }},

]}

request9 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN9).execute()
print(request9)

RUN10 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211208,
            "title": '2021-12-08',
        },

    }},

]}

request10 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN10).execute()
print(request10)

RUN11 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211209,
            "title": '2021-12-09',
        },

    }},

]}

request11 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN11).execute()
print(request11)

RUN12 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211210,
            "title": '2021-12-10',
        },

    }},

]}

request12 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN12).execute()
print(request12)

RUN13 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211211,
            "title": '2021-12-11',
        },

    }},

]}

request13 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN13).execute()
print(request13)

RUN14 = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": 20211212,
            "title": '2021-12-12',
        },

    }},

]}

request14 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN14).execute()
print(request14)

# python3 /home/luke_blue/Startup_Files/add_weekly_sheets_set.py