from pathlib import Path
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup


def find_link_url(page_url: str, button_text: str) -> str:
    """Find the URL of the link with the given text."""
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")
    matching_anchors = soup.find_all("a", string=button_text)
    if len(matching_anchors) == 0:
        raise Exception("Could not find a link with the expected text.")
    if len(matching_anchors) > 1:
        raise Exception("Multiple links with the expected text were found. The correct option could not be determined.")
    else:
        return matching_anchors[0]['href']

def select_drive(expected_fs: str) -> Path:
    print(f'Make sure that the target drive is formatted as {expected_fs} and mounted.')
    input('Once the target drive is properly formatted and mounted press ENTER.')
    while (True):
        selected_path = Path(input('Enter the target drive\'s mount point: '))
        if not selected_path.exists():
            print('The selected path does not exist.')
            continue
        if not selected_path.is_dir():
            print('The selected path is not directory.')
            continue
        if not selected_path.is_mount():
            print('The selected path is not a mount point. You must select the root directory of the drive.')
            continue
        return selected_path

def download_temp_file(url: str, name: str) -> Path:
    # TODO: check if the file is downloaded and offer to use the current file if so
    print(f'Downloading {name} file...')
    downloaded_file, http_message = urlretrieve(url)
    print(f'Downloaded file is saved at {downloaded_file}.')
    # TODO: add fallback file hosts in case the url changes or stops hosting
    return Path(downloaded_file)

def copy_file(source: Path, target: Path):
    """Safely copy a file and ensure all dependent directories exist."""
    # ensure that the target dir exists
    target.parent.mkdir(parents=True, exist_ok=True)
    source.copy(target)
    print(f'{source} successfully copied to {target}.')
