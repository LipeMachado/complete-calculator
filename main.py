# -*- coding: utf-8 -*-
import os
from time import sleep

print('-=-'*10)
sleep(0.2)
print('Calculadora feita por:')
sleep(0.3)
print('@killalone  <-- Telegram')
sleep(0.3)
print('@coursesprogrammerandhacker  <-- Canal/Telegram')
sleep(0.3)
print('Se inscreva no canal. ^-^')
sleep(0.3)
print('Qualquer bug ou dúvida pergunte.')
sleep(0.3)

rodando = 'rodando'

while rodando != 'termino':
    try:
        def Object():
            print('-=-'*10)
            sleep(0.5)

        Object()
        print('!!Bem-Vindo!!')
        print('1 - Algebra - Matemática Básica')
        print('2 - Geometria Plana')
        print('0 - Sair')
        Object()
        user = int(input('Escolha: '))

        if user == 1:
            os.system("cls")
            import algebra
        elif user == 2:
            os.system("cls")
            import geometria_plana
        elif user == 0:
            sleep(0.5)
            print('Saindo..... BYE, BYE')
            sleep(0.55)
            rodando = 'termino'
        else:
            Object()
            print('Ops.. Tente novamente!')
    except:
        Object()
        print('O que você digitou???')
        print('Digite corretamente, por favor.')
