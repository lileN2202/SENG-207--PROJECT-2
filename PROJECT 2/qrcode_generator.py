# NAME: DELORES NKRUMAH
# ID:10956674
# DEPARTMENT: BMEN


import qrcode
import PySimpleGUI as sg
 

qrc_image=[sg.Image('',key='-QRCODE-',size=(350,350),background_color='gray')]

layout=[
    [sg.Input('',key='-URL-',justification='center',size=(53))],
    [sg.Button('Create', key='-submit-',expand_x= True,button_color='blue')],
    [sg.Column([qrc_image], justification= 'center')],
]


wind = sg.Window('QRCode Generator APP',layout)

while True:
    event,values = wind.read()
    if event==sg.WIN_CLOSED:
        break
    
    if event=='-submit-':
        url= values['-URL-']
        if url:
            image= qrcode.make(url)
            image.save('qr.png')
            wind['-QRCODE-'].update('qr.png')
wind.close()