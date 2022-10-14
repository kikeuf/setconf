import sys
from os.path import exists as file_exists

import environment as env
# from settings import *
import settings as cfg


def translate_args():
    #-w - t yaml - f "d:\tutswiki.yaml" - p Details2 "domain2" "www.toto.org"
    #global arg_command
    #global arg_filetype
    #global arg_conffile
    #global arg_section_path
    #global arg_variable
    #global arg_value
    #global default_env

    try:

        helpmode = False

        args=[]
        argcount=len(sys.argv)
        for i, arg in enumerate(sys.argv):
            args.append(arg)

        a=1
        while a<argcount:
            #print(a)

            if args[a]=="-r": #read
                if cfg.arg_command == "":
                    cfg.arg_command = "read"
                else:
                    return "error: conflicted arguments between read and write mode"
            elif args[a]=="-w": #write
                if cfg.arg_command == "":
                    cfg.arg_command = "write"
                else:
                    return "error: conflicted arguments between read and write mode"

            elif args[a]=="-n": #new tag
                cfg.arg_newtag = True

            #elif args[a]=="-c": #change
            #    if cfg.arg_command == "":
            #        cfg.arg_command = "replace"
            #    else:
            #        return "error: conflicted arguments between read, write and replace mode"
            elif args[a] == "-t": #type
                if cfg.arg_filetype == "":
                    a = a + 1
                    cfg.arg_filetype = args[a].lower()
                    if cfg.arg_filetype!="json" and cfg.arg_filetype!="xml" and cfg.arg_filetype!="conf" and cfg.arg_filetype!="yaml" and cfg.arg_filetype!="text":
                        return "error: unknown file type"
                else:
                    return "error: conflicted arguments for file type"
            elif args[a] == "-f": #filename
                if cfg.arg_conffile == "":
                    a = a + 1
                    cfg.arg_conffile = args[a]
                    if cfg.arg_conffile == "":
                        return "error: configuration file not specified"
                else:
                    return "error: conflicted arguments for configuration file"
            elif args[a] == "-p": #path or section
                if cfg.arg_section_path == "":
                    a = a + 1
                    cfg.arg_section_path = args[a]
                    #pas d'erreur car il peut être vide
                    #if cfg.arg_section_path == "":
                    #    return "error: path of the variable not specified"
                else:
                    return "error: conflicted arguments for configuration file"
            elif args[a] == "-v": #variable
                if cfg.arg_variable == "":
                    a = a + 1
                    cfg.arg_variable = args[a]
                else:
                    return "error: conflicted arguments for variable name"
            elif args[a] == "-d": #data
                if cfg.arg_value == "":
                    a = a + 1
                    cfg.arg_value = args[a]
                else:
                    return "error: conflicted arguments for value"
            elif args[a] == "-e": #environment variable
                if cfg.arg_envvar == "":
                    a = a + 1
                    cfg.arg_envvar = args[a]
                else:
                    return "error: conflicted arguments for environment variable name"
            #elif args[a] == "-i": #index de liste
            #    if cfg.arg_listindex == -9999:
            #        a = a + 1
            #        cfg.arg_listindex = args[a]
            #    else:
            #        return "error: conflicted arguments for index of list"
            elif args[a] == "-h":
                helpmode = True
                cfg.showhelp()
            #else:
            #    return "error: bad argument"
            a = a + 1


        if cfg.arg_command=="write":
            if cfg.arg_value == "":
                cfg.arg_value = args[argcount-1]
            if cfg.arg_variable == "":
                cfg.arg_variable = args[argcount-2]
        elif cfg.arg_command == "read":
            if cfg.arg_variable == "":
                cfg.arg_variable = args[argcount-1]
        #else:
        #    cfg.arg_value = args[argcount-1]

        #print(cfg.arg_command)

        #Set default values if not set in command line
        if cfg.arg_command == "":
            cfg.arg_command = "read"

        if cfg.arg_filetype == "":
            cfg.arg_filetype = "conf"

        if cfg.arg_envvar == "":
            cfg.arg_envvar = cfg.default_env

        #if cfg.arg_listindex == -9999:
        #    cfg.arg_listindex = cfg.default_listindex

        # Translate code to text
        if cfg.arg_value == "$":
            cfg.arg_value = env.getenvvar(cfg.arg_envvar)
        elif cfg.arg_value[0:1] == "$":
            cfg.arg_value = env.getenvvar(cfg.arg_envvar[1:])

        #Détection des variables non renseignées et fichiers inexistants
        if helpmode:
            return ""

        if cfg.arg_section_path == "" and cfg.arg_filetype != "conf" and cfg.arg_filetype != "text":
            return "error: section or path is not specified"

        if cfg.arg_variable == "" and cfg.arg_filetype != "text":
            return "error: variable name is not specified"

        if cfg.arg_value == "" and cfg.arg_command == "write":
            return "error: value is not specified"

        if cfg.arg_conffile == "":
            return "error: configuration file is not specified"

        if not file_exists(cfg.arg_conffile):
            return "error: configuration file cannot be found"

    except Exception as ex:
        if hasattr(ex, 'message'):
            msg = str(ex.message)
        else:
            msg = str(ex)
        return "error: " + msg
