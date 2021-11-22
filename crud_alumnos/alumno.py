class Alumno:
  cuenta = ""
  nombre = ""
  genero = ""
  correo = ""
  telefono = ""

  def obtener_formato_columna(self):
    print(self.cuenta + "\t" + self.nombre + "\t" + self.telefono + "\t" + self.genero + "\t" + self.correo)
