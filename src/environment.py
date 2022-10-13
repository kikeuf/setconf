
import os

def setenvvar(varname, value):
   try:
       os.environ[varname]=value
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