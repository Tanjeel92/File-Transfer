import PySimpleGUI as sg

layout = [[sg.Text('Source: '), sg.Input(), sg.FolderBrowse()],[sg.Text('Destination: '), sg.Input(), sg.FolderBrowse()],[sg.Button('Sort')]]

window = sg.Window('Title', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if values[0] == '':
        print("Source path can't be empty")
        continue
    if values[1] == '':
        print("Destination path can't be empty")
        continue
    elif event == "Sort":
        source = values[0]
        destination = values[1]
        break
