from google.oauth2 import service_account
from googleapiclient.discovery import build
import time

SERVICE_ACCOUNT_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

spreadsheet_id1 = '1t5ndsyAp20qeOgCJrzeT_HUttgfru1SzwrhCFJzsgu0'
sheet_id1 = '1705435509'
sheet_id2 = '2008036218'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


request1 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range="PWPZ!A1:X4958").execute()
print(request1)


result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range="PWPZ!A2480").execute()
values = result.get('values', [])

RUN2 = [['https://api.dane.gov.pl/media/resources/20211207/poziom_wyszczepienia_mieszka%C5%84c%C3%B3w_gmin_w_dniu_20211206_wska%C5%BAniki.csv'],

        ['=IMPORTDATA(A2480)']]

request2 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range="PWPZ!A2480",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN2}).execute()
print(request2)
time.sleep(3)


result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range="PWPZ!A1").execute()
values = result.get('values', [])

RUN3 = [['=SPLIT(A2481;";")']]

request3 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range="PWPZ!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN3}).execute()
print(request3)


RUN4 = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 2478,
            'startColumnIndex': 0,
            'endColumnIndex': 1,
        },

    }},

]}

request4 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN4).execute()
print(request4)
time.sleep(30)


RUN5 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 2478,
            'startColumnIndex': 0,
            'endColumnIndex': 10,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 2478,
            'startColumnIndex': 0,
            'endColumnIndex': 10,
        },
        "pasteType": "Paste_Values",

    }},

]}

request5 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN5).execute()
print(request5)


request6 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range="PWPZ!A2480:X4958").execute()
print(request6)
time.sleep(20)


RUN7 = {'requests': [
    {
      'sortRange': {
        'range': {
          'sheetId': sheet_id1,
          'startRowIndex': 0,
          'endRowIndex': 2478,
          'startColumnIndex': 0,
          'endColumnIndex': 10
        },
        'sortSpecs': [
          {
            'dimensionIndex': 6,
            'sortOrder': "ASCENDING"
          }
        ]
      }
    }
  ]
}

request7 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN7).execute()
print(request7)


RUN8 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 188,
            'startColumnIndex': 6,
            'endColumnIndex': 10,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 188,
            'startColumnIndex': 7,
            'endColumnIndex': 11,
        },
        "pasteType": "Paste_Values",

    }},

]}

request8 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN8).execute()
print(request8)


request9 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range="PWPZ!G1:G188").execute()
print(request9)


request10 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range="PWPZ!K1:K188").execute()
print(request10)


RUN10 = {'requests': [
    {
      'sortRange': {
        'range': {
          'sheetId': sheet_id1,
          'startRowIndex': 0,
          'endRowIndex': 2478,
          'startColumnIndex': 0,
          'endColumnIndex': 10
        },
        'sortSpecs': [
          {
            'dimensionIndex': 4,
            'sortOrder': "ASCENDING"
          }
        ]
      }
    }
  ]
}

request10 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN10).execute()
print(request10)


request11 = sheet.values().clear(spreadsheetId=spreadsheet_id1,
                                range="PWP!A2:L2479").execute()
print(request11)


RUN12 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 2478,
            'startColumnIndex': 0,
            'endColumnIndex': 10,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 1,
            'endRowIndex': 2479,
            'startColumnIndex': 0,
            'endColumnIndex': 10,
        },
        "pasteType": "Paste_Values",

    }},

]}

request12 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN12).execute()
print(request12, "(All Operations - Successfully!)")

# python3 /home/luke_blue/Startup_Files/import_csv_data_from_url_vaccination.py