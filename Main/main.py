# Importing all modules
from tkinter import *
import tkinter.messagebox as meassge1
import webbrowser
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os
from tkinter import ttk
import pyautogui
import tkinter.ttk as ttk
from tkinter import PhotoImage
import font

# Defining root
root = Tk()
root.title(f"Untitled - HtmlPad")

p1 = PhotoImage(file = 'logo.png')
root.iconphoto(False, p1)


# All functions
def quit():
    global HTMLFILE
    if HTMLFILE == None:
        a = meassge1.askquestion("Exit","You have not saved work, do you want to save it")
        if a == "yes":
            root.destroy()
    else:
        root.destroy()


def gethelp():
    meassge1.showinfo("Info", "This App Made By Saksham Jain")


def run():
    global HTMLFILE
    if HTMLFILE == None:

        if HTMLFILE == None:
            HTMLFILE = asksaveasfilename(initialfile="WritePadUntitled.html", defaultextension=".html",
                                         filetypes=[("All Files", "*.*"), ("Html documents", "*.html")])
            if HTMLFILE == "":
                HTMLFILE = None
            else:
                fileinside = open(HTMLFILE, 'w')
                fileinside.write(htmlarea.get(1.0, END))
                fileinside.close()
                root.title(os.path.basename(HTMLFILE) + "-HtmlPad")
        else:
            fileinside = open(HTMLFILE, 'w')
            fileinside.write(htmlarea.get(1.0, END))
            fileinside.close()
            root.title(os.path.basename(HTMLFILE) + "-HtmlPad")
    else:
     f = open(HTMLFILE, 'w')
     f.write(htmlarea.get(1.0,END))
     f.close()
    webbrowser.open_new_tab(HTMLFILE)


def help():
    meassge1.askquestion("Help","Do You Want Recieve Help")


def cut():
    pyautogui.hotkey("ctrl", "x")


def copy():
    pyautogui.hotkey("ctrl", "c")


def paste():
    pyautogui.hotkey("ctrl", "v")


def undo():
    pyautogui.hotkey("ctrl", "z")


def redo():
    htmlarea.event_generate("<<Redo>>")

def newfile():
       global HTMLFILE
       root.title("Untitled - HtmlPad")
       HTMLFILE = None
       htmlarea.delete(1.0,END)


def openfile():
      global HTMLFILE
      global CSSFILE
      global JSFILE
      file = askopenfilename(defaultextension=".html",filetypes=[("All Files","*.*"),("Html documents","*.html")])
      if file==" ":
          file=None
      else:
        if ".html" in file:
           root.title(os.path.basename(file)+"-HtmlPad")
           htmlarea.delete(1.0, END)
           fileinside=open(file,"r")
           htmlarea.insert(1.0,fileinside.read())
           fileinside.close()
           HTMLFILE =file
           tabControl.tab(tab1, text = os.path.basename(HTMLFILE))
           tabControl.select(tab1)

        if ".css" in file:
           root.title(os.path.basename(file)+"-HtmlPad")
           cssarea.delete(1.0, END)
           fileinside=open(file,"r")
           cssarea.insert(1.0,fileinside.read())
           fileinside.close()
           CSSFILE = file
           tabControl.tab(tab2, text = os.path.basename(CSSFILE))
           tabControl.select(tab2)

        if ".js" in file:
           root.title(os.path.basename(file)+"-HtmlPad")
           jsarea.delete(1.0, END)
           fileinside=open(file,"r")
           jsarea.insert(1.0,fileinside.read())
           fileinside.close()
           JSFILE = file
           tabControl.tab(tab3, text = os.path.basename(JSFILE))
           tabControl.select(tab3)


def savehtml():
    global HTMLFILE
    if HTMLFILE==None:
       HTMLFILE = asksaveasfilename(initialfile="WritePadUntitled.html", defaultextension=".html",filetypes=[("All Files", "*.*"),("Html documents", "*.html")])
       if HTMLFILE == "":
          HTMLFILE = None
       else:
          fileinside = open(HTMLFILE, 'w')
          fileinside.write(htmlarea.get(1.0, END))
          fileinside.close()
          root.title(os.path.basename(HTMLFILE) + "-HtmlPad")
    else:
     fileinside = open(HTMLFILE, 'w')
     fileinside.write(htmlarea.get(1.0, END))
     fileinside.close()
     root.title(os.path.basename(HTMLFILE) + "-HtmlPad")


def savecss():
    global CSSFILE
    if CSSFILE==None:
       CSSFILE = asksaveasfilename(initialfile="style.css", defaultextension=".css",filetypes=[("All Files", "*.*"),("CSS documents", "*.css")])
       if CSSFILE == "":
          CSSFILE = None
       else:
          fileinside = open(CSSFILE, 'w')
          fileinside.write(cssarea.get(1.0, END))
          fileinside.close()
          root.title(os.path.basename(CSSFILE) + "-HtmlPad")
    else:
     fileinside = open(CSSFILE, 'w')
     fileinside.write(cssarea.get(1.0, END))
     fileinside.close()
     root.title(os.path.basename(CSSFILE) + "-HtmlPad")


def savejs():
    global JSFILE
    if JSFILE==None:
       JSFILE = asksaveasfilename(initialfile="js.js", defaultextension=".js",filetypes=[("All Files", "*.*"),("JS documents", "*.js")])
       if JSFILE == "":
          JSFILE = None
       else:
          fileinside = open(JSFILE, 'w')
          fileinside.write(jsarea.get(1.0, END))
          fileinside.close()
          root.title(os.path.basename(JSFILE) + "-HtmlPad")
    else:
     fileinside = open(JSFILE, 'w')
     fileinside.write(jsarea.get(1.0, END))
     fileinside.close()
     root.title(os.path.basename(JSFILE) + "-HtmlPad")

def select_all(event):
    htmlarea.tag_add(SEL, "1.0", END)
    htmlarea.mark_set(INSERT, "1.0")
    htmlarea.see(INSERT)
    return 'break'

def enter():
     htmlarea.insert(END,'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <script src="js.js"></script>
</head>
<body>
    
</body>
</html>
''')


def enterjs():
    htmlarea.insert(INSERT,'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="js.js"></script>
    <title>Document</title>
</head>
<body>
    
</body>
</html>''')


def htmlenter():
    htmlarea.insert(INSERT,'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>''')

def entercss():
    htmlarea.insert(INSERT,'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    
</body>
</html>''')

def h1():
    htmlarea.insert(INSERT,"<h1></h1>")


def h2():
    htmlarea.insert(INSERT, "<h2></h2>")


def h3():
    htmlarea.insert(INSERT,"<h3></h3>")


def h4():
    htmlarea.insert(INSERT, "<h4></h4>")


def h5():
    htmlarea.insert(INSERT,"<h5></h5>")


def h6():
    htmlarea.insert(INSERT, "<h6></h6>")


def p():
    htmlarea.insert(INSERT, "<p></p>")

# All files
HTMLFILE = None
CSSFILE = None
JSFILE = None

#String var
htmlname = StringVar()
cssname = StringVar()
jsname = StringVar() 

htmlname.set("HTML")
cssname.set("CSS")
jsname.set("JS")

# Tab controller
tabControl = ttk.Notebook(root)
  
htmlimg = PhotoImage(file=r'logo.png')

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text =htmlname.get())
tabControl.add(tab2, text =cssname.get())
tabControl.add(tab3, text =jsname.get())

tabControl.pack(expand = False, fill ="both")

style=ttk.Style()
style.theme_use('classic')
style.configure("Vertical.TScrollbar", background="#433566", bordercolor="#433566", arrowcolor="#433566", troughcolor="#282C3E")

scroll = ttk.Scrollbar(tab1)
scroll.pack(side=RIGHT,fill=Y)
htmlarea = Text(tab1, font=("Droid Sans Mono",14),yscrollcommand=scroll.set, undo=True)
htmlarea.pack(fill=BOTH,expand=TRUE)
htmlarea.config(background="#282C3E", foreground="white", insertbackground='#433566')
scroll.config(command=htmlarea.yview)


scroll = ttk.Scrollbar(tab2)
scroll.pack(side=RIGHT,fill=Y)
cssarea = Text(tab2, font=("Droid Sans Mono",14),yscrollcommand=scroll.set, undo=True)
cssarea.pack(fill=BOTH,expand=TRUE)
cssarea.config(background="#282C3E", foreground="white", insertbackground='#433566')
scroll.config(command=cssarea.yview)

scroll = ttk.Scrollbar(tab3)
scroll.pack(side=RIGHT,fill=Y)
jsarea = Text(tab3, font=("Droid Sans Mono",14),yscrollcommand=scroll.set, undo=True)
jsarea.pack(fill=BOTH,expand=TRUE)
jsarea.config(background="#282C3E", foreground="white", insertbackground='#433566')
scroll.config(command=jsarea.yview)

#Menus
MainMenu=Menu(root, background='#373737',foreground='#373737')

#Sub menu File
Filemenu=Menu(MainMenu,tearoff=0, background='#373737', foreground = 'white')
Filemenu.add_command(label="New",command=newfile)
Filemenu.add_command(label="Open",command=openfile)
Filemenu.add_command(label="HTML",command=savehtml)
Filemenu.add_command(label="CSS",command=savecss)
Filemenu.add_command(label="JS",command=savejs)
Filemenu.add_separator()
Filemenu.add_command(label="Exit",command=quit)

MainMenu.add_cascade(menu=Filemenu,label="File", foreground = 'white')

# Sub menu Enter
basic=Menu(MainMenu,tearoff=0, background='#373737', foreground = 'white')
basic.add_command(label="Enter basic structure",command=htmlenter)
basic.add_command(label="Insert JS with HTML",command=enterjs)
basic.add_command(label="Insert CSS with HTML",command=entercss)
basic.add_command(label="Enter complete structure",command=enter)
basic.add_command(label="H1",command=h1)
basic.add_command(label="H2",command=h2)
basic.add_command(label="H3",command=h3)
basic.add_command(label="H4",command=h4)
basic.add_command(label="H5",command=h5)
basic.add_command(label="H6",command=h6)
basic.add_command(label="P",command=p)

MainMenu.add_cascade(menu=basic,label="Enter", foreground = 'white')

# Sub menu Commands
Edit=Menu(MainMenu,tearoff=0, background='#373737', foreground = 'white')
Edit.add_command(label="Cut",command=cut)
Edit.add_command(label="Copy",command=copy)
Edit.add_command(label="Paste",command=paste)
Edit.add_command(label="Redo",command=redo)
Edit.add_command(label="Undo",command=undo)

MainMenu.add_cascade(menu=Edit,label="Commands", foreground = 'white')

# Sub menu run
r=Menu(MainMenu,tearoff=0, background='#373737', foreground = 'white')
r.add_command(label="Run",command=run)

MainMenu.add_cascade(menu=r,label="Run", foreground = 'white')

# Sub menu run
Help=Menu(MainMenu,tearoff=0, background='#373737', foreground = 'white')
Help.add_command(label="About",command=gethelp)
Help.add_command(label="Help",command=help)

MainMenu.add_cascade(menu=Help,label="Help", foreground = 'white')

# Adding menu
root.config(menu=MainMenu)

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook', background="#30354A", foreground="white")
s.configure('TNotebook.Tab', background="#30354A", foreground="#8D96C9")
s.map("TNotebook.Tab", background=[("selected", "#282C3E")], foreground=[("selected", "white")])

# Status bar
statusvar = StringVar()
statusvar.set("Using HTML, CSS And JS")

sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w", background="#272B3D", foreground="#8D96C9")
sbar.pack(side=BOTTOM, fill=X)

root.mainloop()