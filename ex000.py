import os , PySimpleGUI as sg , pyautogui as pa, time, webbrowser as wb, platform
sg.theme('Black')

user = os.getlogin()
machine_name = platform.node()
plataforma = platform.system()
arch = platform.machine() 

layout = [  [sg.Text('Deixe Seu Pc Mais Rapido' , font = ('Arial', 30))],
            [sg.Text('Bem Vindo(a): '+user+'   |' , font = ('Arial', 12)) , sg.Text('Nome Da Maquina(a): '+machine_name , font = ('Arial', 12) )  ],
            [sg.Text(plataforma + '   | ', font = ('Arial', 13)), sg.Text(arch , font = ('Arial', 13)) ],
            [sg.Text('lipar dados inutil !' , size=(50,1), font=('Helvetica', 14)) ,  sg.Button('Fazer', key=('temp') , size = (100,1), font=('Helvetica', 14) , mouseover_colors=('white', 'green') , border_width=0 )],
            [sg.Text('Aumentar Nucleo !', size=(50,1), font=('Helvetica', 14)), sg.Button('Fazer', key=('nuc') ,size = (100,1), font=('Helvetica', 14), mouseover_colors=('white', 'green') , border_width=0,)],
            [sg.Text('Desativar Serviços', size=(50,1), font=('Helvetica', 14)), sg.Button('Fazer', key=('win') ,size = (100,1), font=('Helvetica', 14), mouseover_colors=('white', 'green') , border_width=0,)],
            [sg.Button('Fechar' , size=(100,1) , font=('Helvetica', 14), button_color = ('Red') ,  border_width=0  )] ]



window = sg.Window('Optimizer', layout, size = (800,500))


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Fechar': #
        break
    if event == 'temp':
        pa.alert("Não se mexa "+user+"! Click Em Continuar e dps ignorar tudo")
        pa.hotkey('win', 'r')
        time.sleep(0.5)
        pa.write('%temp%')
        time.sleep(0.5)
        pa.press('enter')
        time.sleep(0.5)
        pa.hotkey('ctrl', 'a')
        pa.press('delete')
    if event == 'nuc':
        pa.alert("inicialização do sistema depois em Opções Avançadas depois em numero de processadores ! ")
        pa.hotkey('win', 'r')
        time.sleep(0.5)
        pa.write('msconfig')
        time.sleep(0.5)
        pa.press('enter')
    if event == 'win':
        wb.open("file:///C:/Users/"+ machine_name +"/Desktop/ex000/optimizer/")


window.close()