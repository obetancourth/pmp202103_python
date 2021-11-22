import sys
from userinterface import show_separator, show_menu, show_registros_class, getAlumnoData, showAlumnoData
from alumno import Alumno
from alumnosdao import createTable, getAllAlumnos, save_new, getByCuenta, update, delete

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
    show_registros_class(getAllAlumnos())
  elif opcion == "C":
    alumno = getAlumnoData(Alumno(), True, teclado)
    save_new(alumno)
  elif opcion == "A":
    print("Ingrese la Cuenta a Actualizar:")
    cuenta = teclado.readline().rstrip().lstrip()
    alumno = getByCuenta(cuenta)
    showAlumnoData(alumno)
    alumno = getAlumnoData(alumno, False, teclado)
    update(alumno)
  elif opcion == "B":
    print("Ingrese la Cuenta a Eliminar:")
    cuenta = teclado.readline().rstrip().lstrip()
    alumno = getByCuenta(cuenta)
    showAlumnoData(alumno)
    eliminar = teclado.readline().lstrip().rstrip().upper()
    if eliminar == 'S':
      delete(alumno)
