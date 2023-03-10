#! /usr/bin/env python3
"""
Upload list of files to GoogleDrive subfolder. Delete all previously-loaded
files if they are in the current list of files to upload.

The purpose of this script is to ensure that the files to be uploaded
are the only files to be present on the GoogleDrive, but not delete all the
files on GoogleDrive because there could be hundreds. This is intended as a
one-way synchronization only.

TODO
- Create list of files on GoogleDrive (list A)
- Compare to list of files to be uploaded (list B)
- Compare A and B, delete files that are in A but not in B
- Do the above before deleting and uploading files as shown in the code below
"""

import datetime as dt

from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
import datasense as ds


def main():
    files_to_upload = [
        "instructions.txt", "diffs.txt", "cbc.svg"
    ]
    output_url = "quickstart.html"
    gdrive_folder = "python_test"
    header_title = "quickstart"
    header_id = "quickstart"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    # Create local webserver and auto-handle authentication
    gauth = GoogleAuth()
    # Authenticate the first time. Wait about an hour. Comment out when
    # successful.
    # gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    # List folders
    # This is almost correct.
    # It lists all folders, subfolders, etc., rather than just root folders
    folders = drive.ListFile(
        {
            "q":
            "mimeType='application/vnd.google-apps.folder' and trashed=false"
        }
    ).GetList()
    folder_titles = sorted([folder["title"] for folder in folders])
    if gdrive_folder not in folder_titles:
        print(f"{gdrive_folder} is not a folder on my Google Drive")
        print()
        ds.exit_script(
            original_stdout=original_stdout,
            output_url=output_url
        )
    for folder in folders:
        if (folder["title"] == gdrive_folder):
            folder_id = folder["id"]
            gdrive_files = drive.ListFile(
                {"q": f"'{folder_id}' in parents and trashed=False"}
            ).GetList()
            print(gdrive_files)
            if gdrive_files:
                gdrive_titles = [f["title"] for f in gdrive_files]
                print(gdrive_titles)
                file_modified_date = [f["modifiedDate"] for f in gdrive_files]
                print(file_modified_date)
                for file in gdrive_files:
                    pass
                    for f in files_to_upload:
                        if file["title"] == f:
                            file.Delete()
            for f in files_to_upload:
                file_upload = drive.CreateFile()
                file_upload = drive.CreateFile(
                    {"parents": [{"id": folder_id}]}
                )
                file_upload.SetContentFile(f)
                file_upload.Upload()
            print("Script completed")
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == "__main__":
    main()
