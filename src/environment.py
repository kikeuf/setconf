
import os
from sys import platform
from settings import write_env_file, read_env_file



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

        #cfg.writefile(varname, value, True)
        write_env_file(varname, value)
        return True

   except Exception as e:
       return "error : " + repr(e)

def getenvvar(varname):
    try:
        #value=os.environ[varname]
        value = os.environ.get(varname)
        if value == None:
            #value = cfg.readfile(varname)
            value = read_env_file(varname)
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
