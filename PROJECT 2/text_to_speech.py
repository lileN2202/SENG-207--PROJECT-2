# NAME: DELORES NKRUMAH
# ID:10956674
# DEPARTMENT: BMEN


import PySimpleGUI as sg
import pyttsx3
 
engine = pyttsx3.init()
voices= engine.getProperty('voices')
volume= engine.getProperty('volume')

layout=[
    [sg.Input('  ',key='-TEXT-',),
     sg.Button('Speaker',key='-submit-',button_color='purple',mouseover_colors='red',)],
    [sg.Text('Select Voice Type:',background_color='lightgreen',text_color='black'),
     sg.Radio('Male',group_id='voice',key='Male_voice',background_color='lightgreen',default=True,circle_color='orange',text_color='black'),
     sg.Radio('Female',group_id='voice',key='Female_voice',background_color='lightgreen', circle_color='orange',text_color='black')],
    [sg.Text('Select Volume:',background_color='lightgreen',text_color='black',k='-volume-',),
     sg.Radio('Low',group_id='volume',background_color='lightgreen',circle_color='orange',text_color='black',key='low'),
     sg.Radio('Medium',group_id='volume',background_color='lightgreen',default=True,circle_color='orange',text_color='black',key='medium'),
     sg.Radio('High',group_id='volume',background_color='lightgreen',circle_color='orange',text_color='black',key='high')]
]


window = sg.Window('TEXT TO SPEECH APP',layout,background_color='lightgreen')


while True:
    event,values = window.read()
    if event==sg.WIN_CLOSED:
        break

    
    if event=='-submit-' :
        text = values['-TEXT-']
        
        
        if values['low']:
            engine.setProperty('volume',0.1)

        elif values['medium']:
            engine.setProperty('volume',0.5)  


        else:
            engine.setProperty('volume',1.0)
        


        if values['Male_voice']:
            engine.setProperty('voice',voices[0].id)
        
        elif values['Female_voice']:
            engine.setProperty('voice',voices[1].id)

        
        engine.say(text)
        engine.runAndWait()

window.close()

 