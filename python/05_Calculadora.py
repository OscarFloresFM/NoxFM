#Este fue mi primer programa en el mundo de programacion
#No fue en python, fue en C++
#Pero decidi empezar a aprender python por su simplicidad y facilidad de uso
#Asi que decidi hacer una simple calculadora en python
#La calculadora puede hacer operaciones basicas como suma, resta, multiplicacion y division
#Para ello sera un selector de operaciones
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division por cero"
print("Bienvenido a la calculadora")
print("Seleccione la operacion:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
operacion = input("Ingrese el numero de la operacion (1/2/3/4): ")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
if operacion == '1':
    print("El resultado de la suma es:", suma(num1, num2))
elif operacion == '2':
    print("El resultado de la resta es:", resta(num1, num2))
elif operacion == '3':
    print("El resultado de la multiplicacion es:", multiplicacion(num1, num2))
elif operacion == '4':
    print("El resultado de la division es:", division(num1, num2))
else:
    print("Operacion invalida")
#Espero que les guste el primer programa que empezara a enseñarles python