from pathlib import Path

from streamlit_cloud_uploader import gdrive


def test_extract_id_from_google_drive_link():
    input_url = "https://drive.google.com/file/d/1mzxpZS_nKx8pOLNLDO2SXzboVTE4rlV-/view?usp=sharing"
    expected_output = "1mzxpZS_nKx8pOLNLDO2SXzboVTE4rlV-"
    output = gdrive._extract_id_from_google_drive_link(url=input_url)
    assert output == expected_output


def test_download_file_from_google_drive(tmp_path: Path):
    filepath = tmp_path / "small-file.csv"
    gdrive.download_file_from_google_drive(
        url="https://drive.google.com/file/d/14rV7E90MgXUd9pxhdas7TyYsDXbPmP2-/view?usp=sharing",
        filepath=filepath,
    )
    assert filepath.exists()
