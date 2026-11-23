import os
from pathlib import Path
import shutil
from urllib.request import urlretrieve
from zipfile import ZipFile

file_url = 'https://www.xbox.com/xboxone/osu1'

def main():
    drive_mount_path = select_installation_drive()
    prepare_drive(drive_mount_path)
    downloaded_file_path = download_update_file()
    extract_contents(downloaded_file_path, drive_mount_path)

def select_installation_drive():
    print('Make sure that the target drive is formatted as NTFS and mounted.')
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

def prepare_drive(mount_path):
    print('Emptying drive contents...')
    for item in os.listdir(mount_path):
        file_path = os.path.join(mount_path, item)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print('Drive successfully emptied.')

def download_update_file():
    # TODO: check if the file is downloaded and offer to use the current file if so
    print('Downloading OSU.zip file...')
    downloaded_file, http_message = urlretrieve(file_url)
    print(f'Downloaded file is saved at {downloaded_file}.')
    # TODO: add fallback file hosts in case microsoft changes the url or stops hosting
    return downloaded_file

def extract_contents(source, destination):
    print('Extracting update contents...')
    with ZipFile(source) as zip_file:
        zip_file.extractall(destination)

if __name__ == '__main__':
    main()