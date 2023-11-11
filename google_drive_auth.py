import os.path
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
from mimetypes import guess_type
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

folder_ID = os.getenv("FOLDER_ID")

def uploadImage(image_path):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Now we upload/create the image in drive
    try:
        service = build("drive", "v3", credentials=creds)

        current_time = datetime.now()

        # Call the Drive v3 API
        file_metadata = {
            'name': current_time.strftime("%Y-%m-%d %H:%M:%S"),
            'parents': [folder_ID]
        }

        # Obtiene el tipo MIME del archivo
        mime_type = guess_type(image_path)[0]

        media = MediaFileUpload(image_path, mimetype=mime_type)
        file = service.files().create(body=file_metadata,
                                      media_body=media, fields='id').execute()

        print(f"Archivo subido con éxito, ID: {file.get('id')}")
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")
        file = None
    return file.get("id")


if __name__ == "__main__":
    uploadImage()
