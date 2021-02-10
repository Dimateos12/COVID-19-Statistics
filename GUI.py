import PySimpleGUI as sg
import data

sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('COVID 19 Statistics'), ],
            [sg.Text('Enter the country '), sg.InputText(), ],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('COVID 19', layout, margins=(200, 100))
text = window.read()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    sg.popup(str(data.wypisz(values[0])),title='WYNIK')

window.close()