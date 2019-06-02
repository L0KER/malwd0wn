import os
import subprocess
print """
 _____   _____   _____   _____   _____   _____   _____ 
|_____| |_____| |_____| |_____| |_____| |_____| |_____|
                 _             _  ___                 
 _ __ ___   __ _| |_      ____| |/ _ \__      ___ __  
| '_ ` _ \ / _` | \ \ /\ / / _` | | | \ \ /\ / / '_ \ 
| | | | | | (_| | |\ V  V / (_| | |_| |\ V  V /| | | |
|_| |_| |_|\__,_|_| \_/\_/ \__,_|\___/  \_/\_/ |_| |_|
 _____   _____   _____   _____   _____   _____   _____ 
|_____| |_____| |_____| |_____| |_____| |_____| |_____|
"""
print """
#-----------------------malwd0wn----------------------------#
| Don't use this application to hack! This app for          |
| the study viruses                                         |
#-----------------------------------------------------------#
| malwd0wn v.1.1                                            |
| Author: L0KER                                             |
| Github: https://github.com/L0KER                          |
| Copyright (C) 2019, Scorred Security All rights reserved  |
#-----------------------------------------------------------#
"""
print """
Select the OS
[0] - Android
[1] - Windows
[2] - MacOS
[3] - Exit
"""
os = input("malwd0wn> ")
if os == 0:
          print"[*] Selected OS: Android"
          print"[!] Select virus:"
          print"""
#-------------------#--Name--------------#
|[0] Ransomware     | Android.LockScreen |
|[1] Trojan         | Blackmart-fake     |
|[2] Virus          | Android.Viking     |
|[3] BotNet         | ING                |
#-------------------#--------------------#
"""
          vira = input("malwd0wn> ")
          if vira == 0:
                       print"[*] Downloading..."
                       subprocess.call(['./bin/android/andrl.sh'])
          if vira == 1:
                       print"[*] Downloading..."
                       subprocess.call(['./bin/android/admin.sh'])
          if vira == 2:
                       print"[*] Downloading..."
                       subprocess.call(['./bin/android/backd.sh'])
          if vira == 3:
                       print"[*] Downloading..."
                       subprocess.call(['./bin/android/botn.sh'])
elif os == 1:
             print"[*] Selected OS: Windows"
             print"[!] Select virus:"
             print """
#-------------------#--Name--------------#
|[0] Ransomware     | Petya.A            |
|[1] Virus          | Sampo              |
|[2] BotNet         | SpyEye             |
|[3] Dropper        | Trojan.Dropper.Gen |
|[4] Backdoor       | ZeroAccess         |
|[5] Worm           | Cridex             |
#-------------------#--------------------#
"""
             virw = input("malwd0wn> ")
             if virw == 0:
                          print"[*] Downloading..."
                          subprocess.call(['./bin/windows/rans.sh'])
             if virw == 1:
                          print"[*] Downloading..."
                          subprocess.call(['./bin/windows/vir.sh'])
             if virw == 2:
                          print"[*] Downloading..."
                          subprocess.call(['./bin/windows/botn.sh'])
             if virw == 3:
                          print"[*] Downloading..."
                          subprocess.call(['./bin/windows/dropp.sh'])
             if virw == 4:
                          print"[*] Downloading..."
                          subprocess.call(['./bin/windows/backd.sh'])
             if virw == 5:
                          print"[*] Downloading..."
                          subprocess.call(['./bin/windows/worm.sh'])
if os == 2:
           print"[*] Selected OS: MacOS"
           print"[!] Select virus:"
           print """
#-------------------#--Name--------------#
|[0] Stealer        | OSX.Wirenet        |
|[1] Backdoor       | OSX.Backdoor.iWorm |
|[2] Rootkit        | rubilyn            |
|[3] Apt trojan     | XAgent             |
#-------------------#--------------------#
"""
           virm = input("malwd0wn> ")
           if virm == 0:
                        print"[*] Downloading..."
                        subprocess.call(['./bin/macos/steal.sh'])
           if virm == 1:
                        print"[*] Downloading..."
                        subprocess.call(['./bin/macos/backd.sh'])
           if virm == 2:
                        print"[*] Downloading..."
                        subprocess.call(['./bin/macos/rootk.sh'])
           if virm == 3:
                        print"[*] Downloading..."
                        subprocess.call(['./bin/macos/apttroj.sh'])
if os == 3:
           print"malwd0wn closing..."
