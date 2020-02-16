# -*- coding: utf-8 -*-
import os
from time import sleep
from math import sqrt

while True:
	
	Object = lambda : print('-=-'*10)	
	linha = lambda : print('-'*15)
	
	def soma():
		while True:
			Object()
			try:
				print('Digite o primeiro número para soma.')
				primeiro_numero = float(input(''))
				print('+')
				print('Digite o segundo número para soma.')
				segundo_numero = float(input(''))
			except Exception:
				os.system("cls || clear")
				Object()
				print("ERROR: Digite um número válido.")
				soma()
			else:
				linha()
				return print(primeiro_numero + segundo_numero)
			break
		
	def subtracao():
		while True:
			Object()
			try:
				print('Digite o primeiro número para subtração.')
				primeiro_numero = float(input(''))
				print('-')
				print('Digite o segundo número para subtração.')
				segundo_numero = float(input(''))
			except Exception:
				os.system("cls || clear")
				Object()
				print('ERROR: Digite um valor válido.')
				subtracao()	
			else:
				linha()
				return print(primeiro_numero - segundo_numero)
			break
		
	def multiplicacao():
		while True:
			Object()
			try:
				print('Digite o primeiro número para multiplicação.')
				primeiro_numero = float(input(''))
				print('X')
				print('Digite o segundo número para multiplicação.')
				segundo_numero = float(input(''))
			except Exception:
				os.system("cls || clear")
				Object()
				print('ERROR: Digite um valor válido.')
				multiplicacao()
			else:
				linha()
				return print(primeiro_numero * segundo_numero)
			break
		
	def divisao():
		while True:
			Object()
			try:
				print('Digite o primeiro número para divisão.')
				primeiro_numero = float(input(''))
				print('/')
				print('Digite o segundo número para divisão.')
				segundo_numero = float(input(''))
			except Exception:
				os.system("cls || clear")
				Object()
				print("ERROR: Digite um valor válido.")
				divisao()
			else:
				linha()
				return print(primeiro_numero / segundo_numero)
			break

	def exponenciacao():
		while True:
			Object()
			try:
				print('Digite o primeiro número para exponenciação.')
				primeiro_numero = float(input(''))
				print('aª')
				print('Digite o segundo número para exponenciação.')
				segundo_numero = float(input(''))
			except Exception:
				os.system("cls || clear")
				Object()
				print('ERROR: Digite um valor válido.')
				exponenciacao()
			else:
				linha()
				return print(primeiro_numero ** segundo_numero)
			break

	def raiz_quadrada():
		while True:
			Object()
			try:
				print('Digite o valor da raiz.')
				print('√')
				valor_da_raiz = float(input(''))
				resultado = sqrt(valor_da_raiz)
			except Exception:
				os.system("cls || clear")
				Object()
				print("ERROR: Digite um valor válido.")
				raiz_quadrada()
			else:
				linha()
				return print(resultado)
			break	

	def fatorial():
		while True:
			Object()
			try:	
				print('Digite o valor do fatorial.')
				valor_do_fatorial = int(input(''))
				contador = 1
				resultado = 1
				while contador <= valor_do_fatorial:
					resultado *= contador
					contador += 1
			except Exception:
				os.system("cls || clear")
				Object()
				print("ERROR: Digite um número válido.")
				fatorial()
			else:
				linha()
				return print(resultado)
			break

	#main
	Object()
	print('!!Opções Disponíveis!!')
	print('ATENÇÃO: CASO O VALOR SEJA COM VÍRGULA, USE PONTO')
	print('1 - Soma')
	print('2 - Subtração')
	print('3 - Multiplicação')
	print('4 - Divisão')
	print('5 - Exponenciação/Potenciação')
	print('6 - Raiz Quadrada')
	print('7 - Fatorial')
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
			soma()
		elif user == 2:
			os.system("cls || clear")
			subtracao()
		elif user == 3:
			os.system("cls || clear")
			multiplicacao()
		elif user == 4:
			os.system("cls || clear")
			divisao()
		elif user == 5:
			os.system("cls || clear")
			exponenciacao()
		elif user == 6:
			os.system("cls || clear")
			raiz_quadrada()
		elif user == 7:
			os.system("cls || clear")
			fatorial()
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