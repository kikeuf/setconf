
import os
from conffile import writeconf, readconf, writetext
from sys import platform
import environment as env

    # montage variable commune déjà existantes en public
    #global arg_command
    #global arg_filetype
    #global arg_conffile
    #global arg_section_path
    #global arg_variable
    #global arg_value
    #global default_env

arg_command = ""  # read, write
arg_filetype = ""  # type of file "conf","json","yaml","xml", "text"
arg_action = "" #action to realize with the variable and its value, "update", "append", "remove"
arg_conffile = ""  # full file name of the config file
arg_section_path = ""  # Section name or XML path or json path (without variable name)
arg_variable = ""  # Name of the variable
arg_value = ""  # value relative to the variable
#arg_envvar = ""  # name of environment variable to use
arg_newtag = False  #Add new tag in XML, Json or yaml even if tag already exists (list)
arg_delimiters = "=,:"  #Change delimiters for conf files
arg_space_around_delimiters = True #Add space before and after the delimiter in conf files

arg_bootfile = ""
arg_dhcpgroup = ""
arg_hostname = ""
arg_macaddress = ""
arg_ipaddress = ""
arg_netmask = ""
arg_server = ""

#arg_listindex=-9999 #Index of the item to read or write in a list
default_env = "SETCONF_ENV"

#env_file = "env.conf"
#env_section = "environment_variables"
#default_listindex = 1

def print_args():
    print("command : " + arg_command)
    print("filetype : " + arg_filetype)
    print("filename : " + arg_conffile)
    print("section : " + arg_section_path)
    print("variable : " + arg_variable)
    print("value : " + arg_value)
    print("delimiters : " + arg_delimiters)
    print("no space around delimiters : " + arg_space_around_delimiters)
    print("force new tag : " + arg_newtag)
    #print("environment variable : " + arg_envvar)

def removeblanklines(filename):
    with open(filename) as reader, open(filename, 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
        writer.truncate()

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

import os

def readfilecontent(filename):

    data = ""
    if os.path.isfile(filename):
        file = open(filename, "r")
        data = str(file.read())
        file.close()

    return data

def isnumber(value):
    try:
        ret = int(value)
        return True
    except:
        return False

def writelisttofile(Filename, MyList):

    text=""
    for lst in MyList:
        text += lst   # + '\n'

    writefile(Filename, text, True)

def showhelp():
    print("setconf [-r][-w] [-a action] [-t type_of_file] -f filename [-p path_of_variable] [–k variable] [-v value] [-l list_of_delimiters] [-nospace] [-n] [-h]")
    print("")
    print("  -r         Read inside the configuration file.")
    print("")
    print("  -w         Update, write or remove the value corresponding to a variable in the configuration file.")
    print("")
    print("  -t type    Type of configuration file whose parameters can be « yaml », « conf », « xml », « json » or « text ».")
    print("             The type « text », only available on writing, add the text specified in the value at the end of the file.")
    print("             If not filled, the default type is « conf ».")
    print("")
    print("  -a action  Action to realize when writing the variable and its value. Actions defined by the following keywords : ")
    print("                For « yaml » file type :")
    print("                  - « update » changes the value of an existing variable; or replace a list by the specified value. Create the variable if it doesn't exists.")
    print("                  - « append » appends the value at the end of a list. If necessary, converts the variable to a list.")
    print("                  - « remove » delete the variable and its values.")
    print("                For « text » file type :")
    print("                  - « remove » delete every line beginning with the text of the value; spaces characters in front of the line are ignored for matching.")
    print("                Other file types don't use this argument.")
    print("             The default action is « update ».")
    print("")
    print("  -f file    Full path of the configuration file to be edited ou read.")
    print("             This argument can point to a environment variable by prefixing it with the symbol « $ », for example « $MY_FILE ».")
    print("")
    print("  -p path    Path to the variable formatted in XPath for files types « xml », « json », « yaml »")
    print("             or section name for a « conf » file type.")
    print("             This argument is ignored in case of « text » file type.")
    print("")
    print("  -k var     Name of the variable or name of the tag.")
    print("             This argument is ignored in case of « text » file type.")
    print("")
    print("  -v value   Value corresponding to a variable or text to insert/remove for « text » file type.")
    print("             This argument can point to a environment variable by prefixing it with the symbol « $ », for example « $MY_VAR ».")
    print("             This argument is ignored in reading mode.")
    print("")
    print("  -l delim   Define delimiters between variables and values for « conf » file type.")
    print("             By default, delimiters are « =,: ».")
    print("")
    print("  -nospace   Remove spaces before and after the delimiter for « conf » file type.")
    print("             For example, 'myvar = myvalue' would become 'my_var=my_value'.")
    print("")
    print("  -n         Create a new tag named as the variable, even if a tag with the same name already exists.")
    print("             For « text » file type, the text line is forced to be written even if the same line already exists.")
    print("             This argument is ignored in case of « conf » file type.")
    print("")
    print("  -h         Show help.")
    print("")

def showhelp_dhcp():
    print( "setdhcp [-f filename] -group dhcp_group –host hostname [-mac mac_address] [-ip ip_address] [-mask netmask] [-server next_server] [-boot boot_file] [-h]")
    print("")
    print("  -f filename          Full path of the DHCP configuration file. The default filename is '/etc/dhcp/dhcpd.conf' will be used, if the file exists.")
    print("")
    print("  -group dhcp_group    Machine membership group.")
    print("")
    print("  -host hostname       Name of the machine.")
    print("")
    print("  -mac mac_address     MAC address of the machine. Mandatory if IP address is not specified")
    print("")
    print("  -ip ip_address       IP address of the machine. Mandatory if MAC address is not specified")
    print("")
    print("  -mask netmask        Netmask relative to the IP address of the machine.")
    print("")
    print("  -server next_server  IP address of the next server.")
    print("")
    print("  -boot boot_file      Name of the boot file.")
    print("")
    print("  -h                   Show help.")
    print("")

def init():

    setconf_src_path = (os.path.dirname(os.path.realpath(__file__)))
    #home_path = env.getenvvar("HOME")
    home_path = os.path.expanduser('~')

    if platform == "linux" or platform == "linux2":

        #Commandes à lancer pour démarrer l'init
        #sudo pip install -e git+https://github.com/kikeuf/setconf#egg=setconf
        #export SETCONF_PATH=`pip show setconf | grep -E "Location:" | cut -c 11-`
        #sudo python3 $SETCONF_PATH/src/setconf.py -init

        #os.system('sudo -i')
        #os.system('cd /')

        print('Retreiving files and folder')
        if setconf_src_path != "":
            setconf_path = setconf_src_path[0:-4]
        else:
            setconf_path = os.system('pip show setconf | grep -E "Location:" | cut -c 11-')

        if setconf_path == "":
            return

        setconf_file = setconf_path + '/setconf'
        setdhcp_file = setconf_path + '/setdhcp'

        print('Updating shortcut files')
        with open(setconf_file, 'w') as f:
            f.write("python3 " + setconf_path + "/src/setconf.py $*")

        with open(setdhcp_file, 'w') as f:
            f.write("python3 " + setconf_path + "/src/setconf.py -w -t dhcp $*")

        print('making executable')
        os.system('sudo chmod +x ' + setconf_file)
        os.system('sudo chmod +x ' + setdhcp_file)

        print('creating aliases')
        os.system('alias setconf="' + setconf_file + '"')
        os.system('alias setdhcp="' + setdhcp_file + '"')

        #writetext(home_path + '/.bashrc', 'alias setconf=', False, 'remove')
        #writetext(home_path + '/.bashrc', 'alias setdhcp=', False, 'remove')
        #writetext(home_path + '/.bashrc', 'alias setconf=' + setconf_file)
        #writetext(home_path + '/.bashrc', 'alias setdhcp=' + setdhcp_file)

        writetext('/etc/profile.d/00-setconf_aliases.sh', 'alias setconf=', False, 'remove')
        writetext('/etc/profile.d/00-setconf_aliases.sh', 'alias setdhcp=', False, 'remove')
        writetext('/etc/profile.d/00-setconf_aliases.sh', 'alias setconf=' + setconf_file)
        writetext('/etc/profile.d/00-setconf_aliases.sh', 'alias setdhcp=' + setdhcp_file)

def uninstall():

    setconf_src_path = (os.path.dirname(os.path.realpath(__file__)))

    if platform == "linux" or platform == "linux2":
        if setconf_src_path != "":
            setconf_path = setconf_src_path[0:-4]
        else:
            setconf_path = os.system('pip show setconf | grep -E "Location:" | cut -c 11-')

        os.system('unalias setconf')
        os.system('unalias setdhcp')

        # writetext(home_path + '/.bashrc', 'alias setconf=', False, 'remove')
        # writetext(home_path + '/.bashrc', 'alias setdhcp=', False, 'remove')

        writetext('/etc/profile.d/00-aliases.sh', 'alias setconf=', False, 'remove')
        writetext('/etc/profile.d/00-aliases.sh', 'alias setdhcp=', False, 'remove')

