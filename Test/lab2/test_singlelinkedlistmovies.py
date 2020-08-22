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
        if pos == 1:
            

