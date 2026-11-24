import os
from pathlib import Path
import shutil
from urllib.request import urlretrieve
from zipfile import ZipFile
from _utils import select_drive, download_temp_file

file_url = 'https://www.xbox.com/xboxone/osu1'

def main():
    drive_mount_path = select_drive("NTFS")
    prepare_drive(drive_mount_path)
    downloaded_file_path = download_temp_file(file_url, "OSU1.zip")
    extract_contents(downloaded_file_path, drive_mount_path)

def prepare_drive(mount_path):
    input('If you choose to proceed, all data on the selected drive will be deleted. Do you wish to continue?')
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

def extract_contents(source: Path, destination: Path):
    print('Extracting update contents...')
    with ZipFile(source) as zip_file:
        zip_file.extractall(destination)

if __name__ == '__main__':
    main()