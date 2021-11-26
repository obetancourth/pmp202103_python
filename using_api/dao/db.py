import sqlite3

class StatsCovid:
  def __init__(self):
    self.conn = sqlite3.connect("covidStat.db")
    cursor = self.conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS covidstats (
      codigo INTEGER PRIMARY KEY AUTOINCREMENT,
      countryIso TEXT NOT NULL,
      country TEXT NOT NULL,
      statdate TEXT NOT NULL,
      cases INTEGER NOT NULL,
      newcases INTEGER NOT NULL
    );""")
    self.conn.commit()
    cursor.close()

  def insert( self, countryIso, country, statdate, cases, newcases):
    cursor = self.conn.cursor()
    cursor.execute("""INSERT INTO covidstats (countryIso, country,
      statdate, cases, newcases) VALUES (?, ?, ?, ?, ?);""",
      (countryIso, country, statdate, cases, newcases)
    )
    self.conn.commit()
    cursor.close()

  def getByMonth(self):
    cursor = self.conn.cursor()
    cursor.execute("""SELECT substr(statdate, 6, 2) as Month,
    max(cases) as MaxCasos, avg(newcases) as PromCasosNuevos, count(*) as registros
    from covidstats group by 1;""")
    rows = cursor.fetchall()
    cursor.close()
    return rows
