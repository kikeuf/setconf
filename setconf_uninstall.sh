#export SETCONF_PATH='/src/setconf'

BASEDIR=$(dirname $0)
#echo "Script location: ${BASEDIR}"

export SETCONF_PATH=`pip show setconf | grep -E "Location:" | cut -c 11-`
if [ $SETCONF_PATH = "" ]
then
  export SETCONF_PATH=$BASEDIR;
fi

#La ligne suivante ne fonctionne pas, il faut transister par un fichier temporaire comme workaround
#export PATH=`echo $PATH | sed 's/'$FMT_PATH'//' | sed 's/::/:/g' | sed 's/^://' | sed 's/:$//'`
sudo echo $PATH | sed 's/'$FMT_PATH'//' | sed 's/::/:/g' | sed 's/^://' | sed 's/:$//' > /tmp/fmt_path
export PATH="`cat /tmp/fmt_path`"
sudo rm /tmp/fmt_path

unalias setconf
unalias setdhcp

unset SETCONF_FILE
unset SETDHCP_FILE
unset FMT_PATH

sudo rm /etc/profile.d/00-setconf_aliases.sh

sudo pip uninstall git+https://github.com/kikeuf/setconf#egg=setconf

cd /
sudo rm -r $SETCONF_PATH

unset SETCONF_PATH




