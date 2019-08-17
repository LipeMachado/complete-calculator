#-*- coding: utf-8 -*-
import os
from time import sleep

rodando = 'rodando'

while rodando != 'termino':
    def Object():
        print('-=-'*10)
        sleep(0.5)

    def linha():
        print('-'*15)

    def area_retangulo():
        Object()
        sleep(0.5)
        print('Digite o valor de lado:')
        try:
            lado = float(input(''))
        except ValueError:
            print('ValueError')
        print('Digite o valor da altura:')
        try:
            altura = float(input(''))
        except ValueError:
            print('ValueError')
        linha()
        return print(f'{lado*altura} cm²')

    def area_quadrado():
        Object()
        sleep(0.5)
        print('Digite o valor do lado:')
        try:
            lado = float(input(''))
        except ValueError:
            print('ValueError')
        linha()
        return print(f'{lado**2} cm²')

    def area_triangulo():
        Object()
        sleep(0.5)
        print('Digite o valor da base:')
        try:
            base = float(input(''))
        except ValueError:
            print('ValueError')
        print('Digite o valor da altura:')
        try:
            altura = float(input(''))
        except ValueError:
            print('ValueError')
        resultado = (base*altura) / 2
        linha()
        return print(f'{resultado} cm²')

    def area_trapezio():
        Object()
        sleep(0.5)
        print('Digite o valor da base maior:')
        try:
            base_maior = float(input(''))
        except ValueError:
            print('ValueError')
        print('Digite o valor da base menor:')
        try:
            base_menor = float(input(''))
        except ValueError:
            print('ValueError')
        print('Digite o valor da altura:')
        try:
            altura = float(input(''))
        except ValueError:
            print('ValueError')
        resultado = ((base_maior + base_menor)* altura) / 2
        linha()
        return print(f'{resultado} cm²')

    def area_losango():
        Object()
        sleep(0.5)
        print('Digite o valor da diagonal maior:')
        try:
            diagonal_maior = float(input(''))
        except ValueError:
            print('ValueError')
        print('Digite o valor da diagonal menor:')
        try:
            diagonal_menor  = float(input(''))
        except ValueError:
            print('ValueError')
        resultado = (diagonal_maior * diagonal_menor) / 2
        linha()
        return print(f'{resultado} cm²')

    def area_circulo():
        Object()
        sleep(0.5)
        print('Digite o valor do raio:')
        try:
            raio = float(input(''))
        except ValueError:
            print('ValueError')
        linha()
        return print(f'{raio**2} π cm²')

    #main
    Object()
    print('!!Opções Disponíveis!!')
    print('CASO O VALOR SEJA COM VÍRGULA, USE PONTO')
    print('1 - Área do Retangulo')
    print('2 - Área do Quadrado')
    print('3 - Área do Triangulo')
    print('4 - Área do Trapézio')
    print('5 - Área do Losango')
    print('6 - Área do Círculo')
    print('0 - Voltar')
    Object()
    try:
        user = int(input('Escolha: '))
    except ValueError:
        print('ValueError')

    if user == 1:
        os.system("cls")
        area_retangulo()
    elif user == 2:
        os.system("cls")
        area_quadrado()
    elif user == 3:
        os.system("cls")
        area_triangulo()
    elif user == 4:
        os.system("cls")
        area_trapezio()
    elif user == 5:
        os.system("cls")
        area_losango()
    elif user == 6:
        os.system("cls")
        area_circulo()
    elif user == 0:
        os.system("cls")
        sleep(0.5)
        print('Voltando..')
        sleep(0.5)
        rodando = 'termino'
    else:
        Object()
        print('Ops.. Tente novamente')