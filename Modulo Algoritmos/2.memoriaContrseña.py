# Ejercicio 2: Escribe una aplicación que solicite al usuario que ingrese una contraseña cualquiera.
# Después se le pedirá que ingrese nuevamente la contraseña, con 3 intentos. Cuando
# acierte ya no pedirá más la contraseña y mostrará un mensaje diciendo “Felicitaciones,
# recordás tu contraseña”. Si falla luego de 3 intentos se mostrará el mensaje “Tenes que
# ejercitar la memoria”. Los mensajes quedarán en pantalla a la espera que el usuario
# presione una tecla, luego de esto se cerrará el programa.

contrasenia = input("Ingrese la contraseña a recordar: ")
contador = 0
while contador < 3:
        contrasenia_intento = input("Ingrese de nuevo la contraseña: ")
        if contrasenia_intento == contrasenia:
            print("Felicitaciones, recordás tu contraseña")
            break
        else:
            print("La contraseña es incorrecta.\n")
            contador +=1
if contador == 3:
        print("Tenes que ejercitar la memoria\n")
input("Presione una tecla para finalizar el programa.")
