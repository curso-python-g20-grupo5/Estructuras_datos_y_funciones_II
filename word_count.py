import sys
'''
El texto lorem ipsum es un texto de prueba que se utiliza para demostrar distintas
tipografías además de usarse para rellenar espacios que requieran largos textos.
¿Cuántas palabras componen este texto?
Genere un archivo llamado word_count.py que importe un texto a Python y realice
las siguientes tareas:
'''
#Verificar que se proporcione el archivo de texto
if len(sys.argv) != 2:
    print("Uso: python word_count.py <archivo_texto>")
    sys.exit(1)


archivo_texto = sys.argv[1]
#Se abre archivo solicitado para utilización de texto, alojandose en una variable dicho texto
with open(archivo_texto, "r") as file:
    texto=file.read()

#Se utiliza metodo 'set' para eliminar valores duplicados
caracteres_distintos = set(texto)
#Se utiliza metodo 'len' para contabilizar valores
distintos = len(caracteres_distintos)

#Se utiliza metodo 'split' para separar por palabras
palabras = texto.split()

#Se utiliza metodo 'len' para contabilizar palabras
palabras_distintas = set(palabras)
cantidad = len(palabras_distintas)

#Salida de datos por consola
print(f"El numero de caracteres distintos es: {distintos}")
print(f"El numero de palabras distintas es: {cantidad}")