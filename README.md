# PyInfect
Backdoor any .py file // Backdoor implanter for OS X - Compatible with EggShell!

# Description
PyInfect is a tool that allows you to create and implant a backdoor on any .py file. The malware works on Mac OS (and soon for Linux).

# Getting Started
#### Installation
```git clone https://github.com/0xCoto/PyInfect```

#### Usage

```
cd PyInfect
python PyInfect.py
```

# Mechanism
The way this tool works is by writing a backdoored shell command in .py file which is being executed when the .py file is run. As soon as the victim runs the .py script, it'll automatically run that shell command which will install a persistance .plist file on their computer, which you can customize using this interactive script.

# Manage Connections
You can monitor, manage and interact with infected machines with the CNC interface created by [Lucas Jackson](https://github.com/neoneggplant/): [EggShell](https://github.com/neoneggplant/EggShell).

# To do
1. Implement feature to implant backdoor on a pre-existing .py file.
2. Support Linux infection (without persistence) - EggShell does not support Linux.
~~3. Make it Python3 compatible.~~
