
import os
from sys import platform

def setenvvar(varname, value):
   try:

        if platform == "linux" or platform == "linux2":
            #os.system('export ' + varname + '=' + value)
            os.environ.setdefault(varname, value)
        else:
            os.environ.setdefault(varname, value)
            # os.environ[varname] = value

        #rvalue = os.environ.get(varname)
        #print('check: $' + varname + '=' + rvalue)

        writefile(varname, value)
        return True

   except Exception as e:
       return "error : " + repr(e)

def getenvvar(varname):
    try:
        #value=os.environ[varname]
        value = os.environ.get(varname)
        if value == "":
            value = readfile(varname)
        return value

    except Exception:
        return ""

def envvarexists(varname):
    try:
        if varname in os.environ:
            return True
        else:
            return False

    except Exception:
        return False

def writefile(filename, text, erase_before = False):

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
