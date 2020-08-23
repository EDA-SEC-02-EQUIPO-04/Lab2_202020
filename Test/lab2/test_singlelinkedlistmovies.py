"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
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

import pytest
import config
import csv
from DataStructures import singlelinkedlist as lts
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from ADT import list as lts


def cmpfunction(element1, element2):
    if element1 == element2:
        return 0


@pytest.fixture
def lst():
    lst = lts.newList(cmpfunction)
    return lst


@pytest.fixture
def books():
    books = []
    books.append({'book_id': '1', 'book_title': 'Title 1', 'author': 'author 1'})
    books.append({'book_id': '2', 'book_title': 'Title 2', 'author': 'author 2'})
    books.append({'book_id': '3', 'book_title': 'Title 3', 'author': 'author 3'})
    books.append({'book_id': '4', 'book_title': 'Title 4', 'author': 'author 4'})
    books.append({'book_id': '5', 'book_title': 'Title 5', 'author': 'author 5'})
    print(books[0])
    return books


@pytest.fixture
def lstbooks(books):
    lst = lts.newList(cmpfunction)
    for i in range(0, 5):
        lts.addLast(lst, books[i])
    return lst


def test_empty(lst):
    assert lts.isEmpty(lst) == True
    assert lts.size(lst) == 0


def test_addFirst(lst, books):
    assert lts.isEmpty(lst) == True
    assert lts.size(lst) == 0
    lts.addFirst(lst, books[1])
    assert lts.size(lst) == 1
    lts.addFirst(lst, books[2])
    assert lts.size(lst) == 2
    book = lts.firstElement(lst)
    assert book == books[2]


def test_addLast(lst, books):
    assert lts.isEmpty(lst) == True
    assert lts.size(lst) == 0
    lts.addLast(lst, books[1])
    assert lts.size(lst) == 1
    lts.addLast(lst, books[2])
    assert lts.size(lst) == 2
    book = lts.firstElement(lst)
    assert book == books[1]
    book = lts.lastElement(lst)
    assert book == books[2]


def test_getElement(lstbooks, books):
    book = lts.getElement(lstbooks, 1)
    assert book == books[0]
    book = lts.getElement(lstbooks, 5)
    assert book == books[4]


def test_removeFirst(lstbooks, books):
    assert lts.size(lstbooks) == 5
    lts.removeFirst(lstbooks)
    assert lts.size(lstbooks) == 4
    book = lts.getElement(lstbooks, 1)
    assert book == books[1]


def test_removeLast(lstbooks, books):
    assert lts.size(lstbooks) == 5
    lts.removeLast(lstbooks)
    assert lts.size(lstbooks) == 4
    book = lts.getElement(lstbooks, 4)
    assert book == books[3]


def test_insertElement(lst, books):
    assert lts.isEmpty(lst) is True
    assert lts.size(lst) == 0
    lts.insertElement(lst, books[0], 1)
    assert lts.size(lst) == 1
    lts.insertElement(lst, books[1], 2)
    assert lts.size(lst) == 2
    lts.insertElement(lst, books[2], 1)
    assert lts.size(lst) == 3
    book = lts.getElement(lst, 1)
    assert book == books[2]
    book = lts.getElement(lst, 2)
    assert book == books[0]


def test_isPresent(lstbooks, books):
    book = {'book_id': '10', 'book_title': 'Title 10', 'author': 'author 10'}
    assert lts.isPresent(lstbooks, books[2]) > 0
    assert lts.isPresent(lstbooks, book) == 0


def test_deleteElement(lstbooks, books):
    pos = lts.isPresent(lstbooks, books[2])
    assert pos > 0
    book = lts.getElement(lstbooks, pos)
    assert book == books[2]
    lts.deleteElement(lstbooks, pos)
    assert lts.size(lstbooks) == 4
    book = lts.getElement(lstbooks, pos)
    assert book == books[3]


def test_changeInfo(lstbooks):
    book10 = {'book_id': '10', 'book_title': 'Title 10', 'author': 'author 10'}
    lts.changeInfo(lstbooks, 1, book10)
    book = lts.getElement(lstbooks, 1)
    assert book10 == book


def test_exchange(lstbooks, books):
    book1 = lts.getElement(lstbooks, 1)
    book5 = lts.getElement(lstbooks, 5)
    lts.exchange(lstbooks, 1, 5)
    assert lts.getElement(lstbooks, 1) == book5
    assert lts.getElement(lstbooks, 5) == book1


def test_carga():
    lista = []
    lst = lt.newList('SINGLE_LINKED', cmpfunction)

    file = config.data_dir + 'MoviesCastingRaw-small.csv'
    sep = ';'
    dialect = csv.excel()
    dialect.delimiter = sep

    assert (lt.size(lst) == 0), "La lista no empieza en cero."

    try:
        with open(file, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, dialect=dialect)

            for row in reader:
                lista.append(row)
                lt.addLast(lst, row)

    except:
        assert False, "Se presento un error al cargar el archivo."

    assert len(lista) == lt.size(lst), "Son diferentes tamaños."

    for i in range(len(lista)):
        assert lt.getElement(lst, i + 1) == lista[i], "Las listas no estan en el mismo orden."
