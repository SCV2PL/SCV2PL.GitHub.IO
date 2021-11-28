from Google import Create_Service

CLIENT_SECRET_FILE = '/home/luke_blue/Startup_Files/sars-cov-2-poland.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

spreadsheet_id = '185RO55T68UARD2KY38pSeYOT9ZrnEGeOfiflTj4cxFQ'
sheet_id = '50471916'

request_body = {
    'requests': [
        {
            'cut_Paste': {
                'source': {
                    'sheet': sheet_id,
                    'startRowIndex': 2,
                    'endRowIndex': 383,
                    'startColumnIndex': 3,
                    'endColumnIndex': 4,
                },

                'destination': {
                    'sheet': sheet_id,
                    'startRowIndex': 2,
                    'columnIndex': 4
                },
                'pasteType': 'PASTE_VALUES'
            }

        }

    ]

}

response = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body=request_body
).execute()

# python3 /home/luke_blue/Startup_Files/copy_paste_avr7d10000_todaysum.py

# luke_blue@blox:~/Startup_Files$ python3 copy_paste_avr7d10000_todaysum.py
# /usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.7) or chardet (3.0.4) doesn't match a supported version!
#   warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
# /home/luke_blue/Startup_Files/sars-cov-2-poland.json-sheets-v4-(['https://www.googleapis.com/auth/spreadsheets'],)
# ['https://www.googleapis.com/auth/spreadsheets']
# Traceback (most recent call last):
#   File "copy_paste_avr7d10000_todaysum.py", line 8, in <module>
#     service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
#   File "/home/luke_blue/Startup_Files/Google.py", line 31, in Create_Service
#     flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
#   File "/usr/local/lib/python3.8/dist-packages/google_auth_oauthlib/flow.py", line 204, in from_client_secrets_file
#     return cls.from_client_config(client_config, scopes=scopes, **kwargs)
#   File "/usr/local/lib/python3.8/dist-packages/google_auth_oauthlib/flow.py", line 162, in from_client_config
#     raise ValueError("Client secrets must be for a web or installed app.")
# ValueError: Client secrets must be for a web or installed app.
# luke_blue@blox:~/Startup_Files$