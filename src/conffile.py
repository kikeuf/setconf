from configparser import ConfigParser
# https://coderzcolumn.com/tutorials/python/configparser-simple-guide-to-create-and-parse-configuration-files
# Get the configparser object
#config_object = ConfigParser()

from journal import log

#-------------------------------------------------
# Read and write conf files type
#-------------------------------------------------

dummy_section = "dummy_top_for_no_section_values_xxx"

def readconf(filename, section, variable, delimiters_list="=,:"):
    try:

        config_object = ConfigParser(allow_no_value=True, delimiters=delimiters_list)

        if section == "":
            section = dummy_section
            with open(filename) as stream:
                config_object.read_string("[" + section + "]\n" + stream.read())  # This line does the trick.
        else:
            # copy config file to object
            config_object.read(filename)

        # Get the value
        section_object = config_object[section]
        value = section_object[variable]
        return value

    except Exception as e:
        log('Setconf error : ' + repr(e))
        return ""


def writeconf(filename, section, variable, value, delimiters_list="=,:", delimiter_spaces=True):

    try:

        #read_section(filename, section)

        #, comment_prefixes='/'
        config_object = ConfigParser(allow_no_value=True, delimiters=delimiters_list)
        #parser = configparser.ConfigParser(delimiters=('?', '*'))

        if section == "":
            section = dummy_section
            with open(filename) as stream:
                config_object.read_string("[" + section + "]\n" + stream.read())  # This line does the trick.
        else:
            # copy config file to object
            config_object.read(filename)

        if not config_object.has_section(section):
            #contournement de bug, on vérifie une seconde fois avec un second test
            if not file_contains_line(filename, '['+section+']'):
                config_object.add_section(section)

        config_object.set(section, variable, value)

         # select the object section
        #section_object = config_object[section]

        # Update the variable with the new value
        #section_object[variable] = value

        # Write changes back to file
        with open(filename, 'w') as conf:
            config_object.write(conf, space_around_delimiters=delimiter_spaces)

        if section == dummy_section:
            return remove_first_line_of_file(filename)
        else:
            return True

    except Exception as e:
        log('Setconf error : ' + repr(e))
        return False


def read_section(filename, section, delimiters_list="=,:"):

    config_object = ConfigParser(allow_no_value=True, delimiters=delimiters_list)

    if section == "":
        section = dummy_section
        with open(filename) as stream:
            config_object.read_string("[" + section + "]\n" + stream.read())  # This line does the trick.
    else:
        # copy config file to object
        config_object.read(filename)

    section_object = config_object[section]
    for it in section_object:
        print(it)

    #value = section_object[variable]

#-------------------------------------------------
# Read and write text files type
#-------------------------------------------------
def writetext(filename, text, newtag=False, action='update'):

    try:

        if action == 'update' or action == 'append':
            if newtag:
                allow_writing = True
            elif file_contains_line(filename, text):
                allow_writing = False
            else:
                allow_writing = True

            if allow_writing:
                by = read_lastbyteoffile(filename)

                with open(filename, 'a') as f:
                    if by != 10 and by != 13:
                        f.write('\n')
                    f.write(text + '\n')
                    return True

            return False

        elif action == 'remove':
            content = file_remove_lines(filename, text)
            if content != "":
                with open(filename, 'w') as f:
                    f.write(content)
                return True
            else:
                return False

        else:
            return False

    except Exception:
        return False


#-------------------------------------------------
# Manipulate files
#-------------------------------------------------
def remove_first_line_of_file(filename):
    try:

        with open(filename, 'r+') as fp:
            # read an store all lines into list
            lines = fp.readlines()
            # move file pointer to the beginning of a file
            fp.seek(0)
            # truncate the file
            fp.truncate()

            # start writing lines except the first line
            # lines[1:] from line 2 to last line
            fp.writelines(lines[1:])

        return True

    except Exception:
        return False

def read_lastbyteoffile(filename):

    try:

        with open(filename, 'rb') as ifile:
            buffer = ifile.read()
            lby = len(buffer) - 1
            return (buffer[lby])

    except:
        return ""

def file_contains_line(filename, text):

    try:
        ffile = open(filename, 'r')
        loglist = ffile.readlines()
        ffile.close()

        for line in loglist:
            #if str(self.CLIENT_HOST) in line:
            if (text == line) or (text + '\n' == line):
                return True

        return False

    except:
        return False

def file_remove_lines(filename, text):

    try:
        content = ""

        ffile = open(filename, 'r')
        loglist = ffile.readlines()
        ffile.close()

        l = len(text)
        for line in loglist:
            xline = line.strip()[0:l]
            if text != xline:
                content += line

        return content

    except:
        return ""

#-------------------------------------------------
# Test and archived functions
#-------------------------------------------------
def createinitest():

    config_object = ConfigParser()

    # Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
    config_object["USERINFO"] = {
        "admin": "Chankey Pathak",
        "loginid": "chankeypathak",
        "password": "tutswiki"
    }

    config_object["SERVERCONFIG"] = {
        "host": "tutswiki.com",
        "port": "8080",
        "ipaddr": "8.8.8.8"
    }

    # Write the above sections to config.ini file
    with open('d:\config.ini', 'w') as conf:
        config_object.write(conf)