from pathlib import Path

import streamlit as st

from streamlit_cloud_uploader.gdrive import download_file_from_google_drive


def cloud_uploader(filepath: Path) -> None:
    storage_source = st.selectbox(
        "Where is your data stored?", options=["Google Drive"]
    )
    url = st.text_input("Enter a link to your data:")
    download_data = st.button("Fetch data?")
    if url is not "" and download_data is True:
        download_file_from_google_drive(url=url, filepath=filepath)


if __name__ == "__main__":
    cloud_uploader(Path.cwd())
