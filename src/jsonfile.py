import json

from dictpath_main import get_dict_item, update_dict_element, write_new_dict_element, convertXpathToDictPath, \
    convertXpathToDictVariable
from dictpath_utils import validate_dict_path


#https://github.com/StephenDiscenza/jsonpath-lite-for-python


def readjson(filename, path, variable):

    try:
        with open(filename, 'r') as f:
            DATA = json.load(f)

        #path = '/menu/popup/menuitem[value="Open"].onclick'
        fullpath = convertXpathToDictPath(path + '/' + variable)
        #path = convertXpathToJsonPath(path)
        #print(path)
        #path = '$.menu.popup.menuitem[?value="Open"].onclick'
        #path = '$.menu.popup.menuitem[?0].onclick'
        #expected_result = True
        #assert get_json_item(DATA, path) == expected_result, f'Did not find {str(expected_result)} at {path}'
        ret = get_dict_item(DATA, fullpath)
        return ret

    except:
        return ""


    #path = '/menu/popup/menuitem/0/value'

    #jsonObject = open(filename, "r")
    #jsonContent = jsonObject.read()
    #obj_python = json.loads(jsonContent)


    #pa = (path+'/'+variable).split('/')
    #obj = obj_python
    #for p in pa:
    #    if p != '':
    #        try:
    #            obj = obj[p]
    #        except TypeError:
    #            obj = obj[int(p)-1]
                #id = int(p) - 1
                #if id > 0:
                #    obj = obj[id]

    #return(obj)

    #obj = obj_python['menu']
    #print(obj)
    #obj2 = obj['popup']
    #print('obj2:')
    #print(obj2)
    #for o in obj:
    #    print(o)
    #print(obj_python['menu']['popup']['menuitem'][1])
    #print(obj_python['menu']['popup']['menuitem'][1])


def writejson(filename, path, variable, value, new_element=False, new_array_field=False):

    with open(filename, 'r') as f:
        DATA = json.load(f)

    #path = '/menu/popup/menuitem[value="Open"].onclick'
    fullpath = convertXpathToDictPath(path + '/' + variable)
    parentpath = convertXpathToDictPath(path)
    arrayvar = convertXpathToDictVariable(variable, value)

    #print(path)
    #path = '$.menu.popup.menuitem[?value="Open"].onclick'
    #path = '$.menu.popup.menuitem[?0].onclick'
    #expected_result = True
    #assert get_json_item(DATA, path) == expected_result, f'Did not find {str(expected_result)} at {path}'

    if validate_dict_path(fullpath)[0] and not new_element:
        ret = update_dict_element(DATA, fullpath, value)
    elif new_array_field:
        ret = write_new_dict_element(DATA, parentpath, arrayvar)
    else:
        ret = write_new_dict_element(DATA, parentpath, value, variable)

    with open(filename, "w") as jsonfile:
        json.dump(DATA, jsonfile, indent=2)

    return ret


def createjsontest():
    article_info = {"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}
    }
    #myjson = json.dumps(article_info)

    #with open("d:\config.json", "w") as jsonfile:
    #    jsonfile.write(myjson)

    with open("d:\config.json", "w") as jsonfile:
        json.dump(article_info, jsonfile, indent=2)
       #print("Write successful")


