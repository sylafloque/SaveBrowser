# SaveBrowser
Browser Backup App
Browser Backup App

A simple GUI application for backing up and restoring browser profiles for Firefox and Edge browsers on Windows operating system. The application creates a zip file of the browser profile folder for backup and extracts the backup file to the browser profile folder for restore.
Getting Started

To use this application, follow these steps:

    Clone the repository to your local machine.
    Install the required libraries using pip install -r requirements.txt.
    Run the browser_backup.py script to start the application.
    Select the browsers to backup/restore, the export folder for the backup files, and click on the Backup/Restore button to perform the operation.

Prerequisites

    Python 3.x
    PySimpleGUI
    zipfile
    shutil

Usage

When you run the browser_backup.py script, the GUI window will appear. You can select the browsers to backup/restore by checking the checkboxes for Firefox and/or Edge. You can also select the export folder for the backup files by clicking on the "..." button next to the input field.

To perform a backup, click on the Backup button. The application will create a new folder with the browser name in the export folder, copy the browser profile folder to the new folder, create a zip file of the new folder, and delete the new folder.

To perform a restore, click on the Restore button. The application will prompt you to select the backup file to restore. Once you select the backup file, the application will extract the backup file to the browser profile folder.
Contributing

Contributions to this project are welcome. You can contribute by:

    Adding support for other browsers and platforms.
    Adding additional features to the application.
    Fixing bugs and issues.

License

This project is licensed under the MIT License - see the LICENSE file for details.
