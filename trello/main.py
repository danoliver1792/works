import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from requests.exceptions import RequestException
from time import sleep

# Trello Key and token, Trello Card ID, Google Sheets ID and sheet name
API_KEY = ""
TOKEN = ""
CARD_ID = ""
SPREADSHEET_ID = ""
WORKSHEET_NAME = ""


def authenticate_google_sheets():
    """
    Google Sheets Authentication using credentials
    """
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\danrl\OneDrive\GitHub\Trello"
                                                                   r"\credentials.json", scope)
    client = gspread.authorize(credentials)
    return client


def main():
    """
    Google Sheets Authentication and URL construction to get card checklists
    """
    try:
        google_sheets_client = authenticate_google_sheets()
        spreadsheet = google_sheets_client.open_by_key(SPREADSHEET_ID)
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

        while True:
            try:
                url = f"https://api.trello.com/1/cards/{CARD_ID}/checklists"
                params = {
                    "key": API_KEY,
                    "token": TOKEN,
                }

                # Clearing data from range E1:F11
                worksheet.batch_clear(['E1:F11'])

                # Enter the data in the range E1:F11
                response = requests.get(url, params=params)
                response.raise_for_status()
                checklists = response.json()

                # Scrolling through the list and updating the worksheet
                for checklist in checklists:
                    for item_index, item in enumerate(checklist['checkItems'], start=1):
                        item_name = item['name']
                        item_state = item.get('state', '')

                        row_number = item_index

                        update_range = f'E{row_number}:F{row_number}'
                        values = [[item_name, item_state]]

                        cell_list = worksheet.range(update_range)
                        for cell, value in zip(cell_list, values[0]):
                            cell.value = value
                        worksheet.update_cells(cell_list)

                sleep(60)
            except RequestException as req_exc:
                print(f'Error HTTP: {req_exc}')
                sleep(60)

    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
