import pytest
import csv
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from ADT import list as lts

def test_carga():
    lista=[]
    lst = lt.newList('ARRAY_LIST', cmpfunction) 

    file = 'Data/theMoviesdb/MoviesCastingRaw-small.csv'
    sep= ';'
    dialect = csv.excel()
    dialect.delimiter = sep


    assert (lt.size(lst)==0), "La lista no empieza en cero."

    try:
        with open (file, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile,dialect=dialect)

            for row in reader:
                lista.append(row)
                lt.addLast(lst,row)

    except:
        assert False, "Se presento un error al cargar el archivo."

    assert len(lista) == lt.size(lst), "Son diferentes tamaños."

    for i in range (len(lista)):
        assert lt.getElement(lst,i+1)==lista[i], "Las listas no estan en el mismo orden."





