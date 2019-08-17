import os
from time import sleep
from math import sqrt

rodando = 'rodando'

while rodando != 'terminado':
	def Object():
		print('-=-'*10)
		sleep(0.5)
	
	def linha():
		print('-'*15)
	
	def soma():
		Object()
		print('Digite o primeiro número para soma.')
		primeiro_numero = float(input(''))
		print('+')
		print('Digite o segundo número para soma.')
		segundo_numero = float(input(''))
		linha()
		return print(primeiro_numero + segundo_numero)
		
	def subtracao():
		Object()
		print('Digite o primeiro número para subtração.')
		primeiro_numero = float(input(''))
		print('-')
		print('Digite o segundo número para subtração.')
		segundo_numero = float(input(''))
		linha()
		return print(primeiro_numero - segundo_numero)
		
	def multiplicacao():
		Object()
		print('Digite o primeiro número para multiplicação.')
		primeiro_numero = float(input(''))
		print('X')
		print('Digite o segundo número para multiplicação.')
		segundo_numero = float(input(''))
		linha()
		return print(primeiro_numero * segundo_numero)
		
	def divisao():
		Object()
		print('Digite o primeiro número para divisão.')
		primeiro_numero = float(input(''))
		print('/')
		print('Digite o segundo número para divisão.')
		segundo_numero = float(input(''))
		linha()
		return print(primeiro_numero / segundo_numero)
		
	def exponenciacao():
		Object()
		print('Digite o primeiro número para exponenciação.')
		primeiro_numero = float(input(''))
		print('aª')
		print('Digite o segundo número para exponenciação.')
		segundo_numero = float(input(''))
		linha()
		return print(primeiro_numero ** segundo_numero)
		
	def raiz_quadrada():
		Object()
		print('Digite o valor da raiz.')
		print('√')
		valor_da_raiz = float(input(''))
		resultado = sqrt(valor_da_raiz)
		linha()
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
	print('0 - Voltar')
	Object()
	user = int(input('Escolha: '))
	
	if user == 1:
		os.system("cls")
		soma()
	elif user == 2:
		os.system("cls")
		subtracao()
	elif user == 3:
		os.system("cls")
		multiplicacao()
	elif user == 4:
		os.system("cls")
		divisao()
	elif user == 5:
		os.system("cls")
		exponenciacao()
	elif user == 6:
		os.system("cls")
		raiz_quadrada()
	elif user == 0:
		sleep(0.5)
		print('Voltando..')
		sleep(0.5)
		rodando = 'termino'
	else:
		Object()
		print('Ops.. Tente novamente!')