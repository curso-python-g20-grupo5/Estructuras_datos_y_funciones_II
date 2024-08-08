import sys #importación de librería sys
'''
 Se solicita crear un archivo conversiones.py y una estructura de datos apropiada que permita
ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar
mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.
'''
#ingreso de datos mediante sys.argv, alojadas en variable 'tasas'
tasas = sys.argv[1:]
if len(tasas) < 4:#requerimiento para ingresar 4 valores
    print("Ingresa los 4 valores solicitados")
    sys.exit(1)

list = tasas
print(list)

# Se crea lista con los valores ingresados
lista_tasas = tasas

# Se solicita indice por lista para alojarlo en variables separadas
sol_peruano = float(lista_tasas[0])
peso_argentino = float(lista_tasas[1])
dolar_americano = float(lista_tasas[2])
peso_chileno = int(lista_tasas[3])

#Se realiza conversion de variables
sol = sol_peruano*peso_chileno
peso_a = peso_argentino*peso_chileno
dolar = dolar_americano*peso_chileno

#Se presentan los datos por consola
print(f"Los {peso_chileno} equivalen a: ")
print(f"{sol:.1f} Soles")
print(f"{peso_a:.1f} Pesos Argentinos")
print(f"{dolar:.1f} Dólares")




    



