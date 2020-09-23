# -*- coding: utf-8 -*-
import os
from time import sleep

while True:

    Object = lambda : print('-=-'*10)

    Object()
    print('Calculadora feita por:')
    print('Telegram:        @LipeMachado')
    print('Canal/Telegram:  @coursesprogrammerandhacker')
    print('GitHub:          LipeMachado')
    print('Qualquer bug ou dúvida pergunte.')

    Object()
    print('!!Bem-Vindo!!')
    print('1 - Algebra - Matemática Básica')
    print('2 - Geometria Plana')
    print('3 - Trigonometria')
    print('0 - Sair')
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
            import algebra
        elif user == 2:
            os.system("cls || clear")
            import geometria_plana
        elif user == 3:
            os.system("cls || clear")
            import trigonometria
        elif user == 4:
            os.system("cls || clear")
            import fisica
        elif user == 0:
            print('Saindo.... BYE, BYE')
            sleep(0.55)
            os.system("cls || clear")
            break
        else:
            os.system("cls || clear")
            Object()
            print('ERROR: Esta opção não existe!')