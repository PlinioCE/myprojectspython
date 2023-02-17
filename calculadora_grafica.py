from PySimpleGUI import PySimpleGUI as cc

# LAYOUT
cc.theme('Reddit')
layout = [
    [cc.Input(key='tela', size=(33, 1), justification='r')],
    [cc.Button('7', size=(4, 2)), cc.Button('8', size=(4, 2)), cc.Button('9', size=(4, 2)), cc.Button('%', size=(4, 2)), cc.Button('C/CE', size=(4, 2))],
    [cc.Button('4', size=(4, 2)), cc.Button('5', size=(4, 2)), cc.Button('6', size=(4, 2)), cc.Button('x', size=(4, 2)), cc.Button('/', size=(4, 2))],
    [cc.Button('1', size=(4, 2)), cc.Button('2', size=(4, 2)), cc.Button('3', size=(4, 2)), cc.Button('+', size=(4, 2)), cc.Button('-', size=(4, 2))],
    [cc.Button('0', size=(10, 2)), cc.Button(',', size=(4, 2)), cc.Button('=', size=(10, 2))]  # ,
    # [cc.ReadFormButton('TESTE')]
]

# JANELA
janela = cc.Window('CALCULADORA', layout)

# EVENTOS E VALORES
while True:
    eventos, valores = janela.read()
    if eventos == cc.WIN_CLOSED:
        break

