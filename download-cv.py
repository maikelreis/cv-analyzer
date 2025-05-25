from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials

scopes = ["https://www.googleapis.com/auth/drive.readonly"] # setting the scope

creds = Credentials.from_authorized_user_file('token.json', scopes)

service = build('drive','v3', credentials=creds) # connection to API

folder_id = '1A3m7GXXXxGcwBURkbKCoVArld4ON4X0o' # Google drive folder id

results = service.files().list(
    q=f"'{folder_id}' in parents", fields='files(id,name)' #getting list of files ids and names
).execute()

files = results.get('files',[])

if not files:
    raise FileNotFoundError('No files found in result')
else:
    for file in files:
        requests = service.files().get_media(fileId=file['id']) # Getting Id for each file in files
        #test_only: requests = service.files().get_media(fileId='1cR6Xn2ZhdKvfnZDyXvCuLpFJVrj8rw4K')
        file_path = f"./curriculum/{file['name']}"
        #test_only: file_path = f"./curriculum/CV Maikel Reis EN_Magalu.pdf"
        with open(file_path,'wb') as file:
            downloader = MediaIoBaseDownload(file,requests)
            # Download file dinamically in chunks
            done = False
            while not done:
                status, done = downloader.next_chunk()

