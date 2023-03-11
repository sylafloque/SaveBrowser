import os
import shutil
import zipfile
import PySimpleGUI as sg

class BrowserBackupApp:
    def __init__(self):
        self.layout = [
            [sg.Text("Browser Backup App")],
            [sg.Checkbox("Firefox", default=True, key="-FIREFOX-"), sg.Checkbox("Edge", default=True, key="-EDGE-")],
            [sg.Text("Export Directory: "), sg.Input(default_text=os.getcwd(), key="-FOLDER-"), sg.FolderBrowse()],
            [sg.ProgressBar(1000, orientation='h', size=(20, 20), key="-PROGRESS-")],
            [sg.Button("Backup"), sg.Button("Restore"), sg.Button("Exit")]
        ]

        self.window = sg.Window("Browser Backup App", self.layout)

    def backup_browser(self, browser_name, browser_path, export_folder, progress_bar):
        try:
            os.makedirs(f'{export_folder}/{browser_name}')
        except FileExistsError:
            pass

        try:
            shutil.copytree(browser_path, f'{export_folder}/{browser_name}/Profile')

            files_to_archive = []
            for root, dirs, files in os.walk(f'{export_folder}/{browser_name}'):
                for file in files:
                    files_to_archive.append(os.path.join(root, file))

            with zipfile.ZipFile(f'{export_folder}/{browser_name}.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
                for i, file in enumerate(files_to_archive):
                    zip_file.write(file, os.path.basename(file))
                    progress_bar.UpdateBar(i+1, max=len(files_to_archive))

            shutil.rmtree(f'{export_folder}/{browser_name}')

        except FileNotFoundError:
            sg.PopupError(f"Profile folder of {browser_name} not found.")

    def restore_browser(self, browser_name, browser_path, backup_file, progress_bar):
        try:
            with zipfile.ZipFile(backup_file, 'r') as zip_file:
                zip_file.extractall(f'{browser_path}/Profile')
                files_to_restore = zip_file.namelist()
                progress_bar.UpdateBar(0, max=len(files_to_restore))
                for i, file in enumerate(files_to_restore):
                    zip_file.extract(file, f'{browser_path}/Profile')
                    progress_bar.UpdateBar(i+1)
        except FileNotFoundError:
            sg.PopupError(f"Backup file not found.")

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break

            if event == "Backup":
                export_folder = values["-FOLDER-"]
                progress_bar = self.window["-PROGRESS-"]
                progress_bar.UpdateBar(0)

                if values["-FIREFOX-"]:
                    self.backup_browser('Firefox', os.path.expanduser('~') + '/AppData/Roaming/Mozilla/Firefox/Profiles/', export_folder, progress_bar)

                if values["-EDGE-"]:
                    self.backup_browser('Edge', os.path.expanduser('~') + '/AppData/Local/Microsoft/Edge/User Data/Default/', export_folder, progress_bar)

                sg.Popup("Backup completed.")

            if event == "Restore":
                backup_file = sg.popup_get_file("Select backup file")
                progress_bar = self.window["-PROGRESS-"]
                progress_bar.UpdateBar(0)

                if values["-FIREFOX-"]:
                    self.restore_browser('Firefox', os.path.expanduser('~') + '/AppData/Roaming/Mozilla/Firefox/Profiles/', backup_file, progress_bar)

                if values["-EDGE-"]:
                    self.restore_browser('Edge', os.path.expanduser('~') + '/AppData/Local/Microsoft/Edge/User Data/Default/', backup_file, progress_bar)

                sg.Popup("Restore completed.")

        self.window.close()

if __name__ == '__main__':
    app = BrowserBackupApp()
    app.run()
