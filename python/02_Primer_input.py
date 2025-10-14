#Ahora hablare un poco sobre los inputs en python
#Un input es una funcion que permite al usuario ingresar datos desde el teclado
#La sintaxis es la siguiente:
variable = input()
#El input siempre devuelve un string (cadena de texto) por lo que si se desea un numero se debe convertir
#Por ejemplo:
numero = int(input("Ingresa un numero: "))
#En este caso se le pide al usuario que ingrese un numero y se convierte a entero con int()
#Si se desea un numero decimal se puede usar float()
decimal = float(input("Ingresa un numero decimal: "))
#Tambien se puede usar input sin conversion si se desea trabajar con cadenas de texto
texto = input("Ingresa un texto: ")
#En este caso se le pide al usuario que ingrese un texto y se guarda en la variable texto
#Finalmente se puede combinar input con print para mostrar mensajes al usuario
print("El numero que ingresaste es:", numero)
#El resultado sera "El numero que ingresaste es: " seguido del numero ingresado por el usuario
#Ahora para terminar una calculadora simple que sume dos numeros ingresados por el usuario
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
suma = num1 + num2
print("La suma de", num1, "y", num2, "es:", suma)
#El resultado sera "La suma de X y Y es: Z" donde X y Y son los numeros ingresados y Z es la suma de ambos
#Recuerda que siempre puedes combinar input con otras funciones y operaciones para crear programas mas complejos
#Eso es todo por ahora, en la proxima leccion hablaremos sobre condicionales