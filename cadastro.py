from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('Reddit')

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Deseja salvar as informações?')],
    [sg.Button('Logar')]

]

# janela
janela = sg.Window('Tela de login', layout)


# ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Pedro' and valores['senha'] == '12345678':

            print('Seja muito bem vindo')


