from tkinter import simpledialog, messagebox
import json
import subprocess
from tkinter import messagebox
import requests
import sys
from update import latestVersionFunction, currentVersionFunction
import os


def taskInputButton():
    taskKey = simpledialog.askstring("input", "Enter your task")
    taskValue = simpledialog.askstring("input", "Enter task description")
    if taskKey: 
        tasks[taskKey]=taskValue
        with open("tasks.json", "w")as f:
            json.dump(tasks,f)
        messagebox.showinfo("output", f"Your task {taskKey}:\"{taskValue}\" is saved")
    # return userInput

def updateBtn():
    if currentVersion.strip() != latestVersionFunction():
        # messagebox.showinfo("output",f"{currentVersion}{latestVersionFunction}")
        try:
            subprocess.Popen(["update.exe"])
            sys.exit()
        except:    
            messagebox.showinfo("output", "Downloading required file")
            with open("update.exe","wb") as f:
                f.write(requests.get("https://github.com/NiloyBormon/ToDoListGui/raw/refs/heads/main/update.exe").content)
            subprocess.Popen(["update.exe"])
            sys.exit()
    else:
        messagebox.showinfo("output","Already up to date")
        
currentVersion = currentVersionFunction()
tasks = {}