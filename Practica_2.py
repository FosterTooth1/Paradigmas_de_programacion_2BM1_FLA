#Autores: Flores Lara Alberto; Rendon Sierra Carlos Alexis; Saucillo González Jesse Obed
#3BV2

#1.Escribe un programa en Python que cree una función lambda que sume 15 a cualquier número que se le pase como argumento. 
#2.Crea una función lambda que multiplique el argumento de entrada x con el argumento de entrada y. 
#3.Escribe un programa que proporcione una función lambda que divida el valor de entrada x, entre un número aleatorio (puedes usar la función random() o bien la función random.randint(lower,upper).
#4.Indica  lo  que  hacen  los  siguientes  códigos,  especialmente  la  función realizada por el cálculo lambda.

#Punto 1
#Se crea una funcion lambda que suma 15 a cualquier numero que se le pase como argumento
sumar15=lambda x:x+15
#Se imprime el resultado de la funcion lambda sumar15
print(sumar15(5))

#Punto 2
#Se crea una funcion lambda que multiplica el argumento de entrada x con el argumento de entrada y
multiplicar=lambda x,y:x*y
#Se imprime el resultado de la funcion lambda multiplicar
print(multiplicar(3,2))

#Punto 3    
#Se crea una funcion lambda que divide el valor de entrada x, entre un numero aleatorio
#Se importa el modulo random
import random
#Se crea una funcion lambda que divide el valor de entrada x, entre un numero aleatorio
dividir=lambda x: x/random.randint(1,10)
#Se imprime el resultado de la funcion lambda dividir
print(dividir(20))

#Punto 4
#La función tomar un argumento n y devuelve una funcion lambda que multiplica el argumento x por n
def func_compute(n): return lambda x : x * n
#Se llama a la funcion func_compute y se le pasa como argumento el numero 2
result = func_compute(2)
#Se imprime el resultado de la funcion (siendo el doble del numero que se le pase como argumento)
print("Double the number of 15 =", result(15))

#Se crea una tupla con las asignaturas y sus notas
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
('Social sciences', 82)]
#Se imprime la tupla creada anteriormente
print("Original list of tuples:")
print(subject_marks)
#se llama a la función sort y se utiliza como parametro de ordenamiento la nota de la asignatura
#mediante la función lambda x: x[1] que indica que se ordene por la segunda posición de la tupla
subject_marks.sort(key = lambda x: x[1])
#Se imprime la tupla ordenada
print("\nResult:")
print(subject_marks)

#Se crea una lista con los numeros del 1 al 10
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Se imprime la lista creada anteriormente
print("Original list of integers:")
print(nums)
#Se imprime la lista que se crea abajo
print("\n number of the said list:")
#Se crea una lista con los numeros de la lista nums elevados al cuadrado
#mediante la función lambda x: x ** 2 que indica que se eleve al cuadrado
#y se utiliza la función map para aplicar la función lambda a cada elemento de la lista nums
#se usa list para convertir el objeto map en una lista
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
#lo mismo que el anterior pero elevando al cubo
print("\n every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)