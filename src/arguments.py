import sys
from common import fileexists, createfile, trim

import environment as env
# from settings import *
import settings as cfg

#data = ""
#quote_symbol = ""

def translate_args():
    #-w - t yaml - f "d:\tutswiki.yaml" - p Details2 "domain2" "www.toto.org"
    #global arg_command
    #global arg_filetype
    #global arg_conffile
    #global arg_section_path
    #global arg_variable
    #global arg_value
    #global default_env

    #data = ""

    Doinit = False

    try:

        helpmode = False

        args = []
        argcount=len(sys.argv)
        for i, arg in enumerate(sys.argv):
            args.append(arg)

        a = 1
        while a < argcount:
            #print(a)

            if args[a] == "-r": #read
                if cfg.arg_command == "":
                    cfg.arg_command = "read"
                else:
                    return "error: conflicted arguments between read and write mode"
            elif args[a] == "-w": #write
                if cfg.arg_command == "":
                    cfg.arg_command = "write"
                else:
                    return "error: conflicted arguments between read and write mode"

            elif args[a] == "-n": #new tag
                cfg.arg_newtag = True

            #elif args[a]=="-c": #change
            #    if cfg.arg_command == "":
            #        cfg.arg_command = "replace"
            #    else:
            #        return "error: conflicted arguments between read, write and replace mode"
            elif args[a] == "-t": #type
                if a + 1 < argcount:
                    if cfg.arg_filetype == "":
                        a = a + 1
                        cfg.arg_filetype = args[a].lower()
                        if cfg.arg_filetype != "json" and cfg.arg_filetype != "xml" and cfg.arg_filetype != "conf" and cfg.arg_filetype != "yaml" and cfg.arg_filetype != "text" and cfg.arg_filetype != "yaml2" and cfg.arg_filetype != "dhcp":
                            return "error: unknown file type"
                    else:
                        return "error: conflicted arguments for file type"
            elif args[a] == "-a": #action
                if a + 1 < argcount:
                    if cfg.arg_action == "":
                        a = a + 1
                        cfg.arg_action = args[a].lower()
                        if cfg.arg_action != "update" and cfg.arg_action != "append" and cfg.arg_action != "remove" and cfg.arg_action != "count":
                            return "error: unknown action"
                    else:
                        return "error: conflicted arguments for action"
            elif args[a] == "-f": #filename
                if a + 1 < argcount:
                    if cfg.arg_conffile == "":
                        a = a + 1
                        #data = args[a]
                        ret = argument_workaround(args, a, argcount)
                        a = ret[0]
                        cfg.arg_conffile = ret[1]
                        #cfg.arg_conffile = data
                        if cfg.arg_conffile == "":
                            return "error: configuration file not specified"
                    else:
                        return "error: conflicted arguments for configuration file"
            elif args[a] == "-p": #path or section
                if a + 1 < argcount:
                    if cfg.arg_section_path == "":
                        a = a + 1
                        ret = argument_workaround(args, a, argcount)
                        a = ret[0]
                        cfg.arg_section_path = ret[1]
                        #data = args[a]
                        #a = argument_workaround(args, a, argcount)
                        #cfg.arg_section_path = data
                        #pas d'erreur car il peut ??tre vide
                        #if cfg.arg_section_path == "":
                        #    return "error: path of the variable not specified"
                    else:
                        return "error: conflicted arguments for configuration file"
            elif args[a] == "-k": #key (variable)
                if a + 1 < argcount:
                    if cfg.arg_variable == "":
                        a = a + 1
                        ret = argument_workaround(args, a, argcount)
                        a = ret[0]
                        cfg.arg_variable = ret[1]
                        #data = args[a]
                        #a = argument_workaround(args, a, argcount)
                        #cfg.arg_variable = data
                    else:
                        return "error: conflicted arguments for variable name"
            elif args[a] == "-v": #value
                if a + 1 < argcount:
                    if cfg.arg_value == "":
                        a = a + 1
                        ret = argument_workaround(args, a, argcount)
                        a = ret[0]
                        cfg.arg_value = ret[1]
                        #data = args[a]
                        #a = argument_workaround(args, a, argcount)
                        #cfg.arg_value = data
                    else:
                        return "error: conflicted arguments for value"
            #elif args[a] == "-e": #environment variable
            #    if a + 1 < argcount:
                #    if cfg.arg_envvar == "":
                #        a = a + 1
                #        cfg.arg_envvar = args[a]
                #    else:
                #        return "error: conflicted arguments for environment variable name"
            #elif args[a] == "-i": #index de liste
            #    if a + 1 < argcount:
                #    if cfg.arg_listindex == -9999:
                #        a = a + 1
                #        cfg.arg_listindex = args[a]
                #    else:
                #        return "error: conflicted arguments for index of list"
            elif args[a] == "-h":
                helpmode = True
            elif args[a] == "-l" and a + 1 < argcount:
                a = a + 1
                if args[a] != "":
                    cfg.arg_delimiters = args[a]

            elif args[a] == "-nospace":
                cfg.arg_space_around_delimiters = False

            elif args[a] == "-ip": #ip_address
                if a + 1 < argcount:
                    if cfg.arg_ipaddress == "":
                        a = a + 1
                        cfg.arg_ipaddress = args[a]
                    else:
                        return "error: conflicted arguments for ip address"

            elif args[a] == "-mask": #netmask
                if a + 1 < argcount:
                    if cfg.arg_netmask == "":
                        a = a + 1
                        cfg.arg_netmask = args[a]
                    else:
                        return "error: conflicted arguments for netmask"

            elif args[a] == "-mac": #mac_address
                if a + 1 < argcount:
                    if cfg.arg_macaddress == "":
                        a = a + 1
                        cfg.arg_macaddress = args[a]
                    else:
                        return "error: conflicted arguments for MAC address"

            elif args[a] == "-host": #hostname
                if a + 1 < argcount:
                    if cfg.arg_hostname == "":
                        a = a + 1
                        cfg.arg_hostname = args[a]
                    else:
                        return "error: conflicted arguments for hostname"

            elif args[a] == "-server": #next-server
                if a + 1 < argcount:
                    if cfg.arg_server == "":
                        a = a + 1
                        cfg.arg_server = args[a]
                    else:
                        return "error: conflicted arguments for next server"

            elif args[a] == "-group": #DHCP groupname
                if a + 1 < argcount:
                    if cfg.arg_dhcpgroup == "":
                        a = a + 1
                        cfg.arg_dhcpgroup = args[a]
                    else:
                        return "error: conflicted arguments for DHCP group"

            elif args[a] == "-boot": #boot file
                if a + 1 < argcount:
                    if cfg.arg_bootfile == "":
                        a = a + 1
                        cfg.arg_bootfile = args[a]
                    else:
                        return "error: conflicted arguments for ip address"

            elif args[a] == "-init": #initialisation
                Doinit = True

            #else:
            #    return "error: bad argument"
            a = a + 1

        #Force actions or values
        if Doinit:
            cfg.init()
            return ""

        if helpmode and cfg.arg_filetype == "dhcp":
            cfg.showhelp_dhcp()
            return ""
        elif helpmode:
            cfg.showhelp()
            return ""

        if cfg.arg_filetype == "dhcp":
            cfg.arg_command = "write"

        #if cfg.arg_command=="write":
        #    if cfg.arg_value == "":
        #        cfg.arg_value = args[argcount-1]
        #    if cfg.arg_variable == "":
        #        cfg.arg_variable = args[argcount-2]
        #elif cfg.arg_command == "read":
        #    if cfg.arg_variable == "":
        #        cfg.arg_variable = args[argcount-1]
        #else:
        #    cfg.arg_value = args[argcount-1]

        #print(cfg.arg_command)

        #Set default values if not set in command line
        if cfg.arg_command == "":
            cfg.arg_command = "read"

        if cfg.arg_filetype == "":
            cfg.arg_filetype = "conf"

        if cfg.arg_action == "":
            cfg.arg_action = "update"

        if cfg.arg_conffile == "" and cfg.arg_filetype == "dhcp":
            dhcpfile = "/etc/dhcp/dhcpd.conf"
            if fileexists(dhcpfile):
                cfg.arg_conffile = dhcpfile

        #if cfg.arg_envvar == "":
        #    cfg.arg_envvar = cfg.default_env

        #if cfg.arg_listindex == -9999:
        #    cfg.arg_listindex = cfg.default_listindex

        # Translate code to text
        if cfg.arg_value == "$":
            cfg.arg_value = env.getenvvar(default_env)
        elif cfg.arg_value[0:1] == "$":
            cfg.arg_value = env.getenvvar(cfg.arg_value[1:])

        if cfg.arg_variable[0:1] == "$":
            cfg.arg_variable = env.getenvvar(cfg.arg_variable[1:])

        if cfg.arg_conffile[0:1] == "$":
            cfg.arg_conffile = env.getenvvar(cfg.arg_conffile[1:])

        if cfg.arg_section_path[0:1] == "$":
            cfg.arg_section_path = env.getenvvar(cfg.arg_section_path[1:])

        #D??tection des variables non renseign??es et fichiers inexistants
        #if helpmode:
        #    return ""

        if cfg.arg_filetype == "dhcp":

            if cfg.arg_dhcpgroup == "":
                return "error: dhcp group is not specified"

            if cfg.arg_hostname == "":
                return "error: hostname is not specified"

            if cfg.arg_macaddress and cfg.arg_ipaddress == "":
                return "error: at least an IP address or a MAC address must be specified"

        else:

            if cfg.arg_section_path == "" and cfg.arg_filetype != "conf" and cfg.arg_filetype != "text":
                return "error: section or path is not specified"

            if cfg.arg_variable == "" and cfg.arg_filetype != "text":
                return "error: variable name is not specified"

            #if cfg.arg_value == "" and cfg.arg_command == "write":
            #    return "error: value is not specified"



        if cfg.arg_conffile == "":
            return "error: configuration file is not specified"
        elif not fileexists(cfg.arg_conffile):
            ret = createfile(cfg.arg_conffile)
            if not ret:
                return "error: configuration file cannot be found"

    except Exception as ex:
        if hasattr(ex, 'message'):
            msg = str(ex.message)
        else:
            msg = str(ex)
        return "error: " + msg

def argument_workaround(arg_list, a, max):

    # contournement de bug de lecture des arguments sous linux quand ils comprennent des espaces

    data = ''
    exit_loop = False
    i = a
    while not exit_loop:

        if i < max:

            pdata = data
            ret = concat_arguments(arg_list[i], data)
            cont = ret[0]
            data = ret[1]

            if cont:
                i += 1
            elif data == pdata:
                i -= 1
                exit_loop = True
            else:
                exit_loop = True

            #if data == pdata:
            #    i = i - 1
            #    exit_loop = True
            #else:
            #    pdata = data
            #    exit_loop = False


                #ch1 = arg_list[i][0]
                #if ch1 == "-":
                #    exit_loop = True
                #    i = i - 1
                #else:
                #    data = data + ' ' + arg_list[i]
        else:
            exit_loop = True
    return i, data

def concat_arguments(curValue, leftPart):

    #d??claration de variable statique
    if not hasattr(concat_arguments, "quote_symbol"):
        concat_arguments.quote_symbol = ""

    #global quote_symbol
    cont = False
    _leftPart = leftPart
    first_char = curValue[0]
    last_char = curValue[-1]
    data = ''

    # Cas du d??but de texte ?? l'int??rieur de quotes
    if _leftPart == '' and is_quote(first_char):
        data = curValue
        concat_arguments.quote_symbol = first_char
        if last_char == concat_arguments.quote_symbol:
            data = remove_quotes(data)
            cont = False
        else:
            cont = True

    # cas du dernier ??l??ment de la suite cloturant la quote
    elif last_char == concat_arguments.quote_symbol and concat_arguments.quote_symbol != '':
        data = remove_quotes(trim(_leftPart + ' ' + curValue))
        cont = False

    # Cas de la suite de texte ?? l'int??rieur de quotes
    elif concat_arguments.quote_symbol != '':
        data = trim(_leftPart + ' ' + curValue)
        cont = True

    # Cas d'une balise - en dehors des quotes
    elif first_char == "-":
        if _leftPart == '':
            data = curValue
        else:
            data = _leftPart

        concat_arguments.quote_symbol = ""
        cont = False

    #Cas d'une donn??e en dehors des quotes
    else:
        data = trim(_leftPart + ' ' + curValue)
        concat_arguments.quote_symbol = ""
        cont = True


    #if _leftPart == '':
    #    _leftPart = curValue

    #_leftPart = remove_quotes(_leftPart)

    if not cont:
        concat_arguments.quote_symbol = ""

    return cont, data

def remove_quotes(mystring):

    try:
        if is_quote(mystring[0]):
            mystring = mystring[1:]

        if is_quote(mystring[-1]):
            mystring = mystring[:-1]

        return mystring

    except:

        return mystring

def is_quote(mychar):


    if mychar == chr(34) or mychar == chr(39):
        return True
    else:
        return False
