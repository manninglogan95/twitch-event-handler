# limit 3 integrations on free account
# update specific cell in google sheets to trigger other event on ifttt

from googleapiclient import discovery
import time, requests

credentials = None

service = discovery.build('sheets', 'v4', credentials=credentials)

spreadsheet_id = '1LjshcGnHZEReAanstmb5BUwl903BARjeiawFpjUMUZM' 
value_input_option = 'RAW'

def turn_on():
    range_ = 'A1'

    values = [[time.time()]]
    body = {'values': values}
    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=body)
    response = request.execute()
    print(response)

    headers = {
        'authority': 'ifttt.com',
        'content-length': '0',
        'accept': '*/*',
        'x-csrf-token': 'QQ38hbP5aM30wH0OJEAsJyde7j73P6PyIQa6uxE9GVuqFwIq2Cct3x5OF7nu/5dFQMRiGfzZc07rw4Stzfexwg==',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.438',
        'content-type': 'application/json',
        'origin': 'https://ifttt.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ifttt.com/applets/hqecFmE4',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'browser_session_id=bqQ_UloMB3OtwEaZwW2yng; _anon_id=IjY3NDlmYmJmZDRhNjNiODlkNTUwYWU2MGIyNDNlMzQ2Ig^%^3D^%^3D--584e71693435fae9371afa6ceb4e36299b704330; timezone=America/Chicago; em_cdn_uid=t^%^3D1618877339689^%^26u^%^3Dde091ec465d7471baa0748df585dea62; remember_token=ffcbb160247469765f9bd3c64ef656cb420da01d; shared_user_id=12566210; show_flash=true; expiring_session_token=iMbDucdCA076JCHka3HYYw; user_channel_ids=6^%^2C1829340444^%^2C1240189002^%^2C4^%^2C1863687020^%^2C336690107^%^2C324969693^%^2C1172726678^%^2C1108205771^%^2C1089090894^%^2C3^%^2C941030000^%^2C799977804^%^2C709896750^%^2C142226432^%^2C51464135^%^2C1620619676^%^2C59109479^%^2C1004582012^%^2C1158179406^%^2C814768187; ifttt_user_id=e^%^3A12566210^%^3A1619059203^%^3AmLt2eQwOyqOC5x5ywHBKjlptwVUcc2MmHybjz41Hpos^%^3D; _ifttt_front_end_session=BAh7CUkiD3Nlc3Npb25faWQGOgZFVEkiJWQwMWI0ZWZhNTczNTNhMzhiYmRhZmUwMzRjZTkxMzk3BjsAVEkiDHVzZXJfaWQGOwBGaQPCvr9JIhJpZnR0dF91c2VyX2lkBjsARmkDwr6^%^2FSSIcYWN0aXZhdGlvbl9zdWNjZXNzX3BsYW4GOwBGewZsKwfRKlVSewg6CW1vZGVJIg13ZWJfdmlldwY7AFQ6DHN1Y2Nlc3N7CDoNcmVkaXJlY3RJIjdodHRwczovL2lmdHR0LmNvbS9idWxrX2NoYW5uZWxfYWN0aXZhdGlvbi9jb250aW51ZQY7AFQ6C2xheW91dEAOOgpmbGFzaEY6DGZhaWx1cmV7CDsISSI1aHR0cHM6Ly9pZnR0dC5jb20vYnVsa19jaGFubmVsX2FjdGl2YXRpb24vZmFpbGVkBjsAVDsJQA47CkY^%^3D--672fa9ee8dc518d2aa7619b18ec6ec172d83fe63; _applet_service_session=SXdUdVZtV0djOUhjcHcvb3JPM1gxaXNZYXkvVDJqT2lwUC9YZzUzWmIwamcwdEkzckx2S0dlcEVYYkZ1NU0rd29tQy85QUdYNUxhc2RoRGtYRHdmYjZXZG9qNjg2V3k3em5vcUlweENYQmI4ek1XZ1gvWS9nYmVqR2gvNitRVjFYMzhRS2FvL09ZRWpVVnY3MnNSbktUcjIwRFNIbGZqcFlaL3BzOXZXTXRPbXVCTDBSY0h3aWl1UjVXS3pPNmhXZE96YVJZUTFtRHNYMURPVWhSeVQyU2xZMWpucDVIQ1I4djd2aTZnVUJla2tyOXhRSmVwd0RLN0I3aXFzNjYwbWo0dkU3ZEFldllGalFNb1lTU2Fpd1ViMUxDeTh1eUNwTXh2WDhsa0p5S1UrK3lub3dqT1B4ZnRsLzZSR3ZydGx1UVRiVkx0dGc5RXVTWWo5c09jM3F1bHpCQ0tMQkxqMHJDU2laaVl1aGZvPS0tRHR4VlhkZlJhWFBwY2ovYVpMeEIyZz09--a6638f77d95710c873d432a82761e91c30ecd9e9',
    }

    response = requests.post('https://ifttt.com/applets/hqecFmE4/check', headers=headers)


def turn_off():
    range_ = 'A2'

    values = [[time.time()]]
    body = {'values': values}
    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=body)
    response = request.execute()
    print(response)

    headers = {
    'authority': 'ifttt.com',
    'content-length': '0',
    'accept': '*/*',
    'x-csrf-token': 'PZzEQxpDLLUjQ94dnSsKBTD4NRnyA9KSSFQIiLJKSAnWhjrscZ1pp8nNtKpXlLFnV2K5PvnlAi6CkTaeboDgkA==',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.438',
    'content-type': 'application/json',
    'origin': 'https://ifttt.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://ifttt.com/applets/A8Qapnye',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'browser_session_id=bqQ_UloMB3OtwEaZwW2yng; _anon_id=IjY3NDlmYmJmZDRhNjNiODlkNTUwYWU2MGIyNDNlMzQ2Ig^%^3D^%^3D--584e71693435fae9371afa6ceb4e36299b704330; timezone=America/Chicago; em_cdn_uid=t^%^3D1618877339689^%^26u^%^3Dde091ec465d7471baa0748df585dea62; remember_token=ffcbb160247469765f9bd3c64ef656cb420da01d; shared_user_id=12566210; show_flash=true; expiring_session_token=iMbDucdCA076JCHka3HYYw; user_channel_ids=6^%^2C1829340444^%^2C1240189002^%^2C4^%^2C1863687020^%^2C336690107^%^2C324969693^%^2C1172726678^%^2C1108205771^%^2C1089090894^%^2C3^%^2C941030000^%^2C799977804^%^2C709896750^%^2C142226432^%^2C51464135^%^2C1620619676^%^2C59109479^%^2C1004582012^%^2C1158179406^%^2C814768187; ifttt_user_id=e^%^3A12566210^%^3A1619059203^%^3AmLt2eQwOyqOC5x5ywHBKjlptwVUcc2MmHybjz41Hpos^%^3D; _ifttt_front_end_session=BAh7CUkiD3Nlc3Npb25faWQGOgZFVEkiJWQwMWI0ZWZhNTczNTNhMzhiYmRhZmUwMzRjZTkxMzk3BjsAVEkiDHVzZXJfaWQGOwBGaQPCvr9JIhJpZnR0dF91c2VyX2lkBjsARmkDwr6^%^2FSSIcYWN0aXZhdGlvbl9zdWNjZXNzX3BsYW4GOwBGewZsKwfRKlVSewg6CW1vZGVJIg13ZWJfdmlldwY7AFQ6DHN1Y2Nlc3N7CDoNcmVkaXJlY3RJIjdodHRwczovL2lmdHR0LmNvbS9idWxrX2NoYW5uZWxfYWN0aXZhdGlvbi9jb250aW51ZQY7AFQ6C2xheW91dEAOOgpmbGFzaEY6DGZhaWx1cmV7CDsISSI1aHR0cHM6Ly9pZnR0dC5jb20vYnVsa19jaGFubmVsX2FjdGl2YXRpb24vZmFpbGVkBjsAVDsJQA47CkY^%^3D--672fa9ee8dc518d2aa7619b18ec6ec172d83fe63; _applet_service_session=SnVORDg5TWluMVpqeUNEZnFpdjlZWlNBVWJ0dGk1U01NQU9IbXpFR1NLS3ZyVnRmM0tqZGcyODB1YjZQVjhJRDlNSFB6NGdjQWxoVm5NK2tUV0t1L0E4bHBvSC9BSnZjQlhRNFZMWkdZdHRSYVd6Vm1rUVl2TVcyVnY5dGtYTVBqNTJra3I4YWltU014b3RwcGxoMXNIMUdHcGFpeXZBSExWNCtxbm4zU3VEQVl0WDRVNU5GVzQ5TzZuM0tXUG5TNWt2cjh0dVV2UmJoUWVvaVd5UzU3MDBtdm03MG1LelFsZ0F5LzZ5OGd6UWFwNjFvZ0x1QU9MMzlZMU5QQkZOS2FzTUc2cTZqNXdSQUk4Yks2cXF1OXBCaHk4MXN3aVBhbE5ua3BDTlFhWWVxdG52YmE2U1IyTGdFK0pOYkNMTThhdEpMNFdKQ1FONUJJTzF1c2d6NGZLa05DcnRSaXI3SDVEbTBLczgvRFRzPS0tSE5IR3VQeW1meThSUjhxNDExRE9tdz09--6f8c516620e9130479ece1c9d3237399c23f45dc',
    }

    response = requests.post('https://ifttt.com/applets/A8Qapnye/check', headers=headers)




turn_off()