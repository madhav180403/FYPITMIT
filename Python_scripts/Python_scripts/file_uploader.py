from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os

files = os.listdir("Articles/")

files.sort() #Getting a sorted list of files in the directory

CLIENT_SECRET_FILE = r'Other_files\client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive'] 

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES) #Creating the service to add files to the Drive account

folder_ids = ['1HFC4GGUVQatcEWLxcOYchmhGzWNukv2R', '1V4gOBla8aJf-e1BKKRGYACflbSB6bHuV','1BnNVRxjE-M-lH1hNDuI9vtj3IONwvdhL','1DafBWoPqLt7Nf3tCtzERcffLA_7CmVgS'] #Passing the ID of each folder of the Drive account, first one being primary, others being secondary nodes

for i in range(len(files)+1):

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
        ).execute() #Adding each file of the directory to all the 4 nodes
