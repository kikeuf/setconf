cd /

unalias setconf
unalias setdhcp

sudo rm /etc/profile.d/00-setconf_aliases.sh

export SETCONF_PATH=`pip show setconf | grep -E "Location:" | cut -c 11-`
sudo pip uninstall git+https://github.com/kikeuf/setconf#egg=setconf

#La ligne suivante ne fonctionne pas, il faut transister par un fichier temporaire comme workaround
#export FMT_PATH=`echo $SETCONF_PATH | sed 's/\//\\\//g'`
sudo echo $SETCONF_PATH | sed 's/\//\\\//g' > /tmp/fmt_path
export FMT_PATH="`cat /tmp/fmt_path`"
sudo rm /tmp/fmt_path

export PATH=`echo $PATH | sed 's/'$FMT_PATH'//' | sed 's/::/:/g' | sed 's/^://' | sed 's/:$//'`

sudo rm -r $SETCONF_PATH