from streamlit_cloud_uploader import gdrive


def test_extract_id_from_google_drive_link():
    input_url = "https://drive.google.com/file/d/1mzxpZS_nKx8pOLNLDO2SXzboVTE4rlV-/view?usp=sharing"
    expected_output = "1mzxpZS_nKx8pOLNLDO2SXzboVTE4rlV-"
    output = gdrive._extract_id_from_google_drive_link(url=input_url)
    assert output == expected_output
