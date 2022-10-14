

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
arg_conffile = ""  # full file name of the config file
arg_section_path = ""  # Section name or XML path or json path (without variable name)
arg_variable = ""  # Name of the variable
arg_value = ""  # value relative to the variable
arg_envvar = "" # name of environment variable to use
arg_newtag = False #Add new tag in XML, Json or yaml even if tag already exists (list)
#arg_listindex=-9999 #Index of the item to read or write in a list
default_env = "SETCONF_ENV"
#default_listindex = 1

def print_args():
    print("command : " + arg_command)
    print("filetype : " + arg_filetype)
    print("filename : " + arg_conffile)
    print("section : " + arg_section_path)
    print("variable : " + arg_variable)
    print("value : " + arg_value)
    print("environment variable : " + arg_envvar)

def removeblanklines(filename):
    with open(filename) as reader, open(filename, 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
        writer.truncate()

def showhelp():
    print("setconf [-r][-w] [-e environment_variable] [-t type_of_file] -f filename [-p path_of_variable] [–v variable] [-d value] [-n] [-h]")
    print("")
    print("   -r        Lecture dans le fichier de configuration. La valeur lue sera écrite dans la variable d’environnement")
    print("             spécifiée avec le commutateur - e ou par défaut dans la variable d’environnement « SETCONF_ENV ».")
    print("")
    print("   -w        Ecrit ou remplace la valeur relative à une variable dans le fichier de configuration.")
    print("")
    print("   -e env    Nom de la variable d’environnement pour le retour de lecture.")
    print("             Si non renseigné la variable d’environnement par défaut « SETCONF_ENV » sera utilisée.")
    print("")
    print("   -t type   Type de fichier de configuration dont les valeurs possibles sont « yaml », « conf », « xml », « json » ou « text ».")
    print("             Si non renseigné le format « conf » sera appliqué par défaut.")
    print("             Le type de fichier « text », disponible uniquement en écriture, ajoute le texte saisi comme valeur à la fin du fichier.")
    print("")
    print("   -f file   Chemin complet du fichier de configuration à lire ou éditer.")
    print("")
    print("   -p path   Chemin d’accès à la variable qui représente la section pour un fichier de type « conf » ")
    print("             ou le chemin au format XPath pour un fichier de type « xml », « json » ou « yaml ».")
    print("             Cet argument est ignoré dans le cas d’un type de fichier « text ».")
    print("")
    print("   -v var    Nom de la variable. Le commutateur -v est facultatif si le nom de la variable est placé en ")
    print("             avant-dernière position juste devant la valeur, ou en dernière position si la valeur n’est pas requise (lecture).")
    print("             Cet argument est ignoré dans le cas d’un type de fichier « text ».")
    print("")
    print("   -d value  Valeur relative à la variable. Le commutateur -d est facultatif si cette valeur est placée en dernière position.")
    print("             La valeur est ignorée et donc non requise en mode de lecture. Cette valeur peut pointer vers une variable ")
    print("             d’environnement en préfixant le nom de la variable d’environnement par le symbole « $ », par exemple « $MY_VAR ».")
    print("             Le symbole « $ » seul est un raccourci vers la variable par défaut « $SETCONF_ENV ».")
    print("")
 #   print("   -i index  Dans le cas de listes (variable répétée dans une section), l’index est le numéro de la variable à lire ou à écrire.")
 #   print("             Utiliser l’index « 0 » pour lire ou écrire l’ensemble des valeurs de cette liste.")
 #   print("             Utiliser l’index « -1 » pour ajouter un élément à la liste (écriture).")
 #   print("             L’index ne fonctionne pour l’instant qu’avec le type de fichier « xml ».")
 #   print("")
    print("   -n        Crée une nouvelle balise, portant le nom de la variable, même si une balise de même nom existe déjà.")
    print("             Cet argument est ignoré dans le cas de type de fichier « text » et « conf ».")
    print("")
    print("   -h        Affiche l'aide.")
    print("")
