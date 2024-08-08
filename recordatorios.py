'''
Se provee del archivo recordatorios.py que incluye una serie de eventos que
quieren ser recordados por usted. El formato de estos recordatorios son una fecha
(año-mes-día), una hora y una descripción del evento.
'''

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para“Empezar el Año”.
recordatorios.insert(1,['2021-02-02', "06:00", "Empezar el año"])

#2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio.
modificado = recordatorios[3] #busca el indice 2 de recordatorio y lo guarda en variable
modificado.remove('2021-07-15') #remueve el contenido del indice 
modificado.insert(0,'2021-07-16')#inserta el contenido del nuevo indice editando el valor de la lista


#3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo.
eliminado = recordatorios[2] #se busca por indice y se guarda en variable
recordatorios.remove(eliminado)#se elimina el evento indicado

#4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
cena_navidad = ['2021-12-24', "22:00", "Cena de Navidad"]#crea primera variable con datos solicitados (lista)
cena_new_year = ['2021-12-31', "22:00", "Cena de Año Nuevo"] #crea segunda variable con datos solicitados (lista)

recordatorios.insert(4, cena_navidad) #inserta lista en indice 4 dentro de lista recordatorios
recordatorios.insert(7, cena_new_year) #inserta lista en indice 7 dentro de lista recordatorios

# Output para ver por consola los datos de manera ordenada
print(f"{recordatorios[0]}, \n{recordatorios[1]}, \n{recordatorios[2]}, \n{recordatorios[3]}, \n{recordatorios[4]}, \n{recordatorios[5]}, \n{recordatorios[6]}")

