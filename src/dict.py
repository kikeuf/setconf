import settings as cfg

def getnodeValuebyXPath(root, path):
    ret = getnodebyXPath(root, path)
    if ret[1] is None:
        return str(ret[0])
    else:
        return ret[1]

def getnodeObjectbyXPath(root, path):
    ret = getnodebyXPath(root, path)
    return ret[0]
def getnodebyXPath(root, path, ForceNodeCreation = False):

    npath = XPathToDictPath(path)

    items = path.split('/')
    nNode = root
    id = -1
    for item in items:
        if item != '':
            idnNode = getchildnode(nNode, item, npath, ForceNodeCreation)
            id = idnNode[0]
            nNode = idnNode[1]
            pNode = idnNode[2]
            name = idnNode[3]
            npath = reduceXPath(npath)

    if id != -1:
        arrayvalue = nNode[id]
        return nNode, arrayvalue, pNode, name
    else:
        return nNode, None, pNode, name

def setnodeValuebyXPath(root, path, value, ForceNodeCreation = False):

    try:
        ret = getnodebyXPath(root, path, ForceNodeCreation)
        id = ret[1]
        nNode = ret[0]
        pNode = ret[2]
        name = ret[3]

        #pNode[name].Append = "test"
        if not (pNode is None):
            #nNode = value

            #print(cfg.arg_action)
            match cfg.arg_action:
                case "update":
                    pNode[name] = formatNumberOrText(value)
                case "append":
                    if isinstance(pNode[name], list):
                        pNode[name].append(formatNumberOrText(value))
                    else:
                        #Conversion de l'élément en liste
                        ovalue = ''
                        if not (pNode[name] is None):
                            ovalue = str(pNode[name])
                        if ovalue == '':
                            ls = {1: formatNumberOrText(value)}
                        else:
                            ls = {1: formatNumberOrText(ovalue), 2: formatNumberOrText(value)}
                        lst = list(ls.values())
                        pNode[name] = lst
                case "remove":
                    del pNode[name]

            return True
        else:
            return False

        #return pNode[name]

    except:
        return None

def getchildnode(parentnode, name, dictpath = "", ForceNodeCreation = False):

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
        return id, cnode, parentnode, name

    except KeyError as ek:
        if ForceNodeCreation:
            try:
                #if isinstance(parentnode, list):
                #    parentnode.append(name)
                #else:
                #    parentnode[name] = None

                #tag = eval("{'"+name+"': {'id': None}}")
                tag = eval(dictpath)
                parentnode.update(tag)

                #parentnode[name] = eval("{'element': 'vide' }")
                return -1, parentnode[name], parentnode, name

            except Exception as ek2:
                #print(repr(ek2))
                return -1, None, None, ""
    except:
        return -1, None, None, ""

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


def XPathToDictPath(path):

    ret = "{'"
    end = "}"
    items = path.split('/')

    for item in items:
        if item != '':
            ret += item + "': {'"
            end += "}"
    ret += "'" + end

    ret = ret.replace("{''}", 'None')

    return ret

def reduceXPath(path):
    pos = path.find(": ", 0)
    return path[pos+2:-1]

def formatNumberOrText(value):
    try:
        type = ""
        ret = value

        f = float(value)
        type = "float"
        ret = f

        i = int(value)
        type = "int"
        ret = i

        return ret

    except:

        if type == "":
            type = "str"
            lret = ret.lower()
            match lret:
                case 'yes' | 'true':
                    type = "boolean"
                    return True
                case 'no' | 'false':
                    type = "boolean"
                    return False

        return ret
def testdict():

    datas = "{'network': {'ethernets': {'enp1s0': {'addresses': ['163.173.228.1/22'], 'dhcp4': 'no'}}, 'renderer': 'networkd', 'version': 2}}"
    #newdata =

    datas="{'network': {'ethernets': { 'enp1s0': {'addresses': ['163.173.228.1/22', '10.0.0.1/24'], 'addresses2': ['163.173.228.1/22', '10.0.0.1/24'], 'dhcp4': False, 'test': {'test2': 'rien'}}}, 'renderer': 'networkd', 'version': 2}}"

    #marks = {'Physics': 67, 'Maths': 87}
    #internal_marks = eval("{'Practical': 48 }")
    dict=eval(datas)

    #marks.update(internal_marks)

    #print(marks)


    path = "/network/ethernets/enp1s0/aaaa/bbbb/cccc"

    ret = setnodeValuebyXPath(dict, path, 'noquote', True)
    print(dict)


    # Output: {'Physics': 67, 'Maths': 87, 'Practical': 48}
