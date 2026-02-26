#Diego Lipa
#Fechas en Python

from datetime import date, datetime

# Fecha actual
hoy = date.today()
print(hoy)

# formatear fecha
formateado = hoy.strftime("%d-%m-%Y")
print(formateado)

# Hora actual
fecha_actual = datetime.now()
print(fecha_actual)

#camturar el año
anio = fecha_actual.year
print(anio)

mes = fecha_actual.month
print(mes)

dia = fecha_actual.day
print(dia)

hora_actual = fecha_actual.strftime("%H:%M:%S")
print(hora_actual)

# Fomato AM PM
hora_am_pm = fecha_actual.strftime("%I:%M:%S %p")
print(hora_am_pm)
