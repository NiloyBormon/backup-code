import requests
import os
import subprocess
import sys
from tkinter import messagebox
import time
import json

def currentVersionFunction():
    currentVersion = "0.0.1"
    try:
        with open("version.json","r")as f:
            currentVersion = json.load(f)
        return currentVersion
    except FileNotFoundError:
        with open ("version.json", "w")as f:
            json.dump(currentVersion,f)
        return currentVersion.strip()
       

def latestVersionFunction():
    latestVersion = requests.get("https://raw.githubusercontent.com/NiloyBormon/ToDoListGui/refs/heads/main/version").text
    return latestVersion.strip()

currentVersion = currentVersionFunction()
latestVersion = latestVersionFunction()
if currentVersion.strip() != latestVersion.strip():
    messagebox.showinfo("output","Update available.Trying to update")
    with open(f"ToDoListGui{latestVersion.strip()}.exe","wb")as f:
              f.write(requests.get("https://github.com/NiloyBormon/ToDoListGui/raw/refs/heads/main/ToDoListGui0.0.1.exe").content)
    messagebox.showinfo("output","Latest version download done")
    os.replace(f"ToDoListGui{currentVersion.strip()}",f"ToDoListGui{latestVersion.strip()}")
    print("update done")
    currentVersion = latestVersion
    with open("version.json","w")as f:
           json.dump(latestVersion,f)
    messagebox.showinfo("output","Update done. Restarting")
    subprocess.Popen([f"ToDoList{latestVersion}"])
    sys.exit()