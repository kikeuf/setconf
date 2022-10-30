#sudo wget -P /tmp https://raw.githubusercontent.com/kikeuf/setconf/master/setconf_install.sh && . /tmp/setconf_install.sh && sudo rm /tmp/setconf_install.sh

echo "Installing setconf and setdhcp"

#sudo -i
cd /

sudo pip install -e git+https://github.com/kikeuf/setconf#egg=setconf

export SETCONF_PATH=`pip show setconf | grep -E "Location:" | cut -c 11-`
export SETCONF_FILE=$SETCONF_PATH/setconf
export SETDHCP_FILE=$SETCONF_PATH/setdhcp

alias setconf=$SETCONF_FILE
alias setdhcp=$SETDHCP_FILE

sudo echo 'python3 '$SETCONF_PATH'/src/setconf.py $*' > $SETCONF_FILE
sudo echo 'python3 '$SETCONF_PATH'/src/setconf.py -w -t dhcp $*' > $SETDHCP_FILE

sudo chmod +x $SETCONF_FILE
sudo chmod +x $SETDHCP_FILE

#sudo chmod +x $SETCONF_PATH/setconf_install.sh
sudo rm $SETCONF_PATH/setconf_install.sh
sudo chmod +x $SETCONF_PATH/setconf_uninstall

#La ligne suivante ne fonctionne pas, il faut transister par un fichier temporaire comme workaround
#export FMT_PATH=`echo $SETCONF_PATH | sed 's/\//\\\//g'`
sudo echo $SETCONF_PATH | sed 's/\//\\\//g' > /tmp/fmt_path
export FMT_PATH="`cat /tmp/fmt_path`"
sudo rm /tmp/fmt_path

export NEW_PATH=`echo $PATH | sed 's/'$FMT_PATH'//' | sed 's/::/:/g' | sed 's/^://' | sed 's/:$//'`
export PATH=`echo $SETCONF_PATH':'$NEW_PATH`

sudo echo 'alias setconf='$SETCONF_FILE > /etc/profile.d/00-setconf_aliases.sh
sudo echo 'alias setdhcp='$SETDHCP_FILE >> /etc/profile.d/00-setconf_aliases.sh
sudo echo 'export PATH='$PATH >> /etc/profile.d/00-setconf_aliases.sh

#sudo python3 $SETCONF_PATH/src/setconf.py -init

