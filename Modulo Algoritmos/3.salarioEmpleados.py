# Ejercicio 3: Por teclado se ingresa el valor hora de un empleado. Posteriormente se ingresa el
# nombre del empleado, la antigüedad y la cantidad de horas trabajadas en el mes. Se
# pide calcular el importe a cobrar teniendo en cuenta que al total que resulta de
# multiplicar el valor hora por la cantidad de horas trabajadas. Además, si el empleado
# tiene más de 10 años de antigüedad hay que sumarle la cantidad de años trabajados
# multiplicados por $30. Imprimir en pantalla el nombre, la antigüedad y el total a cobrar.

valor_hora = int(input("Ingrese el valor por hora del empleado: "))
nombre_empleado = input("Ingrese el nombre: ")
antiguedad_empledo = int(input("Ingrese los años de antigüedad del empleado: "))
trabajo_mes = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
total = valor_hora*trabajo_mes
if antiguedad_empledo>10:
        total += antiguedad_empledo*30
print("El monto a pagar a "+nombre_empleado+" con "+str(antiguedad_empledo)+" años de antigüedad es de $"+str(total))