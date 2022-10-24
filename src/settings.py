
import os
from conffile import writeconf, readconf

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

def showhelp():
    print("setconf [-r][-w] [-t type_of_file] -f filename [-p path_of_variable] [–v variable] [-d value] [-l list_of_delimiters] [-nospace] [-n] [-h]")
    print("")
    print("  -r         Read inside the configuration file.")
    print("")
    print("  -w         Update, write or remove the value corresponding to a variable in the configuration file.")
    print("")
    print("  -a action  Action to realize when writing the variable and its value. Actions defined by the following keywords : ")
    print("                - « update » changes the value of an existing variable; or replace a list by the specified value. Create the variable if it doesn't exists.")
    print("                - « append » appends the value at the end of a list. If necessary, converts the variable to a list.")
    print("                - « remove » delete the variable and its values.")
    print("             This argument is used only for « yaml » file type. The default action is « update ».")
    print("")
    print("  -t type    Type of configuration file whose parameters can be « yaml », « conf », « xml », « json » or « text ».")
    print("             If not filled, the default type will be « conf ».")
    print("             The type « text », only available on writing, add the text specified in the value at the end of the file.")
    print("")
    print("  -f file    Full path of the configuration file to be edited ou read.")
    print("")
    print("  -p path    Path to the variable formatted in XPath for files types « xml », « json », « yaml »")
    print("             or section name for a « conf » file type.")
    print("             This argument will be ignored in case of « text » file type.")
    print("")
    print("  -k var     Name of the variable or name of the tag.")
    print("             This argument will be ignored in case of « text » file type.")
    print("")
    print("  -v value   Value corresponding to a variable or text to insert for « text » file type.")
    print("             This Value can point to a environment variable by prefixing it with the symbol « $ », for example « $MY_VAR ».")
    print("             This argument will be ignored in reading mode.")
    print("")
    print("  -l delim   Define delimiters between variables and values for « conf » file type.")
    print("             By default, delimiters are « =,: ».")
    print("")
    print("  -nospace   Remove spaces before and after the delimiter for « conf » file type.")
    print("             For example, 'myvar = myvalue' would become 'my_var=my_value'.")
    print("")
    print("  -n         Create a new tag named as the variable, even if a tag with the same name already exists.")
    print("             This argument will be ignored in case of « text » or « conf » file types.")
    print("")
    print("  -h         Show help.")
    print("")

def showhelp_fr():
    print("setconf [-r][-w] [-t type_of_file] -f filename [-p path_of_variable] [–v variable] [-d value] [-l list_of_delimiters] [-nospace] [-n] [-h]")
    print("")
    print("   -r        Lecture dans le fichier de configuration.")
    print("")
    print("   -w        Ecrit ou remplace la valeur relative à une variable dans le fichier de configuration.")
    #print("")
    #print("   -e env    Nom de la variable d’environnement pour le retour de lecture.")
    #print("             Si non renseigné la variable d’environnement par défaut « SETCONF_ENV » sera utilisée.")
    print("")
    print("   -t type   Type de fichier de configuration dont les valeurs possibles sont « yaml », « conf », « xml », « json » ou « text ».")
    print("             Si non renseigné le format « conf » sera appliqué par défaut.")
    print("             Le type de fichier « text », disponible uniquement en écriture, ajoute le texte saisi comme valeur à la fin du fichier.")
    print("")
    print("   -f file   Chemin complet du fichier de configuration à lire ou éditer.")
    print("")
    print("   -p path   Chemin d’accès à la variable au format XPath pour les tyoes de fichiers « xml », « json », « yaml »")
    print("             ou nom de la section pour un fichier de type « conf » ")
    print("             Cet argument est ignoré dans le cas d’un type de fichier « text ».")
    print("")
    print("   -v var    Nom de la variable ou de la balise.")
    print("             Cet argument est ignoré dans le cas d’un type de fichier « text ».")
    print("")
    print("   -d value  Valeur relative à la variable ou texte à insérer pour le type de fichier  « text ».")
    print("             Cette valeur peut pointer vers une variable d’environnement en la préfixant le symbole « $ », par exemple « $MY_VAR ».")
    print("             Cet argument est ignoré en mode de lecture. ")
    print("")
 #   print("   -i index  Dans le cas de listes (variable répétée dans une section), l’index est le numéro de la variable à lire ou à écrire.")
 #   print("             Utiliser l’index « 0 » pour lire ou écrire l’ensemble des valeurs de cette liste.")
 #   print("             Utiliser l’index « -1 » pour ajouter un élément à la liste (écriture).")
 #   print("             L’index ne fonctionne pour l’instant qu’avec le type de fichier « xml ».")
 #   print("")
    print("   -l delim   Redéfinit les délimiteurs entre variables et valeurs pour les fichiers de type « conf ».")
    print("              Par défaut, les délimiteurs sont « =,: ».")
    print("")
    print("   -nospace  Supprime les espaces devant et derrière le délimiteur pour les fichiers de type « conf ».")
    print("             Par exemple, 'myvar = myvalue' deviendra 'my_var=my_value'.")
    print("")
    print("   -n        Crée une nouvelle balise, portant le nom de la variable, même si une balise de même nom existe déjà.")
    print("             Cet argument est ignoré dans le cas de type de fichier « text » et « conf ».")
    print("")
    print("   -h        Affiche l'aide.")
    print("")



