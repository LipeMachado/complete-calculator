# -*- coding: utf-8 -*-
from time import sleep
import os
from math import sin, cos, tan, hypot, pi

rodando = 'rodando'

while rodando != 'termino':

    Object = lambda : print('-=-'*10)

    linha = lambda : print('-'*15)

    def seno():
        Object()
        print('Digite o número para saber seu Seno:')
        try:
            numero = float(input(''))
        except ValueError:
            print('ValueError')
        linha()
        return print(f'{sin(numero)}')

    def cosseno():
        Object()
        print('Digite o nnúmero para saber seu Cosseno:')
        try:
            numero = float(input(''))
        except ValueError:
            print('ValueError')
        linha()
        return print(f'{cos(numero)}')

    def tangente():
        Object()
        print('Digite o número para saber sua Tangente:')
        try:
            numero = float(input(''))
        except ValueError:
            print('ValueError')
        linha()
        return print(f'{tan(numero)}')

    def hipotenusa():
        Object()
        print('Digite o número do cateto oposto:')
        try:
            cateto_oposto = float(input(''))
        except ValueError:
            print('ValueError')
        sleep(0.5)
        print('Digite o número do cateto adjacente:')
        try:
            cateto_adjacente = float(input(''))
        except ValueError:
            print('ValueError')
        return print(f'{hypot(cateto_oposto, cateto_adjacente)}')

    def numero_de_pi():
        Object()
        print('Número de pi:')
        linha()
        return print(f'{pi}')

    #main
    Object()
    print('!!Opções Disponíveis!!')
    print('1 - Seno do número em radiano')
    print('2 - Cosseno do número em radiano')
    print('3 - Tangente do número em raiano')
    print('4 - Hipotenusa dos números')
    print('5 - Consultar o número de pi')
    print('0 - Voltar')
    Object()
    try:
        user = int(input('Escolha: '))
    except ValueError:
            print('ValueError')

    if user == 1:
        os.system("cls || clear")
        seno()
    elif user == 2:
        os.system("cls || clear")
        cosseno()
    elif user == 3:
        os.system("cls || clear")
        tangente()
    elif user == 4:
        os.system("cls || clear")
        hipotenusa()
    elif user == 5:
        os.system("cls || clear")
        numero_de_pi()
    elif user == 0:
        sleep(0.5)
        print('Voltando..')
        sleep(0.5)
        rodando = 'termino'
        os.system("cls || clear")
        import main
    else:
        Object()
        print('Ops.. Tente novamente!')