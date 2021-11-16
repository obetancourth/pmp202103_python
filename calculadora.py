#Leer datos de la linea de comando
import sys

# print("Escriba su nombre: ")
entrada = sys.stdin
# print("Su respuesta es " + entrada.readline() )
# print("="* 40)
# print("Escriba su correo: ")
# print("Su respuesta es " + entrada.readline() )

print("Ingrese el primer operador: ")
operador1 = float(entrada.readline().rstrip().lstrip())
print("Ingrese el segundo operador: ")
operador2 = float(entrada.readline().rstrip().lstrip())
print("Determine que operación realizar")
print("+ Sumar, - Restar, / Dividir, * Multiplicar")
tipo_operacion = entrada.readline().rstrip().lstrip()
# Tarea en clase
# Determinar si la operacion es dentro de lo establecido
# Realizar la operacion asignandola a un variable
# Mostrar el Resutlado con el siguiente formato:
# <operador1> <tipo_operacion> <operador2> = <resutlado>
# 10 + 10 = 20
if tipo_operacion == "+":
  print("Tipo de operación Suma")
elif tipo_operacion == "-":
  print("Tipo de operación Resta")
elif tipo_operacion == "/":
  print("Tipo de operación División")
elif tipo_operacion == "*":
  print("Tipo de operación Multiplicación")
else:
  print("Tipo de operación no Reconocida")
