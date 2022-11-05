
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
import re

# import sys
from dictpath_main import get_dict_item, update_dict_element, write_new_dict_element, convertXpathToDictPath, \
    convertXpathToDictVariable
from dictpath_utils import validate_dict_path
from settings import removeblanklines
from dict import getnodeValuebyXPath, getnodeObjectbyXPath, setnodeValuebyXPath, countnodeListbyXPath
from journal import log


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

    except Exception as e:
        log('Setconf error : ' + repr(e))
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

def countyamlelements(filename, path):

    try:

        with open(filename, "r") as yamlfile:
            DATA = yaml.load(yamlfile, Loader=yaml.FullLoader)

        cnt = countnodeListbyXPath(DATA, path)
        return cnt

    except:

        return 0
def writeyaml(filename, path, variable, value, new_element=False, new_array_field=False, action='update'):

    try:

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
            yaml.dump(DATA, yamlfile, default_style=None, default_flow_style=False)
            #yamlfile.close()
            #lines = [line.strip() for line in file.readlines() if len(line.strip()) != 0]

            removeblanklines(filename)

        return ret

    except Exception as e:
        log('Setconf error : ' + repr(e))
        return False


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


def writeyamlalternate(yamlfile, xpath, variable, value):

    try:

        with open(yamlfile, 'r') as file:
            lines = file.readlines()

        with open(yamlfile, 'r') as file:
            content = file.read()

        lines = createsection(lines, xpath, variable, value)

        #if not sectionexists(yamlfile, xpath + '/' + variable):
        #    createsection(lines, xpath, variable, value)

        newcontent = yamlchangevalue(lines, xpath + '/' + variable, value)

        if newcontent != '' and newcontent != content:
            with open(yamlfile, 'w') as file:
                file.write(newcontent)
        else:
            return False

        return True

    except Exception as e:
        log('Setconf error : ' + repr(e))
        return False

def getdeepersection(yamllines, xpath):

    elements = xpath.split('/')
    i = 0
    max = len(elements)
    line_count = 0
    insert_line = -1
    pindent = ''
    pindent_len = 0
    valid_path = ''


    for line in yamllines:
        line_count += 1
        if elements[i] == '':
            i += 1
        el = elements[i] + ":"
        pos = line.find(el)
        cindent = getindent(line)
        cindent_len = len(cindent)
        if cindent_len <= pindent_len and valid_path != '' and pindent_len != 0:
            return insert_line, pindent, valid_path
        elif pos != -1:
            valid_path += '/' + elements[i]
            pindent = cindent
            pindent_len = cindent_len
            insert_line = line_count
            i += 1
            if i == max:
                return 0, pindent, valid_path

    return insert_line, pindent, valid_path

def createsection(yamllines, xpath, variable, value):

    fpath = xpath + '/' + variable
    ret = getdeepersection(yamllines, fpath)
    idx = ret[0]
    pindent = ret[1]
    valid_path = ret[2]

    if idx <= 0:
        return yamllines

    missing_path = getstringafter(fpath, valid_path)
    missings = missing_path.split('/')

    cnt = 0
    max = len(missings)
    for missing in missings:
        cnt += 1

        if missing != '':
            idt = getindent(yamllines[idx])
            if len(idt) > len(pindent):
                pindent = idt
            else:
                pindent += '  '
            if cnt == max:
                yamllines.insert(idx, pindent + missing + ": " + value + '\n')
                return yamllines
            else:
                yamllines.insert(idx, pindent + missing + ":" + '\n')
                idx += 1

    return yamllines

def yamlchangevalue(yamllines, xpath, value):

    elements = xpath.split('/')
    i = 0
    found = False
    ntext = ""
    nline = ""
    max = len(elements)
    line_count = 0
    buf_value = ""
    buf_insertline = -1

    for line in yamllines:
        line_count += 1
        if elements[i] == '':
            i += 1
        el = elements[i] + ":"
        pos = line.find(el)
        indent = line[0:pos]
        if pos != -1 and not found:
            i += 1
            if i == max:
                found = True
                i = 0
                rvalue = getstringafter(line, el).strip()
                if rvalue.strip() == "|":
                    #C'est une chaine de caractères sur plusieurs lignes, dans ce cas on ignore la mise à jour
                    nline = line
                elif rvalue != '':
                    nline = indent + el + ' ' + value + '\n'
                else:
                    # on vérifie s'il s'agit d'une liste, auquel cas on ajoute la valeur en fin de liste
                    ret = countlistlines(yamllines, line_count)
                    if ret[0] > 0:
                        buf_value = ret[1] + "- " + value + '\n'
                        buf_insertline = line_count + ret[0]

                    nline = line
            else:
                nline = line
        else:
            nline = line

        ntext += nline
        if line_count == buf_insertline and buf_value != '':
            ntext += buf_value

    #print(ntext)
    return ntext

def getstringafter(mystring, matchstring):

    match = (re.search(matchstring, mystring))

    if match != None:

        # getting the starting index using match.start()
        pos_s = match.start()
        pos_e = pos_s + len(matchstring)

        return mystring[pos_e:]

        # Getting the start and end index in tuple format using match.span()
        #print("start and end index", match.span())

    else:
        return ''

def countlistlines(lines, index):

    try:

        e_cnt = 0
        c_cnt = 0
        end_of_list = False
        i = index
        idt = ''

         while not end_of_list:
            mstr=lines[i].strip()
            if len(mstr) > 0:
                char = mstr[0]
                match char:
                    case '-':
                        if e_cnt == 0:
                            idt = getindent(lines[i])
                        e_cnt += 1
                        i += 1
                    case '#':
                        c_cnt += 1
                        i += 1
                    case _:
                        end_of_list = True
                if i >= len(lines):
                    end_of_list = True
            else:
                end_of_list = True

        if e_cnt == 0:
            return 0
        else:
            return e_cnt + c_cnt, idt

    except:
        return -1

def getindent(mystring):

    idt = ''
    for ch in mystring:
        if ch == ' ':
            idt += ' '
        else:
            return idt

    return idt

