import sys
from userinterface import show_separator, show_menu, show_registros
from alumno import Alumno
from alumnosdao import createTable, getAll

show_separator()
print("CRUD de Alumnos V 0.0.1")
show_separator()

teclado = sys.stdin
createTable()

opcion = ""
while True:
  show_menu()
  opcion = teclado.readline().rstrip().lstrip().upper()
  if opcion == "Q":
    break
  elif opcion == "M":
    show_registros(getAll())
  elif opcion == "T":
    mi_alumno = Alumno()
    mi_alumno.cuenta = "12345678"
    mi_alumno.correo = "alguncorreo@corre.com"
    mi_alumno.nombre = "Fulanito de Tal y Porcuerra"
    mi_alumno.genero = "Masculino"
    mi_alumno.telefono = "00000000"
    mi_alumno.obtener_formato_columna()
