import tkinter as tk # Import tinker which we will use to design our GUI 
from tkinter import filedialog, Text # filedialog will help us extract the path file and text will help display test to our GUI 
import os 

root = tk.Tk() # If you think in terms of html, this is kinda the whole of the body, everything we want to display we put here 
apps = []

def initApp():
    if os.path.isfile('save.txt'):
        with open('save.txt', 'r') as f:
            tempApps = f.read()
            apps = tempApps.split(',')
            apps = [x for x in apps if x.strip()]

    for app in apps:
        label=tk.Label(frame, text=app, bg="gray")
        label.pack()
    
    return apps

def addApp():
    print(apps)
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
                                        filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def delLastApp():
    apps.pop()

    for widget in frame.winfo_children():
        widget.destroy()
    
    for app in apps:
        label=tk.Label(frame, text=app, bg="gray")
        label.pack()


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42") # Sets a backdrop 
canvas.pack() #connects the backdrop to be displayed 

frame = tk.Frame(root, bg="white")

# Woweeee lotta arguments, relwidth and relheight set the relative heights and width
# while relx and rely sets the "padding" if you will haha epic css term but unlike padding this is spacing 
# for the actual object, its actual size does not increase 
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) 

# Okay so there is actual padding for this too, fg controlls font color 
# Note that here we have to option to add to either root or frame 
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runFile = tk.Button(root, text="Run File", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runFile.pack()

delLastFile = tk.Button(root, text="Delete Last File", padx=10, pady=5, fg="white", bg="#263D42", command=delLastApp)
delLastFile.pack()

apps = initApp()

root.mainloop()
