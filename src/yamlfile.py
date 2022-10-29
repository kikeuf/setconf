
#For reading and writing to the YAML file, we first need to install the PyYAML package by using the following command.
#pip install pyyaml

#https://python.land/data-processing/python-yaml

#import yaml
#import ruamel.yaml as yaml
import json
#import sys
#from dictpath_main import get_dict_item, update_dict_element, write_new_dict_element, convertXpathToDictPath, convertXpathToDictVariable
#from dictpath_utils import validate_dict_path
#from settings import removeblanklines
# import ruamel.yaml as yaml

import json
import yaml

# import sys
from dictpath_main import get_dict_item, update_dict_element, write_new_dict_element, convertXpathToDictPath, \
    convertXpathToDictVariable
from dictpath_utils import validate_dict_path
from settings import removeblanklines
from dict import getnodeValuebyXPath, getnodeObjectbyXPath, setnodeValuebyXPath


#from pathlib import Path

def createyamltest():

    article_info = [
        {
            'Details': {
                'domain': 'www.tutswiki.com',
                'language': 'python',
                'date': '11/09/2020'
            }
        }
    ]
    fi='d:\config.yaml'
    with open(fi, 'w') as yamlfile:
        data = yaml.dump(article_info, yamlfile)
        #yamlfile.close()
        #print("Write successful")

def dumpyaml(filename,section):

    article_info = {
            section
        }
    with open(filename, 'w') as yamlfile:

        data = yaml.dump(article_info, yamlfile)
        yamlfile.close()
        #print('section dump')

def readyaml(filename, path, variable):

    try:

        with open(filename, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)

        #print(data)
        fullpath = convertXpathToDictPath(path + '/' + variable)
        ret = get_dict_item(data, fullpath)
        return ret

    except:
        return ""

def writeyaml_x(filename, path, variable, value, new_element=False, new_array_field=False):


    #yml = yaml.YAML()
    #yml.preserve_quotes = True
    #DATA = yml.load(filename)

    #print(DATA)

    with open(filename, "r") as yamlfile:
        DATA = yaml.load(yamlfile, Loader=yaml.FullLoader)

    fullpath = convertXpathToDictPath(path + '/' + variable)
    parentpath = convertXpathToDictPath(path)
    arrayvar = convertXpathToDictVariable(variable, value)
    #testval = DATA["autoinstall"]["ssh_keys"]["rsa_private"]
    #testval = getchildnode(DATA["autoinstall"], "version2", True)

    new_element = False
    new_array_field = True

    curNode = getnodeObjectbyXPath(DATA, "/autoinstall/apt/packages2", new_element)

    #with open(filename, 'w') as yamlfile:
    #    yaml.dump(DATA, yamlfile)
    #with open(filename, "r") as yamlfile:
    #    DATA = yaml.load(yamlfile, Loader=yaml.FullLoader)
    #print(str(DATA))

    curNode = getnodeObjectbyXPath(DATA, "/autoinstall/apt/packages2", False)

    #If the node wasn't found and the auto-creation was enabled, yaml must be reparsed to get the node
    #if curNode is None and new_element:
    #    curNode = getnodeObjectbyXPath(DATA, "/autoinstall/apt/packages2", False)
    #curNode = getnodeObjectbyXPath(DATA, path + '/' - variable, False)
    print(curNode)

    if new_array_field:
        curNode.append(value)
    else:
        curNode = value

    #curNodeValue = getnodeValuebyXPath(DATA, "/autoinstall/apt/packages[3]", False)
    #print(curNodeValue)

    #if validate_dict_path(fullpath)[0] and not new_element:
    #    ret = update_dict_element(DATA, fullpath, value)
    #elif new_array_field:
    #    ret = write_new_dict_element(DATA, parentpath, arrayvar)
    #else:
    #    ret = write_new_dict_element(DATA, parentpath, value, variable)

    with open(filename, 'w') as yamlfile:
        yaml.dump(DATA, yamlfile, default_flow_style=False, sort_keys=False)

    ret = True
    return ret
def writeyaml(filename, path, variable, value, new_element=False, new_array_field=False, action='update'):

    method = 2

    #yml = yaml.YAML()
    #yml.preserve_quotes = True
    #DATA = yml.load(filename)

    with open(filename, "r") as yamlfile:
        DATA = yaml.load(yamlfile, Loader=yaml.FullLoader)

    if method == 1:
        fullpath = convertXpathToDictPath(path + '/' + variable)
        parentpath = convertXpathToDictPath(path)
        arrayvar = convertXpathToDictVariable(variable, value)

        if validate_dict_path(fullpath)[0] and not new_element:
            ret = update_dict_element(DATA, fullpath, value)
        elif new_array_field:
            ret = write_new_dict_element(DATA, parentpath, arrayvar)
        else:
            ret = write_new_dict_element(DATA, parentpath, value, variable)
    else:
        ret = setnodeValuebyXPath(DATA, path + '/' + variable, value, True, action)

    #DATA=yaml.normalise(DATA)
    #yml.dump(DATA, filename)
    #yaml.default_flow_style = False
    with open(filename, 'w') as yamlfile:
        yaml.dump(DATA, yamlfile, default_flow_style=False)
        #yamlfile.close()
        #lines = [line.strip() for line in file.readlines() if len(line.strip()) != 0]

    #removeblanklines(filename)

    return ret


def readyaml2(filename, section, variable):

    try:

        with open(filename, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            #print(data)

            pa = (section + '/' + variable).split('/')
            obj = data
            for p in pa:
                if p != '':
                    try:
                        obj = obj[p]
                    except TypeError:
                        obj = obj[int(p)]
            #print(obj)

            #value = data[section][variable]

        return obj

    except Exception:
        return ""

def writeyaml2(filename, section, variable, value):

    try:

        if not sectionexists(filename, section):
            dumpyaml(filename, section)
            return False

        with open(filename, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            data[0][section][variable] = value
            yamlfile.close()

        with open(filename, 'w') as yamlfile:
            data1 = yaml.dump(data, yamlfile)
            yamlfile.close()

        return True

    except Exception:
        return False

def sectionexists(filename,section):
    try:
        with open(filename, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            s = data[0][section]
            yamlfile.close()

        return True

    except Exception:
        return False

def yamltojson(yamlfile, jsonfile):
    with open(yamlfile, 'r') as file:
        configuration = yaml.safe_load(file)

    with open(jsonfile, 'w') as json_file:
        json.dump(configuration, json_file)
