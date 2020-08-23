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
from Sorting import shellsort as shell
from Sorting import selectionsort as selection
from Sorting import insertionsort as insertion

from time import process_time


def load_csv_file(file_d, file_c, sep=';'):
    """
    Carga un archivo csv a una lista
    Args:
        file_d
            Archivo de texto del cual se cargaran los detalles de las películas.
        file_c
            Archivo de texto del cual se cargaran los castings de las películas.
        sep :: str
            Separadores código para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None
    """
    lst_d = lt.newList("ARRAY_LIST")  # Usando implementacion arraylist
    lst_c = lt.newList("ARRAY_LIST")  # Usando implementacion arraylist
    # lst_d = lt.newList()  # Usando implementacion linkedlist
    # lst_c = lt.newList()  # Usando implementacion linkedlist
    print('Cargando archivos...')
    t1_start = process_time()  # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(file_d, encoding='utf-8-sig') as csvfile_d, open(file_c, encoding='utf-8-sig') as csvfile_c:
            spamreader_d = csv.DictReader(csvfile_d, dialect=dialect)
            spamreader_c = csv.DictReader(csvfile_c, dialect=dialect)
            for row in spamreader_d:
                lt.addLast(lst_d, row)
            for row in spamreader_c:
                lt.addLast(lst_c, row)
    except:
        # lst_d = lt.newList("ARRAY_LIST")  #Usando implementacion arraylist
        # lst_c = lt.newList("ARRAY_LIST")  #Usando implementacion arraylist
        lst_d = lt.newList()  # Usando implementacion linkedlist
        lst_c = lt.newList()  # Usando implementacion linkedlist
        print('Se presento un error en la carga de los archivos')
    t1_stop = process_time()  # tiempo final
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return lst_d, lst_c


def print_menu():
    """
    Imprime el menu de opciones
    """
    print('\nBienvenido')
    print('1- Cargar Datos')
    print('2- Contar los elementos de la Lista')
    print('3- Contar películas filtradas por palabra clave')
    print('4- Consultar buenas películas de un director')
    print('5- Ordenar películas por votos')
    print('6- Conocer a un director y todas sus películas')
    print('0- Salir')


def cantidad_peliculas_director(director, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        director:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        lst
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
            if director.lower() in element[column].lower():  # filtrar por palabra clave
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return counter


def encontrar_buenas_peliculas(director, vote_average, lst_d, lst_c):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if len(lst_d) == 0:
        print('Las listas están vacías')
        return 0, 0
    else:
        t1_start = process_time()  # tiempo inicial
        all_director_movies = []
        # Search all director movies and add them to a list.
        for element in lst_c['elements']:
            if director.lower() in element['director_name'].lower():  # filtrar por nombre
                all_director_movies.append(element)
        # Search good movies and add vote points to list.
        good_movies_votes = []
        for movie in all_director_movies:
            for element in lst_d['elements']:
                if movie['id'] == element['id']:
                    actual_vote = float(element['vote_average'])
                    if actual_vote >= vote_average:
                        good_movies_votes.append(actual_vote)
        # Calculate number of good movies and total vote average of director.
        counter_good_movies = len(good_movies_votes)
        total_vote_average = sum(good_movies_votes) / counter_good_movies
        t1_stop = process_time()  # tiempo final
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return counter_good_movies, round(total_vote_average, 1)


def conocer_director(director, lst_d, lst_c):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if len(lst_d) == 0:
        print('Las listas están vacías')
        return 0, 0
    else:
        t1_start = process_time()  # tiempo inicial
        all_director_movies = []
        # Search all director movies and add them to a list.
        for element in lst_c['elements']:
            if director.lower() in element['director_name'].lower():  # filtrar por nombre
                all_director_movies.append(element)
        # Search movies and add vote points to list.
        movies_votes = []
        for movie in all_director_movies:
            for element in lst_d['elements']:
                if movie['id'] == element['id']:
                    actual_vote = float(element['vote_average'])
                    movies_votes.append(actual_vote)
        # Calculate number of movies and total vote average of director.
        counter_movies = len(movies_votes)
        total_vote_average = sum(movies_votes) / counter_movies
        t1_stop = process_time()  # tiempo final
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return all_director_movies, counter_movies, round(total_vote_average, 1)


def less(element1, element2):
    if float(element1['vote_average']) < float(element2['vote_average']):
        return True
    return False


def greater(element1, element2):
    if float(element1['vote_average']) > float(element2['vote_average']):
        return True
    return False


def order_movies(function, lst_d, req_elements, algorithm, column):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if len(lst_d) == 0:
        print('Las listas están vacías')
        return []
    else:
        t1_start = process_time()  # tiempo inicial
        movies_votes = []
        # Search all movies votes depending on parameter.
        for element in lst_d['elements']:
            movies_votes.append(element[column])
        # Sort movies.
        if algorithm == 'selection':
            if function == 'less':
                selection.selectionSort(movies_votes, less)
            elif function == 'greater':
                selection.selectionSort(movies_votes, greater)
        elif algorithm == 'shell':
            if function == 'less':
                shell.shellSort(movies_votes, less)
            elif function == 'greater':
                shell.shellSort(movies_votes, greater)
        elif algorithm == 'insertion':
            if function == 'less':
                insertion.insertionSort(movies_votes, less)
            elif function == 'greater':
                insertion.insertionSort(movies_votes, greater)
        # Assign movie to vote_average or count.
        if column == 'vote_average':
            for index_movie in range(req_elements):
                for movie in lst_d:
                    if movie['vote_average'] == movies_votes[index_movie]:
                        movies_votes[index_movie] = {'vote_average': movies_votes[index_movie], 'movie_data': movie}
                        break
        else:
            for index_movie in range(req_elements):
                for movie in lst_d:
                    if movie['vote_count'] == movies_votes[index_movie]:
                        movies_votes[index_movie] = {'vote_count': movies_votes[index_movie], 'movie_data': movie}
                        break
        t1_stop = process_time()  # tiempo final
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return movies_votes


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """

    while True:
        print_menu()  # imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar:\n')  # leer opción ingresada
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                details_list, casting_list = load_csv_file('../Data/MoviesDetailsCleaned-small.csv',
                                                           '../Data/MoviesCastingRaw-small.csv')  # Cargar datos
                if len(details_list) == len(casting_list):
                    print('Datos cargados, ' + str(len(details_list['elements'])) + ' elementos cargados en listas')
                else:
                    print('Datos cargados, aunque inconsistentes')
            elif int(inputs[0]) == 2:  # opcion 2
                if len(details_list['elements']) == 0:  # obtener la longitud de la lista
                    print('La lista esta vacía')
                else:
                    print('La lista tiene ' + str(len(details_list['elements'])) + ' elementos')
            elif int(inputs[0]) == 3:  # opcion 3
                director = input('Ingrese un director para consultar su cantidad de películas:\n')  # filtrar columna
                counter_movies = cantidad_peliculas_director(director, 'director_name', casting_list)
                print('Coinciden', counter_movies, 'elementos con el director', director)
            elif int(inputs[0]) == 4:  # opcion 4
                director = input('Ingrese el nombre del director para conocer sus buenas películas:\n')
                counter, average = encontrar_buenas_peliculas(director, 6, details_list, casting_list)
                print('Existen', counter, 'buenas películas del director', director, 'en el catálogo')
                print('Las buenas películas de este director tienen un promedio de votación de', average, 'puntos.')
            elif int(inputs[0]) == 5:  # opcion 5
                print('Ranking de películas')
                req = input('Ingrese el número de películas requeridas: ')
                while int(req) < 10:
                    req = input('Ingrese por lo menos 10 películas requeridas: ')
                # Sorting direction.
                function = input('Ingrese 1 para orden ascendente o 2 para descendente: ')
                if function == '1':
                    function = 'greater'
                elif function == '2':
                    function = 'less'
                # Column criteria for sorting.
                column = input('Ingrese 1 para ordenar por cantidad de votos o '
                               '2 para ordenar por calificación promedio: ')
                if column == '1':
                    column = 'vote_count'
                elif column == '2':
                    column = 'vote_average'
                # Type of sorting.
                algorithm = input('Ingrese 1 para ordenar con selection sorting o '
                                  '2 para ordenar con shell sorting o '
                                  '3 para ordenar con insertion sorting: ')
                if algorithm == '1':
                    algorithm = 'selection'
                elif algorithm == '2':
                    algorithm = 'shell'
                elif algorithm == '3':
                    algorithm = 'insertion'
                # Show results.
                ordered_list = order_movies(function, details_list, req, algorithm, column)
                print(ordered_list)
                print(req, 'best' if function == 'greater' else 'worst',
                      'count' if column == 'vote_count' else 'average')
                print('Se ordenó la lista')
            elif int(inputs[0]) == 6:  # opcion 6
                director = input('Ingrese el nombre del director para conocer su trabajo:\n')
                peliculas, counter, average = conocer_director(director, details_list, casting_list)
                print('Las películas dirigidas por', director, 'son:\n', peliculas)
                print('Existen', counter, 'películas del director', director, 'en el catálogo')
                print('Las películas de este director tienen un promedio de votación de', average, 'puntos.')
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == '__main__':
    main()
