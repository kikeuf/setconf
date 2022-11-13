import environment as env
import re
from os.path import exists

#-------------------------------------------------
# Environnement files
#-------------------------------------------------

def create_env_file():
    if env_section == "":
        writefile(env_file, '', True)
    else:
        writefile(env_file, '[' + env_section + ']', True)

def write_env_file(env_name, value):

    if not os.path.exists(env_file):
        create_env_file()

    return writeconf(env_file, env_section, env_name, value)

def read_env_file(env_name):
    return readconf(env_file, env_section, env_name)

#-------------------------------------------------
# File manipulation
#-------------------------------------------------

def fileexists(filename):
    return exists(filename)

def createfile(filename):
    try:
        file = open(filename, "x")
        return True
    except:
        return False

def writefile(filename, text, erase_before=False):

    try:

        if erase_before:
            deletefile(filename)

        f = open(filename, 'w')
        # Writing a string to file
        f.write(text)
        f.close()

        return True

    except:
        return False

def deletefile(filename):

    try:
        os.remove(filename)
        return True

    except:
        return False

def readfile(filename):

    try:
        f = open(filename, 'r')
        ret = f.readline()
        return ret

    except:
        return ""

def readfilecontent(filename):

    data = ""
    if os.path.isfile(filename):
        file = open(filename, "r")
        data = str(file.read())
        file.close()

    return data

def writelisttofile(Filename, MyList):

    text = ""
    for lst in MyList:
        text += lst   # + '\n'

    writefile(Filename, text, True)

def removeblanklines(filename):
    with open(filename) as reader, open(filename, 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
        writer.truncate()

#-------------------------------------------------
# Data formatting and search
#-------------------------------------------------

def isnumber(value):
    try:
        ret = int(value)
        return True
    except:
        return False

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

def trim(mystring):

    result = re.sub(r'^\s+|\s+$', '', mystring)
    return result

def getchar(mystring, index):

    try:
        ch = mystring[index]
        return ch
    except:
        return ''

def substring(mystring, start, end):

    try:
        xstr = mystring[start:end]
        return xstr
    except:
        return ''

def clean_array(myarray):

    try:

        arr1 = []  # initialization
        for ar in myarray:
            if ar != '':
                arr1.append(ar)

        return arr1

    except:
        return myarray

#-------------------------------------------------
# XPATH manipulations
#-------------------------------------------------
def get_xpath_index(xpath):

    try:

        if xpath[-1] == ']':
            le = len(xpath)
            for x in range(1, le-1):
                y = le-x
                ch = getchar(xpath, y)
                if ch == "[":
                    val = substring(xpath, y+1, le-1)
                    n_xpath = substring(xpath, 0, y)
                    if isnumber(val):
                        return int(val), n_xpath
                    break
        return 0, xpath

    except:
        return 0, xpath

def get_parent_xpath(xpath):

    try:

        le = len(xpath)
        for x in range(1, le - 1):
            y = le - x
            ch = getchar(xpath, y)
            if ch == "/":
                val = substring(xpath, 0, y)
                val2 = substring(xpath, y+1, le)
                return val, val2
                break

        return '', xpath

    except:

        return '', xpath
