from configparser import ConfigParser

# Get the configparser object
#config_object = ConfigParser()
dummy_section = "dummy_top_for_no_section_values_xxx"


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


def readconf(filename, section, variable):
    try:

        config_object = ConfigParser()

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

    except Exception:
        return ""


def writeconf(filename, section, variable, value):
    try:

        config_object = ConfigParser()

        if section == "":
            section = dummy_section
            with open(filename) as stream:
                config_object.read_string("[" + section + "]\n" + stream.read())  # This line does the trick.
        else:
            # copy config file to object
            config_object.read(filename)

        if not config_object.has_section(section):
            config_object.add_section(section)

        config_object.set(section, variable, value)

         # select the object section
        #section_object = config_object[section]

        # Update the variable with the new value
        #section_object[variable] = value

        # Write changes back to file
        with open(filename, 'w') as conf:
            config_object.write(conf)

        if section == dummy_section:
            return remove_first_line_of_file(filename)
        else:
            return True

    except Exception:
        return False


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


def writetext(filename, text):
    try:

        by = read_lastbyteoffile(filename)

        with open(filename, 'a') as f:
            if by != 10 and by != 13:
                f.write('\n')
            f.write(text + '\n')

        return True

    except Exception:
        return False


def read_lastbyteoffile(filename):
    with open(filename, 'rb') as ifile:
        buffer = ifile.read()
        lby = len(buffer) - 1
        return (buffer[lby])
