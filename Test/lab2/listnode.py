def newsingleNode(element):
    node = {'info':element,'netx':None}
    return node

def gerEelement(node):
    return node['info']

def assingnNextNode(currentNode, nextNode):
    currentNode['next'] = nextNode