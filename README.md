# Estructuras datos y funciones II
En este repositorio se presenta el desarrollo para la actividad Estructuras datos y funciones II.

## Descripción del proyecto

Este repositorio está compuesto por cuatro archivos: 
  - ```conversiones.py```: este archivo corresponde a la solución de la actividad 'Conversiones'
  - ```lorem ipsum.txt```: este es un texto generado para ser importado a Python
  - ```word_count.py```: este archivo es un contador de palabras para la actividad 'Contador de Palabras'
  - ```recordatorios.py```: este archivo corresponde a la solución de la actividad 'Recordatorios'

## Actividad 1: Conversiones
Para esta actividad es importante considerar los siguientes datos:

### Tasas de Conversión de Peso Chileno:
● a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.00013

En esta actividad se nos pide crear un archivo llamado ```conversiones.py``` que contenga una estructura de datos apropiada que permita ingresar tasas de conversión. El ingreso de estos datos (tasas de conversión) se hacen mediante ```sys.argv```, el cuál permite rescatar argumentos desde el terminal, en el siguiente orden: Sol, Peso Argentino y Dólar Americano.
Ademmás, se debe ingresar un cuarto argumento que sea el valor en peso chileno a convertir. Por consiguiente, el programa debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas. Al ejecutar el programa se espera el siguiente output:

Tenemos que los datos presentados anteriormente son ingresados mediante la terminal ```python conversiones.py 0.0046 0.093 0.0013 10000```. Por tanto, el programa ha de devolver lo siguiente:
```
Los 10000 pesos equivalen a:
46.0 Soles
930.0 Pesos Argentinos
13.0 Dólares
```
## Actividad 2: Contador de Palabras
El texto ```lorem ipsum``` es un texto genérico que se utiliza para demostrar tipografías además de usarse para rellenar espacios que requieran largos textos. Ante ello, buscamos generar un programa que pueda contabilizar las palabras que componen este texto.
Generamos un archivo llamado ```word_count.py``` que pueda importar un texto a Python y realice las siguientes tareas:
- Contar la cantidad de caracteres distintos que componen un texto.
- Contar el número de palabras distintas que componen el texto ingresado (```lorem ipsum.txt```). Además, para poder separar un texto por espacios, se busca utilizar el método ```.split("")```.
Para poder importar un texto a Python se debe ejecutar el siguiente código:
```
with open(“texto.txt”, "r") as file:
  texto=file.read()
```
Donde ```texto.txt``` corresponderá a la ruta del archivo a importar. En nuestro caso, la variable texto será denominada ```archivo_texto```:

```
# Se crea la variable archivo_texto en donde alojamos el número 1 de los valores que toma el sys.argv
archivo_texto = sys.argv[1]

#Se abre archivo solicitado para utilización de texto, alojandose en una variable dicho texto
with open(archivo_texto, "r") as file:
    texto=file.read()
```

Para comprobar el correcto funcionamiento del código se provee el archivo lorem_ipsum.txt.
Al ejecutar el programa ```python word_count.py lorem_ipsum.txt``` se espera el siguiente output:
```
El número de caracteres distintos es: 40
El número de palabras distintas es: 243
```
## Actividad 3: Recordatorios
El archivo ```recordatorios.py``` incluye una serie de eventos que quieren ser recordados por el usuario. Estos eventos se presentan a través del formato fecha (año-mes-día), una hora y una descripción del evento.
Esta actividad se compuso por cuatro momentos:
1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para
“Empezar el Año”.
2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar
de tal manera que sea el 16 de Julio.
3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del
día del trabajo.
4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a
las 22 hrs.
Al ejecutar el programa ```python recordatorios.py``` se espera el siguiente output:
```
[['2021-01-01', '11:00', 'Levantarse y ejercitar'],
['2021-01-02', '06:00', 'Empezar el año'],
['2021-07-16', '13:00', 'No hacer nada es feriado'],
['2021-09-18', '16:00', 'Ramadas'],
['2021-12-24', '22:00', 'Cena de Navidad'],
['2021-12-25', '00:00', 'Navidad'],
['2021-12-31', '22:00', 'Cena de Año Nuevo']]
```

## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)
- [Claudia Aguayo](https://github.com/aguayo40)

⌨️ con ❤️ por el Grupo 5 - G20 😊
