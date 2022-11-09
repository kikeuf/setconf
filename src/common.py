import environment as env
import re

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