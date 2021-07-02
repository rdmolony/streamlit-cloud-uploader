from pathlib import Path

import streamlit as st

from .gdrive import download_file_from_google_drive


def cloud_uploader(filepath: Path) -> None:
    storage_source = st.selectbox(
        "Where is your data stored?", options=["Google Drive"]
    )
    url = st.text_input("Enter a link to your data:")
    download_data = st.button("Fetch data?")
    if url is not "" and download_data is True:
        download_file_from_google_drive(input_url=url, filepath=filepath)
