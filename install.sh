#!/bin/bash

echo """
#------malwd0wn------------#
| malwd0wn linux installer |
#--------------------------#
"""
cd bin && cd android && chmod +x * && cd ..
cd windows && chmod +x * && cd ..
cd macos && chmod +x * && cd ..
cd linux && chmod +x * && cd .. && cd ..
chmod +x malwd0wn.py
apt-get install curl -y
apt-get install python2 -y
echo """
#------malwd0wn-------#
| malwd0wn installed! |
#---------------------#
"""
