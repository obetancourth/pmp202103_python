from dao import getConn
conn = getConn()
cursor = conn.cursor()

def createTable():
  global cursor
  global conn
  cursor.execute("CREATE TABLE IF NOT EXISTS ALUMNOS(cuenta text PRIMARY KEY, nombre text, telefono text, genero text, correo text)")
  conn.commit()

def getAll():
  global cursor
  global conn
  cursor.execute("SELECT * from ALUMNOS")
  rows = cursor.fetchall()
  return rows
