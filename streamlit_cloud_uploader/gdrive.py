"""Download file from inputted URL.

Google Drive downloader was adapted from https://github.com/thoppe/streamlit-skyAR
"""

from pathlib import Path

import requests
from requests import Response
from stqdm import stqdm
import streamlit as st


def _extract_id_from_google_drive_link(url: str) -> str:
    """Extract ID from URL

    Or '1mzxpZS_nKx8pOLNLDO2SXzboVTE4rlV-' from
    https://drive.google.com/file/d/1mzxpZS_nKx8pOLNLDO2SXzboVTE4rlV-/view?usp=sharing

    Args:
        url (str): Google Drive link

    Returns:
        str: Google Drive File ID
    """
    split_url = url.split("/")
    index_of_d = split_url.index("d")
    return split_url[index_of_d + 1]


def _get_confirm_token(response: Response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value
    return None


def _save_response_content(response: Response, filepath: Path):
    chunk_size = 32768
    with open(filepath, "wb") as f:
        for chunk in stqdm(response.iter_content(chunk_size)):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def download_file_from_google_drive(url: str, filepath: Path):
    base_url = "https://docs.google.com/uc?export=download"
    id = _extract_id_from_google_drive_link(url)
    session = requests.Session()
    response = session.get(base_url, params={"id": id}, stream=True)
    token = _get_confirm_token(response)
    if token:
        params = {"id": id, "confirm": token}
        response = session.get(base_url, params=params, stream=True)
    _save_response_content(response, filepath)
