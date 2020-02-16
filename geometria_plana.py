# -*- coding: utf-8 -*-
import os
from time import sleep

while True:
    
    Object = lambda : print('-=-'*10)    
    linha = lambda : print('-'*15)

    def area_retangulo():
        while True:
            Object()
            try:
                print('Digite o valor de lado:')
                lado = float(input(''))
                print('Digite o valor da altura:')
                altura = float(input(''))
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                area_retangulo()
            else:
                linha()
                return print(f'{lado*altura} cm²')
            break

    def area_quadrado():
        while True:
            Object()
            try:
                print('Digite o valor do lado:')
                lado = float(input(''))
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                area_quadrado()
            else:
                linha()
                return print(f'{lado**2} cm²')
            break

    def area_triangulo():
        while True:
            Object()
            try:
                print('Digite o valor da base:')
                base = float(input(''))
                print('Digite o valor da altura:')
                altura = float(input(''))
                resultado = (base*altura) / 2
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                area_triangulo()
            else:
                linha()
                return print(f'{resultado} cm²')
            break

    def area_trapezio():
        while True:
            Object()
            try:
                print('Digite o valor da base maior:')
                base_maior = float(input(''))
                print('Digite o valor da base menor:')
                base_menor = float(input(''))
                print('Digite o valor da altura:')
                altura = float(input(''))
                resultado = ((base_maior + base_menor)* altura) / 2
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                area_trapezio()
            else:
                linha()
                return print(f'{resultado} cm²')
            break

    def area_losango():
        while True:
            Object()
            try:
                print('Digite o valor da diagonal maior:')
                diagonal_maior = float(input(''))
                print('Digite o valor da diagonal menor:')
                diagonal_menor  = float(input(''))
                resultado = (diagonal_maior * diagonal_menor) / 2
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                area_losango()
            else:
                linha()
                return print(f'{resultado} cm²')
            break

    def area_circulo():
        while True:
            Object()
            try:
                print('Digite o valor do raio:')
                raio = float(input(''))
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                area_circulo()
            else:
                linha()
                return print(f'{raio**2} π cm²')
            break

    #main
    Object()
    print('!!Opções Disponíveis!!')
    print('ATENÇÃO: CASO O VALOR SEJA COM VÍRGULA, USE PONTO')
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
    except Exception:
        os.system("cls || clear")
        Object()
        print('ERROR: Isto que você digitou está incorreto. Digite um número inteiro!')
    else:
        if user == 1:
            os.system("cls || clear")
            area_retangulo()
        elif user == 2:
            os.system("cls || clear")
            area_quadrado()
        elif user == 3:
            os.system("cls || clear")
            area_triangulo()
        elif user == 4:
            os.system("cls || clear")
            area_trapezio()
        elif user == 5:
            os.system("cls || clear")
            area_losango()
        elif user == 6:
            os.system("cls || clear")
            area_circulo()
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