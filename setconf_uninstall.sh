cd /

unalias setconf
unalias setdhcp

sudo rm /etc/profile.d/00-setconf_aliases.sh

export SETCONF_PATH=`pip show setconf | grep -E "Location:" | cut -c 11-`
sudo pip uninstall git+https://github.com/kikeuf/setconf#egg=setconf

sudo rm -r $SETCONF_PATH