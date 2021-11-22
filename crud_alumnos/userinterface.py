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


def show_registros_class(alumnos):
  print("CUENTA\tNOMBRE\tTELEFONO\tGENERO\tCORREO")
  show_separator()
  for alumno in alumnos:
    alumno.obtener_formato_columna()


def getInput(label, teclado, defaultvalue):
  print(label + "(" + defaultvalue + ")")
  valorTeclado = teclado.readline().rstrip().lstrip()
  if valorTeclado == "":
    return defaultvalue
  else:
    return valorTeclado

def getAlumnoData(alumno, getcuenta, teclado):
  if getcuenta:
    alumno.cuenta = getInput("Cuenta", teclado, alumno.cuenta)
  alumno.nombre = getInput("Nombre", teclado, alumno.nombre)
  alumno.telefono = getInput("Telefono", teclado, alumno.telefono)
  alumno.genero = getInput("Genero", teclado, alumno.genero)
  alumno.correo = getInput("Correo", teclado, alumno.correo)
  return alumno

def showAlumnoData(alumno):
  print("Cuenta:\t" + alumno.cuenta)
  print("Nombre:\t" + alumno.nombre)
  print("Telefono:\t" + alumno.telefono)
  print("Genero:\t" + alumno.genero)
  print("Correo:\t" + alumno.correo)

def show_separator():
  print("="*60)
