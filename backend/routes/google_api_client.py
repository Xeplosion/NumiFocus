import os
import io
import logging
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import gspread

# Configure module-specific logger.
logger = logging.getLogger("GoogleAPIClient")
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class GoogleAPIClient:
    """
    Encapsulates authentication and client generation for Google APIs.
    """
    def __init__(self):
        self.logger = logger
        self.scopes = [s.strip() for s in os.environ.get("SCOPES", "").split(",") if s.strip()]
        self.token_path = os.environ.get("TOKEN")
        self.credentials_path = os.environ.get("CREDENTIALS")
        self.creds = self._get_credentials()

        self.drive_service = self.get_drive_service()
        self.gspread_client = self.get_gspread_client()

    def _get_credentials(self):
        self.logger.info("[GoogleAPIClient] Loading credentials")
        creds = None
        if self.token_path and os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, self.scopes)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                self.logger.info("[GoogleAPIClient] Refreshing expired credentials")
                creds.refresh(Request())
            else:
                self.logger.info("[GoogleAPIClient] Starting OAuth flow for new credentials")
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.scopes)
                creds = flow.run_local_server(port=0)
                with open(self.token_path, "w") as token:
                    token.write(creds.to_json())

        self.logger.info("[GoogleAPIClient] Credentials are ready")
        return creds

    def get_drive_service(self):
        """Builds and returns the Google Drive service client."""
        try:
            service = build("drive", "v3", credentials=self.creds)
            self.logger.info("[GoogleAPIClient] Drive service client created")
            return service
        except HttpError as e:
            self.logger.error(f"[GoogleAPIClient] Failed to build Drive service: {e}")
            return None

    def get_gspread_client(self):
        """Authorizes and returns a gspread client for Google Sheets."""
        try:
            client = gspread.authorize(self.creds)
            self.logger.info("[GoogleAPIClient] gspread client created")
            return client
        except HttpError as e:
            self.logger.error(f"[GoogleAPIClient] Failed to authorize gspread client: {e}")
            return None

    def get_spreadsheet_from_key(self, sheet_key):
        """Retrieves a Google Spreadsheet using its key."""
        return self.gspread_client.open_by_key(sheet_key)

    def get_drive_file_metadata(self, file_id):
        """Retrieves metadata for a file on Google Drive."""
        if not self.drive_service:
            return None
        try:
            metadata = self.drive_service.files().get(fileId=file_id).execute()
            logger.info(f"[GoogleAPIClient] Retrieved metadata for file ID {file_id}")
            return metadata
        except HttpError as e:
            logger.error(f"[GoogleAPIClient] Error retrieving file metadata: {e}")
            return None

    def get_drive_file(self, file_id):
        """Retrieves data for a file on Google Drive."""
        request = self.drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO() # In-memory byte stream to hold file data.

        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            logger.info(f"[GoogleAPIClient] Downloading file ID {file_id} {int(status.progress() * 100)}%.")

        fh.seek(0)  # reset stream position to start

        file_content = fh.read().decode('utf-8')
        return file_content
