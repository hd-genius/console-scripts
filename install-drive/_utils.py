from pathlib import Path
from urllib.request import urlretrieve


def select_drive(expected_fs) -> Path:
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


def download_temp_file(url, name) -> Path:
    # TODO: check if the file is downloaded and offer to use the current file if so
    print(f'Downloading {name} file...')
    downloaded_file, http_message = urlretrieve(url)
    print(f'Downloaded file is saved at {downloaded_file}.')
    # TODO: add fallback file hosts in case the url changes or stops hosting
    return Path(downloaded_file)