from dao import getConn
from alumno import Alumno
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

def getByCuenta(cuenta):
  global cursor
  global conn
  cursor.execute("SELECT * from ALUMNOS where cuenta=?;", (cuenta,))
  row = cursor.fetchone()
  alumno = Alumno()
  alumno.cuenta = row[0]
  alumno.nombre = row[1]
  alumno.telefono = row[2]
  alumno.genero = row[3]
  alumno.correo = row[4]
  return alumno

def getAllAlumnos():
  rows = getAll()
  alumnos_list = list()
  for row in rows:
    alumno= Alumno()
    alumno.cuenta = row[0]
    alumno.nombre = row[1]
    alumno.telefono = row[2]
    alumno.genero = row[3]
    alumno.correo = row[4]
    alumnos_list.append(alumno)
  return alumnos_list

def save_new(alumno):
  global cursor
  global conn
  insertSql = "INSERT into ALUMNOS(cuenta, nombre, telefono, genero, correo) values (?,?,?,?,?);"
  cursor.execute(
    insertSql,
    (alumno.cuenta, alumno.nombre, alumno.telefono, alumno.genero, alumno.correo)
  )
  conn.commit()

def update(alumno):
  global cursor
  global conn
  updateSql = "UPDATE ALUMNOS set nombre=?, telefono=?, genero=?, correo=? where cuenta = ?;"
  cursor.execute(
      updateSql,
      (alumno.nombre, alumno.telefono, alumno.genero, alumno.correo, alumno.cuenta)
  )
  conn.commit()


def delete(alumno):
  global cursor
  global conn
  deleteSql = "DELETE FROM ALUMNOS where cuenta = ?;"
  cursor.execute(
      deleteSql,
      (alumno.cuenta, )
  )
  conn.commit()
