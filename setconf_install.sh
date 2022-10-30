#wget https://raw.githubusercontent.com/kikeuf/setconf/master/setconf_install.sh && sh setconf_install.sh && rm setconf_install.sh

echo "Installing setconf and setdhcp"

#sudo -i
cd /

sudo pip install -e git+https://github.com/kikeuf/setconf#egg=setconf
export SETCONF_PATH=`pip show setconf | grep -E "Location:" | cut -c 11-`
sudo python3 $SETCONF_PATH/src/setconf.py -init

