sudo echo 'alias setconf='$SETCONF_FILE > /etc/profile.d/00-setconf_aliases.sh
sudo echo 'alias setdhcp='$SETDHCP_FILE >> /etc/profile.d/00-setconf_aliases.sh
sudo echo 'export PATH='$PATH >> /etc/profile.d/00-setconf_aliases.sh

#sudo chmod +x $SETCONF_PATH/setconf_install.sh
sudo rm $SETCONF_PATH/setconf_install.sh
sudo rm $SETCONF_PATH/setconf_install_end.sh
sudo chmod +x $SETCONF_PATH/setconf_uninstall

sudo echo 'python3 '$SETCONF_PATH'/src/setconf.py $*' > $SETCONF_FILE
sudo echo 'python3 '$SETCONF_PATH'/src/setconf.py -w -t dhcp $*' > $SETDHCP_FILE

sudo chmod +x $SETCONF_FILE
sudo chmod +x $SETDHCP_FILE

sudo rm /tmp/setconf_install.sh
sudo rm /tmp/setconf_install_end.sh