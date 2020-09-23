# -*- coding: utf-8 -*-

from time import sleep
import os

while True:

    Object = lambda : print("-=-"*10)
    linha = lambda : print("-"*15)

    def celsius_fahrenheit():
        while True:
            Object()
            try:
                print('Digite o valor do Cº:')
                celsius = float(input(''))
                resultado = (celsius * 9/5) + 32
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                celsius_fahrenheit()
            else:
                linha()
                return  print(f"{resultado}º Fahrenheit")
            break

    def fahrenheit_celsius():
        while True:
            try:
                print('Digite o valor de Fº:')
                fahrenheit = float(input(''))
                resultado = (fahrenheit - 32) / 1.8
            except Exception:
                os.system("cls || clear")
                Object()
                print('ERROR: Digite um número válido.')
                fahrenheit_celsius()
            else:
                linha()
                return print(f"{resultado}º Celsius")
            break
    
    def celsius_kelvin():
        while True:
            try:
                print('Digite o valor do Cº:')
                celsius = float(input(''))
                resultado = (celsius + 273.15)
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                celsius_kelvin()
            else:
                linha()
                return print(f"{resultado} Kelvin")
            break

    def kelvin_celsius():
        while True:
            try:
                print('Digite o valor de Kelvin:')
                kelvin = float(input(''))
                resultado = (kelvin - 273.15)
            except Exception:
                os.system("cls || clear")
                Object()
                print("ERROR: Digite um número válido.")
                kelvin_celsius()
            else:
                linha()
                return print(f"{resultado}º Celsius")
            break

    #main
    Object()
    print('!!Opções Disponíveis!!')
    print('ATENÇÃO: CASO O VALOR SEJA COM VÍRGULA, USE PONTO')
    print('1 - Conversão de Celsius para Fahrenheit')
    print('2 - Conversão de Fahrenheit para Celsius')
    print('3 - Conversão de Celsius para Kelvin')
    print('4 - Conversão de Kelvin para Celsius')
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
            celsius_fahrenheit()
        elif user == 2:
            os.system("cls || clear")
            fahrenheit_celsius()
        elif user == 3:
            os.system("cls || clear")
            celsius_kelvin()
        elif user == 4:
            os.system("cls || clear")
            kelvin_celsius()
        else:
            os.system("cls || clear")
            Object()
            print('ERROR: Esta opção não existe!')