#!/usr/bin/env python3

from pathlib import Path
from _utils import select_drive, download_temp_file, find_link_url, copy_file


reinstall_page_url = 'https://www.playstation.com/en-us/support/hardware/ps5/system-software/'
download_button_text = 'PS5 console reinstallation file'

def main():
    drive_mount_path = select_drive("FAT32 or exFAT")
    file_url = find_link_url(reinstall_page_url, download_button_text)
    downloaded_file = download_temp_file(file_url, "PS5UPDATE.PUP")
    copy_file(downloaded_file, Path(f'{drive_mount_path}/PS5/UPDATE/PS5UPDATE.PUP'))
    print('Installation drive successfully created.')

if __name__ == '__main__':
    main()