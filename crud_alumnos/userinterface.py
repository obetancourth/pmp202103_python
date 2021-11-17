def show_menu():
  print("M\tMostrar los Registros de Alumnos")
  print("C\tCrear Nuevo Alumno")
  print("A\tEditar Alumno")
  print("B\tBorrar Alumno")
  show_separator()
  print("Q\tSalir")
  show_separator()
  print("Escriba una Opcion seguido del Enter")

def show_registros(rows):
  print("CUENTA\tNOMBRE\tTELEFONO\tGENERO\tCORREO")
  show_separator()
  for row in rows:
    print(row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + "\t" + row[4])

def show_separator():
  print("="*60)
