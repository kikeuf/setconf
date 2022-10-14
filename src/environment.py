
import os
from sys import platform

def setenvvar(varname, value):
   try:

        print('set: $' + varname + '=' + value)


        if platform == "linux" or platform == "linux2":
            os.system('export ' + varname + '=' + value)
        else:
            os.environ.setdefault(varname, value)
            # os.environ[varname] = value

        rvalue = os.environ.get(varname)
        print('check: $' + varname + '=' + rvalue)

        return True

   except Exception:
       return False


def getenvvar(varname):
    try:
        #value=os.environ[varname]
        value = os.environ.get(varname)
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