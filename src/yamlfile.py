
#For reading and writing to the YAML file, we first need to install the PyYAML package by using the following command.
#pip install pyyaml

#https://python.land/data-processing/python-yaml

import yaml
#import ruamel.yaml as yaml
import json
#import sys
from dictpath_main import get_dict_item, update_dict_element, write_new_dict_element, convertXpathToDictPath, convertXpathToDictVariable
from dictpath_utils import validate_dict_path
from settings import removeblanklines
# import ruamel.yaml as yaml
import json

import yaml

# import sys
from dictpath_main import get_dict_item, update_dict_element, write_new_dict_element, convertXpathToDictPath, \
    convertXpathToDictVariable
from dictpath_utils import validate_dict_path
from settings import removeblanklines


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


def writeyaml(filename, path, variable, value, new_element=False, new_array_field=False):


    #yml = yaml.YAML()
    #yml.preserve_quotes = True
    #DATA = yml.load(filename)

    #print(DATA)

    with open(filename, "r") as yamlfile:
        DATA = yaml.load(yamlfile, Loader=yaml.FullLoader)

    fullpath = convertXpathToDictPath(path + '/' + variable)
    parentpath = convertXpathToDictPath(path)
    arrayvar = convertXpathToDictVariable(variable, value)

    if validate_dict_path(fullpath)[0] and not new_element:
        ret = update_dict_element(DATA, fullpath, value)
    elif new_array_field:
        ret = write_new_dict_element(DATA, parentpath, arrayvar)
    else:
        ret = write_new_dict_element(DATA, parentpath, value, variable)

    #DATA=yaml.normalise(DATA)
    #yml.dump(DATA, filename)

    with open(filename, 'w') as yamlfile:
        yaml.dump(DATA, yamlfile)
        #yamlfile.close()
        #lines = [line.strip() for line in file.readlines() if len(line.strip()) != 0]

    removeblanklines(filename)

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
