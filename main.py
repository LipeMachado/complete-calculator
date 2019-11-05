# -*- coding: utf-8 -*-
import os
from time import sleep

print('-=-'*10)
sleep(0.2)
print('Calculadora feita por:')
print('@killalone  <-- Telegram')
print('@coursesprogrammerandhacker  <-- Canal/Telegram')
print('Se inscreva no canal. ^-^')
print('Qualquer bug ou dúvida pergunte.')
sleep(0.2)

rodando = 'rodando'

while rodando != 'termino':
    
    Object = lambda : print('-=-'*10)

    Object()
    print('!!Bem-Vindo!!')
    print('1 - Algebra - Matemática Básica')
    print('2 - Geometria Plana')
    print('3 - Trigonometria')
    print('0 - Sair')
    Object()
    try:
        user = int(input('Escolha: '))
    except:
        Object()
        print('O que você digitou???')
        print('Digite corretamente, por favor.')

    if user == 1:
        os.system("cls || clear")
        import algebra
    elif user == 2:
        os.system("cls || clear")
        import geometria_plana
    elif user == 3:
        os.system("cls || clear")
        import trigonometria
    elif user == 0:
        sleep(0.5)
        print('Saindo..... BYE, BYE')
        sleep(0.55)
        os.system("cls || clear")
        rodando = 'término'
    else:
        Object()
        print('Ops.. Tente novamente!')