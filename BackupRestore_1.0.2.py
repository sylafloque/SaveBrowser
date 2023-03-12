import os
import shutil
import zipfile
import PySimpleGUI as sg

class BrowserBackupApp:
    def __init__(self):
        self.layout = [
            [sg.Text("Browser Backup App")],
            [sg.Radio("Firefox", "BROWSER", default=True, key="-FIREFOX-"), sg.Radio("Edge", "BROWSER", default=False, key="-EDGE-")],
            [sg.Text("Export Directory: "), sg.Input(default_text=os.getcwd(), key="-FOLDER-"), sg.FolderBrowse(initial_folder=os.getcwd())],
            [sg.ProgressBar(1000, orientation='h', size=(20, 20), key="-PROGRESS-", bar_color=("#E5C07B", "#0078D7"))],
            [sg.Button("Backup"), sg.Button("Restore"), sg.Button("Exit")]
        ]

        self.window = sg.Window("Browser Backup App", self.layout)

    def backup_browser(self, browser_name, browser_path, export_folder, progress_bar):
        try:
            os.makedirs(f'{export_folder}/{browser_name}')
        except FileExistsError:
            pass

        try:
            if browser_name == "Edge":
                shutil.copytree(browser_path, f'{export_folder}/{browser_name}/Default', ignore=shutil.ignore_patterns(''))
            elif browser_name == "Firefox":
                shutil.copytree(browser_path, f'{export_folder}/{browser_name}/Profiles', ignore=shutil.ignore_patterns(''))

            with zipfile.ZipFile(f'{export_folder}/{browser_name}.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
                files_to_archive = []
                for root, dirs, files in os.walk(f'{export_folder}/{browser_name}'):
                    for file in files:
                        files_to_archive.append(os.path.join(root, file))

                for i, file in enumerate(files_to_archive):
                    zip_file.write(file, os.path.relpath(file, f'{export_folder}/{browser_name}'))
                    progress_bar.UpdateBar(i+1, max=len(files_to_archive))

            shutil.rmtree(f'{export_folder}/{browser_name}')

            progress_bar.UpdateBar(1000)
        except FileNotFoundError:
            sg.PopupError(f"Profile folder of {browser_name} not found.")
        progress_bar.UpdateBar(0)

    def restore_browser(self, browser_name, browser_path, backup_file, progress_bar):
        try:
            with zipfile.ZipFile(backup_file, 'r') as zip_file:
                zip_file.extractall(f'{browser_path}')
                files_to_restore = zip_file.namelist()
                progress_bar.UpdateBar(0, max=len(files_to_restore))
                for i, file in enumerate(files_to_restore):
                    zip_file.extract(file, f'{browser_path}')
                    progress_bar.UpdateBar(i+1)
        except FileNotFoundError:
            sg.PopupError(f"Backup file not found.")

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break

            if event == "Backup":
                export_folder = sg.popup_get_folder("Select backup folder", no_window=True)
                progress_bar = self.window["-PROGRESS-"]
                progress_bar.UpdateBar(0)

                if values["-FIREFOX-"]:
                    self.backup_browser('Firefox', os.path.expanduser('~') + '/AppData/Roaming/Mozilla/Firefox/Profiles/', export_folder, progress_bar)

                if values["-EDGE-"]:
                    self.backup_browser('Edge', os.path.expanduser('~') + '/AppData/Local/Microsoft/Edge/User Data/Default/', export_folder, progress_bar)

                sg.Popup("Backup completed.")

            if event == "Restore":
                backup_file = sg.popup_get_file("Select backup file", no_window=True, file_types=(("Zip Files", "*.zip"),))
                progress_bar = self.window["-PROGRESS-"]
                progress_bar.UpdateBar(0)

                if values["-FIREFOX-"] and not values["-EDGE-"]:
                    self.restore_browser('Firefox', os.path.expanduser('~') + '/AppData/Roaming/Mozilla/Firefox/', backup_file, progress_bar)

                if values["-EDGE-"] and not values["-FIREFOX-"]:
                    self.restore_browser('Edge', os.path.expanduser('~') + '/AppData/Local/Microsoft/Edge/User Data/', backup_file, progress_bar)

                sg.Popup("Restore completed.")

        self.window.close()

if __name__ == '__main__':
    app = BrowserBackupApp()
    app.run()

