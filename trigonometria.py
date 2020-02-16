# -*- coding: utf-8 -*-
from time import sleep
import os
from math import sin, cos, tan, hypot, pi

while True:

    Object = lambda : print('-=-'*10)
    linha = lambda : print('-'*15)

    def seno():
        while True:
            Object()
            try:
                print('Digite o número para saber seu Seno:')
                numero = float(input(''))
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                seno()
            else:
                linha()
                return print(f'{sin(numero)}')
            break

    def cosseno():
        while True:
            Object()
            try:
                print('Digite o nnúmero para saber seu Cosseno:')
                numero = float(input(''))
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                cosseno()
            else:
                linha()
                return print(f'{cos(numero)}')
            break

    def tangente():
        while True:
            Object()
            try:
                print('Digite o número para saber sua Tangente:')
                numero = float(input(''))
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                tangente()
            else:
                linha()
                return print(f'{tan(numero)}')
            break

    def hipotenusa():
        while True:
            Object()
            try:
                print('Digite o número do cateto oposto:')
                cateto_oposto = float(input(''))
                print('Digite o número do cateto adjacente:')
                cateto_adjacente = float(input(''))
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                hipotenusa()
            else:
                linha()
                return print(f'{hypot(cateto_oposto, cateto_adjacente)}')
            break

    def numero_de_pi():
        Object()
        print('Número de pi:')
        linha()
        return print(f'{pi}')

    #main
    Object()
    print('!!Opções Disponíveis!!')
    print('ATENÇÃO: CASO O VALOR SEJA COM VÍRGULA, USE PONTO')
    print('1 - Seno do número em radiano')
    print('2 - Cosseno do número em radiano')
    print('3 - Tangente do número em raiano')
    print('4 - Hipotenusa dos números')
    print('5 - Consultar o número de pi')
    print('0 - Voltar')
    Object()
    try:
        user = int(input('Escolha: '))
    except Exception:
            os.system("cls || clear")
            Object()
            print('ERROR: Isto que você digitou está incorreto. Digite um número inteiro!')
    else:
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
            break
        else:
            os.system("cls || clear")
            Object()
            print('ERROR: Esta opção não existe!')