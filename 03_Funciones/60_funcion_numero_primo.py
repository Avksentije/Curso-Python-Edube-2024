def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True   
    if num % 2 == 0: 
        return False    
#Para determinar si un número a partir del 3 es primo, 
#necesitamos verificar si es divisible por cualquier número primo menor o igual a su raíz cuadrada.
    for i in range(3, int(num**0.5), 2): 
        if num % i == 0: 
            return False
    return True
#Para este último for, tuvimos que investigar los principios para evaluar un número primo
#La forma de resolverlo es revisar solo numeros impares a partir del 3, dado que los pares no son primos.
#Para esto, se emplea el criterio de dividir entre 2 y entre cualquier otro número primo (raíz cuadrada)
#Al aplicar int() a un número flotante, la función int() truncará el número flotante hacia cero, eliminando cualquier parte fraccionaria y dejando solo la parte entera.

for i in range(1, 20):
	if is_prime(i):
			print(i, end=" ")
print()