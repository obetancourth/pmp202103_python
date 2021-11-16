import csv;
# Esto es un comentario en Python
print("Hello World!!!")
str_message = "¡¡¡Hola Mundo en Español!!!"
print(str_message)
print("="*80)
# Bloques de control y ciclos
bol_es_tercera_edad = False
if bol_es_tercera_edad:
  print("Si es tercera edad....")
else:
  print("No es Tercera Edad...")
print("*"*80)
# Ciclos
for i in range(0,100, 10):
  print(i)
#
pfizer_counts=0
aztrazeneca_counts=0
with open("data/covid19.csv") as covidFile:
  lector_csv = csv.reader(covidFile, delimiter=",")
  for linea in lector_csv:
    if linea[4] == "PSF":
      pfizer_counts += 1
    if linea[4] == "AZT":
      aztrazeneca_counts += 1

print([pfizer_counts, aztrazeneca_counts])
