import tkinter
from tkinter import simpledialog, messagebox
import toDoListBackEnd
from toDoListBackEnd import taskInputButton, updateBtn

root = tkinter.Tk()
root.title("ToDoList")
root.geometry("500x500")

updateBtn = tkinter.Button(root,text="Check for update", command=updateBtn)
updateBtn.pack(pady=10)

createNewTaskBtn = tkinter.Button(root,text="Create New Task", command=taskInputButton)
createNewTaskBtn.pack(pady=50)

# viewTasksBtn = tkinter.Button(root, text="View Tasks")

root.mainloop()