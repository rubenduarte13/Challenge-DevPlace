# Ejercicio 4: Generar un número aleatorio comprendido entre 0 y 1000. Pedir, a continuación, al
# usuario adivinar el número escogido por el ordenador. Para ello, debe introducir un
# número comprendido entre 0 y 1000. Se compara el número introducido con el
# calculado por el ordenador y se muestra en la consola "es mayor" o "es menor" en
# función del caso. Se repite la operación hasta que el usuario encuentra el número.
# 5. Pedir al usuario que ingrese un número repetidamente hasta que ingrese un -1 y en ese
# caso se terminará el programa.
# Al terminar, mostrará lo siguiente:
# a. – mayor número introducido
# b. – menor número introducido
# c. – suma de todos los números
# d. – suma de los números

from random import randint

n =  randint(0, 1000)
intento = 0
print("Intenta adivinar un número entre 0 y 1000.")
while intento != n:
        intento = int(input(">"))
        if intento < n:
            print("El número es mayor al dado")
        if intento > n:
            print("el número es menor al dado")
        if intento == n:
            print("Felicitaciones, adivinaste el numero!!")
