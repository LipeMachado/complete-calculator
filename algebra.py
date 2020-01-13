# -*- coding: utf-8 -*-
import os
from time import sleep
from math import sqrt

rodando = 'rodando'

while rodando != 'terminado':
	
	Object = lambda : print('-=-'*10)
	
	linha = lambda : print('-'*15)
	
	def soma():
		Object()
		print('Digite o primeiro número para soma.')
		try:
			primeiro_numero = float(input(''))
		except ValueError:
			print('ValueError')
		print('+')
		print('Digite o segundo número para soma.')
		try:
			segundo_numero = float(input(''))
		except ValueError:
			print('ValueError')
		linha()
		return print(primeiro_numero + segundo_numero)
		
	def subtracao():
		Object()
		print('Digite o primeiro número para subtração.')
		try:
			primeiro_numero = float(input(''))
		except ValueError:
			print('ValueError')
		print('-')
		print('Digite o segundo número para subtração.')
		try:
			segundo_numero = float(input(''))
		except ValueError:
			print('ValueError')	
		linha()
		return print(primeiro_numero - segundo_numero)
		
	def multiplicacao():
		Object()
		print('Digite o primeiro número para multiplicação.')
		try:
			primeiro_numero = float(input(''))
		except ValueError:
			print('ValueError')
		print('X')
		print('Digite o segundo número para multiplicação.')
		try:
			segundo_numero = float(input(''))
		except ValueError:
			print('ValueError')
		linha()
		return print(primeiro_numero * segundo_numero)
		
	def divisao():
		Object()
		print('Digite o primeiro número para divisão.')
		try:
			primeiro_numero = float(input(''))
		except ValueError:
			print('ValueError')
		print('/')
		print('Digite o segundo número para divisão.')
		try:
			segundo_numero = float(input(''))
		except ValueError:
			print('ValueError')	
		linha()
		return print(primeiro_numero / segundo_numero)
		
	def exponenciacao():
		Object()
		print('Digite o primeiro número para exponenciação.')
		try:
			primeiro_numero = float(input(''))
		except ValueError:
			print('ValueError')
		print('aª')
		print('Digite o segundo número para exponenciação.')
		try:
			segundo_numero = float(input(''))
		except ValueError:
			print('ValueError')
		linha()
		return print(primeiro_numero ** segundo_numero)
		
	def raiz_quadrada():
		Object()
		print('Digite o valor da raiz.')
		print('√')
		try:
			valor_da_raiz = float(input(''))
		except ValueError:
			print('ValueError')
		resultado = sqrt(valor_da_raiz)
		linha()
		return print(resultado)
	
	def fatorial():
		Object()
		print('Digite o valor do fatorial.')
		try:
			valor_do_fatorial = int(input(''))
		except ValueError:
			print('ValueError')
		contador = 1
		resultado = 1
		
		while contador <= valor_do_fatorial:
			resultado *= contador
			contador += 1
		return print(resultado)

	#main
	Object()
	print('!!Opções Disponíveis!!')
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
	except ValueError:
		print('ValueError')
	
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
	else:
		Object()
		print('Ops.. Tente novamente!')