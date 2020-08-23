from lab2 import listnode as node
from Utils import error as error

def newList(cmpfunction = None):
    new_list = {'first': None, 'last': None,'size' = 0, 'type' = 'SINGLE_LINKEDLIST', 'cmpfunction':cmpfunction}
    return new_list

def addFirst(list,element):
    try:
        new_node = node.newsingleNode(element)
        new_node['next'} = lst['next']
        if(['size'] == 0):
            lst['last'] = lst['first']
        lst['size'] += 1
        return lst
    except:
        print('Error agregando un nodo al comienzo de una lista')

def addLast(lst, element):
    try:
        new_node = node.newsingleNode(element)
        if lst['size'] == 0:
            lst['first'] = new_node
        else:
            lst['last']['next'] = new_node
        lst['last'] = new_node
        lst['size'] += 1
        return lst
    except:
        print('Error afrefando un nodo al final de la lista')

def deleteEelement(lst,pos):
    try:
        node = lst['first']
        prev = lst['first']
        searchpos = 1
        if (pos == 1):
            lst['first'] = lst['first']['next']
        elif (pos > 1):
            while searchpos < pos:
                searchpos += 1
                prev = node
                node = node['next']
            prev['next'] = node['next']
        lst['size'] -= 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->deleteElement: ')

def removeFirst(lst):
    """ Remueve el primer elemento de la lista. 
    
    Elimina y retorna el primer elemento de la lista.  El tamaño de la lista se decrementa en uno.  Si la lista
    es vacía se retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['first'] != None:
            temp = lst['first']['next']
            node = lst['first']
            lst['first'] = temp
            lst['size'] -= 1
            if (lst['size'] == 0):
                lst['last'] = lst['first']
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->removeFirst: ')


def removeLast(lst):
    """ Remueve el último elemento de la lista.
    
    Elimina el último elemento de la lista  y lo retorna en caso de existir. El tamaño de la lista se decrementa en 1. 
    Si la lista es vacía  retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['size'] > 0:
            if lst['first'] == lst['last']:
                node = lst['first']
                lst['last'] = None
                lst['first'] = None
            else:
                temp = lst['first']
                while temp['next'] != lst['last']:
                    temp = temp['next']
                node = lst['last']
                lst['last'] = temp
                lst['last']['next'] = None
            lst['size'] -= 1
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->remoLast: ')


def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista. 
    
    Inserta el elemento en la posición pos de la lista. La lista puede ser vacía.  Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,  0 < pos <= size(lst) 

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)
        if (pos == 1):
            new_node['next'] = lst['first']
            lst['first'] = new_node
        else:
            cont = 1
            prev = lst['first']
            current = lst['first']
            while cont < pos:
                prev = current
                current = current['next']
                cont += 1
            new_node['next'] = current
            prev['next'] = new_node
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->insertElement: ')


def isPresent(lst, element):
    """ Informa si el elemento element esta presente en la lista. 
    
    Informa si un elemento está en la lista.  Si esta presente, retorna la posición en la que se encuentra 
    o cero (0) si no esta presente. Se utiliza la función de comparación utilizada durante la creación 
    de la lista para comparar los elementos. La cual debe retornar cero en caso de que los elementos sean iguales.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar

    Raises:
        Exception
    """
    try:
        size = lst['size']
        if size > 0:
            node = lst['first']
            keyexist = False
            for keypos in range(1, size + 1):
                if (lst['cmpfunction'](element, node['info']) == 0):
                    keyexist = True
                    break
                node = node['next']
            if keyexist:
                return keypos
        return 0
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->isPresent: ')


def changeInfo(lst, pos, newinfo):
    """ Cambia la informacion contenida en el nodo de la lista que se encuentra en la posicion pos.
    
    Args:   
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el nodo de la posición pos

    Raises:
        Exception
    """
    try:
        current = lst['first']
        cont = 1
        while cont < pos:
            current = current['next']
            cont += 1
        current['info'] = newinfo
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->changeInfo: ')


def exchange(lst, pos1, pos2):
    """ Intercambia la informacion en las posiciones pos1 y pos2 de la lista.

    Args:
        lst: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posiocion del segundo elemento

    Raises:
        Exception
    """
    try:
        infopos1 = getElement(lst, pos1)
        infopos2 = getElement(lst, pos2)
        changeInfo(lst, pos1, infopos2)
        changeInfo(lst, pos2, infopos1)
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->exchange: ')


def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.
    
    Se retorna una lista que contiene los elementos a partir de la posicion pos, con una longitud de numelem elementos.  
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        sublst = {'first': None, 'last': None, 'size': 0, 'type': 'SINGLE_LINKED', 'cmpfunction': lst['cmpfunction']}
        cont = 1
        loc = pos
        while cont <= numelem:
            elem = getElement(lst, loc)
            addLast(sublst, elem)
            loc += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->subList: ')
            

