#!/bin/bash

echo """
#------malwd0wn-------------#
| malwd0wn termux installer |
#---------------------------#
"""
cd bin && cd android && chmod +x * && cd ..
cd windows && chmod +x * && cd .. && cd ..
chmod +x malwd0wn.py
pkg install curl
pkg install python2
echo """
#------malwd0wn-------#
| malwd0wn installed! |
#---------------------#
"""
