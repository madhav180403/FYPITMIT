from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os

cnt=4482

files = os.listdir("Articles/")

files.sort()


CLIENT_SECRET_FILE = r'Other_files\client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_ids = ['1HFC4GGUVQatcEWLxcOYchmhGzWNukv2R', '1V4gOBla8aJf-e1BKKRGYACflbSB6bHuV','1BnNVRxjE-M-lH1hNDuI9vtj3IONwvdhL','1DafBWoPqLt7Nf3tCtzERcffLA_7CmVgS']

for i in range(5000, len(files)+1):

    print(cnt)

    file_name = 'Articles\\' + files[i]

    for id in folder_ids:
        file_metadata = {
            'name': file_name,
            'parents': [id]
        }

        media_content = MediaFileUpload(file_name, mimetype='text/plain')

        file = service.files().create(
            body=file_metadata,

            media_body=media_content
        ).execute()

    cnt+=1
