import subprocess
import sys
import os
import time

newFile = "toDoListNew.exe"
oldFile = "toDoList.exe"

os.replace(newFile,oldFile)
subprocess.Popen(["toDoList.exe"])
sys.exit()