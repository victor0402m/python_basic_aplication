import random



""" Ejemplo de busqueda binaria 
implementada por recursividad"""
def busqueda_binaria(lista, numero, bajo, alto):
	if bajo > alto :
		return False

	mitad = (alto+bajo) // 2

	if lista[mitad] == numero:
		return True
	elif numero < lista[mitad]:
		return busqueda_binaria(lista, numero, bajo, mitad-1)
	else:
		return busqueda_binaria(lista, numero, mitad-1, alto)


""" Implementacin de busquda binaria por 
ciclos repetitivos"""
def busqueda_binaria_loop(lista, numero, bajo, alto):
	while bajo <= alto:
		mitad = (alto+bajo) // 2

		if lista[mitad] == numero:
			return True
		elif numero < lista[mitad]:
			alto = mitad-1
		else:
			bajo = mitad-1

	return False
		

""" Funcion para inicalizar el programa"""
if __name__ == '__main__':
	lista_numeros = [random.randint(0,100) for x in range(10)]
	lista_numeros.sort()
	print (lista_numeros)

	numero_buscado = input('Que numero busca? ')
	numero_buscado = int(numero_buscado)

	busqueda = busqueda_binaria(lista_numeros, numero_buscado, 0, len(lista_numeros)-1 )

	if busqueda:
		print('Encontrado')
	else:
		print('No encontrado')

	busqueda_por_ciclos = busqueda_binaria_loop(lista_numeros, numero_buscado, 0, len(lista_numeros)-1 )

	if busqueda_por_ciclos:
		print('Encontrado loop')
	else:
		print('No encontrado loop')