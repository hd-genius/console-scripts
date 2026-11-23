#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup
import requests
from pathlib import Path
from _utils import select_drive, download_temp_file


reinstall_page_url = 'https://www.playstation.com/en-us/support/hardware/ps5/system-software/'
download_button_text = 'PS5 console reinstallation file'

def main():
    drive_mount_path = select_drive("FAT32 or exFAT")
    file_url = find_file_url()
    downloaded_file = download_temp_file(file_url, "PS5UPDATE.PUP")
    create_install_drive(drive_mount_path, downloaded_file)

def find_file_url():
    response = requests.get(reinstall_page_url)
    soup = BeautifulSoup(response.text, "html.parser")
    matching_anchors = soup.find_all("a", string=download_button_text)
    if len(matching_anchors) == 0:
        raise Exception("Could not find a link/button with the expected text for the download.")
    if len(matching_anchors) > 1:
        raise Exception("Multiple links/buttons with the expected text for the download was found. The correct option could not be determined.")
    else:
        return matching_anchors[0]['href']

def create_install_drive(drive: Path, update_file: Path):
    file_name = 'PS5UPDATE.PUP'
    destination_dir = Path(f'{drive}/PS5/UPDATE')
    destination_dir.mkdir(parents=True, exist_ok=True)
    target_path = destination_dir.joinpath(file_name)
    target_path.touch(exist_ok=True)
    update_file.copy(target_path)
    print('Installation drive successfully created.')

if __name__ == '__main__':
    main()