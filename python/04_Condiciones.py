#Ahora en esta leccion hablaremos sobre condicionales en python
#Empecemos con la estructura basica de un condicional if
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
#En este ejemplo pedimos al usuario que ingrese su edad y la convertimos a entero
#Luego usamos un condicional if para verificar si la edad es mayor o igual a 18
#Si la condicion es verdadera se imprime "Eres mayor de edad"
#Si la condicion es falsa se ejecuta el bloque else e imprime "Eres menor de edad"
#Puedes tambien usar elif para verificar multiples condiciones o switch entre diferentes opciones

#Ahora con while loops
contador = 0
while contador < 5:
    print("Contador es:", contador)
    contador += 1
#En este ejemplo usamos un while loop para imprimir el valor del contador mientras sea menor a 5
#El contador empieza en 0 y se incrementa en 1 en cada iteracion hasta que la condicion ya no se cumple
#Puedes cambiar la condicion y el incremento para ver como afecta el comportamiento del loop
#Tambien puedes usar break para salir del loop antes de que la condicion falle
#Esto facilmente se puede cambiar con un for loop dependiendo de la situacion
#Eso es todo por ahora, practica estos conceptos y en la proxima leccion hablaremos sobre funciones