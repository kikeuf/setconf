
def getnodeValuebyXPath(root, path, ForceNodeCreation = False):
    ret = getnodebyXPath(root, path, ForceNodeCreation)
    if ret[1] is None:
        return str(ret[0])
    else:
        return ret[1]

def getnodeObjectbyXPath(root, path, ForceNodeCreation = False):
    ret = getnodebyXPath(root, path, ForceNodeCreation)
    return ret[0]
def getnodebyXPath(root, path, ForceNodeCreation = False):

    items = path.split('/')
    nNode = root
    id = -1
    for item in items:
        if item != '':
            idnNode = getchildnode(nNode, item, ForceNodeCreation)
            id = idnNode[0]
            nNode = idnNode[1]

    if id != -1:
        arrayvalue = nNode[id]
        return nNode, arrayvalue
    else:
        return nNode, None

def getchildnode(parentnode, name, ForceNodeCreation = False):

    try:
        id = -1
        ret = getnodeindex(name)
        #print(ret)
        if ret[0] != "":
            id = ret[0]
            name = ret[1]

        #if isinstance(parentnode[name], list):
        #    print(parentnode[name][id] + " is list")
        cnode = parentnode[name]

        #if id != "":
        #    return cnode[id]
        #else:
        #    return cnode
        return id, cnode

    except KeyError as ek:
        if ForceNodeCreation:
            try:
                if isinstance(parentnode, list):
                    parentnode.append(name)
                else:
                    parentnode[name] = None

                return -1, parentnode[name]

            except Exception as ek2:
                #print(repr(ek2))
                return -1, None
    except:
        return -1, None

def getnodeindex(name):
    # Cas de l'index de liste
    idx = -1
    nname = name
    if name[-1] == "]":
        pos = name.rfind("[")
        if pos != -1:
            idx = name[pos+1:-1]
            nname = name[0:pos]
    return int(idx), nname
