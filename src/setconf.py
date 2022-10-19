# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import conffile as cf
import environment as env
import jsonfile as jf
import settings as cfg
import xmlfile as xf
import yamlfile as yf
from arguments import translate_args


#def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#def listargs():
#    print(f"Arguments count: {len(sys.argv)}")
#    for i, arg in enumerate(sys.argv):
#        print(f"Argument {i:>6}: {arg}")

def setconfig():
    if cfg.arg_command == 'read':
        if cfg.arg_filetype == 'conf':
            value = cf.readconf(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable)
            env.setenvvar(cfg.arg_envvar, value)
            return value
        elif cfg.arg_filetype == 'yaml':
            value = yf.readyaml(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable)
            env.setenvvar(cfg.arg_envvar, value)
            return value
        elif cfg.arg_filetype == 'xml':
            #value = xf.readxml_sav(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable, cfg.arg_listindex)
            value = xf.readxml(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable)
            env.setenvvar(cfg.arg_envvar, value)
            return value
        elif cfg.arg_filetype == 'json':
            value = jf.readjson(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable)
            env.setenvvar(cfg.arg_envvar, value)
            return value
        else:
            return
    elif cfg.arg_command == 'write':
        if cfg.arg_filetype == 'conf':
            ret = cf.writeconf(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable, cfg.arg_value)
            return ret
        elif cfg.arg_filetype == 'yaml':
            ret = yf.writeyaml(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable, cfg.arg_value, cfg.arg_newtag)
            return ret
        elif cfg.arg_filetype == 'xml':
            #ret = xf.writexml_sav(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable, cfg.arg_value, cfg.arg_listindex)
            ret = xf.writexml(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable, cfg.arg_value, cfg.arg_newtag)
            return ret
        elif cfg.arg_filetype == 'json':
            ret = jf.writejson(cfg.arg_conffile, cfg.arg_section_path, cfg.arg_variable, cfg.arg_value, cfg.arg_newtag)
            return ret
        elif cfg.arg_filetype == 'text':
            ret = cf.writetext(cfg.arg_conffile, cfg.arg_value)
            return ret
        else:
            return
    else:
        return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm2')

    #cf.createinitest()
    #yf.createyamltest()
    #x.writexml('d:\config.xml', '/users/test', 'li2', '')
    #print(xf.readxml('d:\config.xml', '/users/test', 'li', 9))
    #jf.createjsontest()
    #r = jf.readjson('d:\config.json', '/menu/popup/menuitem[1]', 'value')

    #r = jf.writejson('d:\config.json', '/menu/popup/menuitem[0]', 'value3', 'New3', True, True)

    #ret = yf.readyaml('d:\config.yaml', '/autoinstall/identity', 'username')
    #yf.writeyaml('d:\config.yaml', '/autoinstall/identity', 'username', 'ubuntu3')
    #ret = yf.readyaml('d:\config2.yaml', 'Details', 'domain')
    #print(ret)


    ret = translate_args()
    #cfg.print_args()
    if not (ret is None):
        print(ret)
    else:
        #print("command : " + cfg.arg_command + " | variable : " + cfg.arg_variable + " | value : " + cfg.arg_value)
        ret = setconfig()
        print(ret)


        #yf.createyamltest()

        #print(env.getenvvar("GOPATH"))
        #ret=env.setenvvar("GOPATH","C:\\Users\\Kikeuf\\go2")

        #cf.createinitest()

        #value=cf.readconf('d:\config.ini','SERVERCONFIG','port')
        #print(value)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
