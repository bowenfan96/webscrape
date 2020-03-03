from pywebcopy import save_webpage
import schedule
import PySimpleGUI as sg
import time


def download(url, folder):
    folder = folder + '\\' + time.strftime('%H%M')
    save_webpage(url=url, project_folder=folder)


layout = [[sg.Text('Webpage URL:', size=(15, 1)), sg.Input(size=(30, 1), key='url')],
          [sg.Text('Save Directory', size=(15, 1)), sg.Input(size=(30, 1), key='directory'), sg.FolderBrowse()],
          [sg.Text('Run Frequency (min)', size=(15, 1)), sg.Input(size=(10, 1), key='frequency'), sg.Button('Run')]
          ]

window = sg.Window('Webpage Downloader', layout)

while True:
    event, values = window.Read()

    if event is 'Run':
        download(values['url'], values['directory'])
        schedule.every(int(values['frequency'])).minutes.do(download, values['url'], values['directory'])

        while True:
            schedule.run_pending()
            time.sleep(1)

    if event is None:
        break
