import os
import shutil
import zipfile
import PySimpleGUI as sg

class BrowserRestoreApp:
    def __init__(self):
        self.layout = [
            [sg.Text("Browser Restore App")],
            [sg.Radio("Firefox", group_id="browser", default=True, key="-FIREFOX-"), sg.Radio("Edge", group_id="browser", key="-EDGE-")],
            [sg.Text("Backup File: "), sg.Input(key="-FILE-"), sg.FileBrowse(file_types=(("Zip Files", "*.zip"),))],
            [sg.ProgressBar(1000, orientation='h', size=(20, 20), key="-PROGRESS-")],
            [sg.Button("Restore"), sg.Button("Exit")]
        ]

        self.window = sg.Window("Browser Restore App", self.layout)

    def restore_browser(self, browser_name, backup_file, backup_folder, progress_bar):
        try:
            with zipfile.ZipFile(backup_file, 'r') as zip_file:
                zip_file.extractall(f'{backup_folder}/{browser_name}')

            shutil.move(f'{backup_folder}/{browser_name}/Profile', backup_folder)

            progress_bar.UpdateBar(100)

        except FileNotFoundError:
            sg.PopupError(f"Backup file of {browser_name} not found.")

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break

            if event == "Restore":
                backup_file = values["-FILE-"]
                progress_bar = self.window["-PROGRESS-"]
                progress_bar.UpdateBar(0)

                if values["-FIREFOX-"]:
                    browser_name = "Firefox"
                else:
                    browser_name = "Edge"

                if backup_file == "":
                    sg.PopupError("Please select a backup file.")
                else:
                    try:
                        self.restore_browser(browser_name, backup_file, os.path.dirname(backup_file), progress_bar)
                        sg.Popup("Restore completed.")
                    except Exception as e:
                        sg.PopupError(f"Error: {str(e)}")

        self.window.close()


if __name__ == '__main__':
    app = BrowserRestoreApp()
    app.run()
