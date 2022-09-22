# Ejercicio 1: Pide un número por teclado e indica si es un número primo o no. 
# Un número primo es aquel que solo puede dividirse entre 1 y sí mismo. 
# Por ejemplo: 25 no es primo, ya que 25 es divisible entre 5, sin embargo, 17 si es primo.

numero = int(input("Ingrese un número a evaluar: "))
contador = 0
print()
print("{0} es divisible por".format(numero), end=": ")
for n in range(1, numero+1):
  if numero % n == 0:
    print(n, end=" - ")
    contador += 1
print("Fin")
if contador == 2:
  print("El número ingresado si es primo, tiene {0} divisores".format(contador))
else:
  print("El número ingresado no es primo, tiene {0} divisores".format(contador))