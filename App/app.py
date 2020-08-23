"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from time import process_time
from Sorting import insertionsort as ins
from Test import sorting as ism


def loadCSVFile(file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    # lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList()  # Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time()  # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                lt.addLast(lst, row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time()  # tiempo final
    print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar tiempo según el ordenamiento")
    print("0- Salir")


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size'] == 0:
        print("La lista esta vacía")
        return 0
    else:
        t1_start = process_time()  # tiempo inicial
        counter = 0
        iterator = it.newIterator(lst)
        while it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower():  # filtrar por palabra clave
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return counter


def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0


def obtener_peliculas(lst, numero):
    peliculas = lst
    lista = []
    print(lt.getElement(peliculas,12))
    for i in peliculas:
        if lt.getElement(peliculas) >= 6:
            mejores_peliculas = lista.append(lt.getElement(peliculas,i))
    return mejores_peliculas

def orderElementsByCriteria(criteria, lst, elementos, funcion):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if lst['size']==0:
        print("La lista está vacía")
    else:
        if funcion == 1:
            t1_start = it.process_time()
            lista = obtener_peliculas(criteria,lst)
            ordenada = ins.insertionsrot(lista,less)
            mejores = ordenada[0:int(elementos)]
            t1_stop = it.process_time()
            print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
        elif funcion == 2:
            t1_start = it.process_time()
            lista = obtener_peliculas(criteria,lst)
            ordenada = ins.selectionsort(lista,less)
            mejores = ordenada[0:int(elementos)]
            t1_stop = it.process_time()
            print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
        elif funcion == 3:
            t1_start = it.process_time()
            lista = obtener_peliculas(criteria,lst)
            ordenada = ins.shellsort(listaless)
            mejores = ordenada[0:int(elementos)]
            t1_stop = it.process_time()
            print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return elementos


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()  # se require usar lista definida
    lista2 = lt.newList()
    while True:
        printMenu()  # imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar:\n')  # leer opción ingresada
        if len(inputs) > 0:

            if int(inputs[0]) == 1:  # opcion 1
                lista = loadCSVFile("Data/Peliculas/MoviesCastingRaw-small.csv")  # llamar funcion cargar datos
                lista2 = loadCSVFile("Data/Peliculas/SmallMoviesDetalsCleaned.csv")
                print("Datos cargados, ", lista['size'], " elementos cargados")
            elif int(inputs[0]) == 2:  # opcion 2
                if lista == None or lista['size'] == 0:  # obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("La lista tiene ", lista['size'], " elementos")
                    print(lista["first"]["info"]["vote_average"])
            elif int(inputs[0]) == 3:  # opcion 3
                if lista == None or lista['size'] == 0:  # obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')                    
                    counter = countElementsFilteredByColumn(criteria,"nombre",
                                                            lista)  # filtrar una columna por criterio
                    print("Coinciden ", counter, " elementos con el crtierio: ", criteria)
            elif int(inputs[0]) == 4:  # opcion 4
                if lista == None or lista['size'] == 0:  # obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    counter = countElementsByCriteria(criteria, 0, lista)
                    print("Coinciden ", counter, " elementos con el crtierio: '", criteria, "' (en construcción ...)")
            elif int(inputs[0]) == 5: # opción 5
                if lista == None or lista['size'] == 0:
                    print("La lista está vacía")
                else:
                    print("¿Cómo quiere ordenar los elementos?")
                    print("Seleccione 1 para insertion sort")
                    print("Seleccione 2 para selection sort")
                    print("Seleccione 3 para shell sort")
                    funcion = input("Seleccione cómo quiere ordenar los elementos: ")
                    numero = input ("Buscando los top: ")
                    obtener_peliculas(lista,numero)
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
