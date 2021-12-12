from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import ttk, messagebox
import subprocess
import webbrowser
import requests

__author__ = 'PKZOID/PKGAMER/ATIFSIDDIQUE'
__copyright__ = 'Copyright (C) 2020, PKZOID'
__credits__ = ['PKZOID']
__license__ = 'The MIT License (MIT)'
__version__ = '1.0'
__maintainer__ = 'Victor Santiago'
__email__ = 'Snipergamerpk@gmail.com'
__status__ = 'Beta'

_AppName_ = 'IDLE'

root = Tk()
root.geometry('900x700')
root.attributes('-alpha',0.95)
root.title("Python IDLE")
file_path = ''

def Comingsoon():
    messagebox.showinfo('Coming Soon',"Coming Soon Update Make Your Own Language Only For Premium User")
def check_updates():
            try:
                # -- Online Version File
                # -- Replace the url for your file online with the one below.
                response = requests.get(
                    'https://raw.githubusercontent.com/vsantiago113/Tkinter-MyTestApp/master/version.txt')
                data = response.text

                if float(data) > float(__version__):
                    messagebox.showinfo('Software Update', 'Update Available!')
                    mb1 = messagebox.askyesno('Update!', f'{_AppName_} {__version__} needs to update to version {data}')
                    if mb1 is True:
                        # -- Replace the url for your file online with the one below.
                        webbrowser.open_new_tab('https://github.com/vsantiago113/Tkinter-MyTestApp/raw/master/'
                                                'updates/MyTestApp.msi?raw=true')
                        parent.destroy()
                    else:
                        pass
                else:
                    messagebox.showinfo('Software Update', 'No Updates are Available.')
            except Exception as e:
                messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))

def theme():
    editor.configure(bg='#3D2B27',foreground='white',insertbackground='white')
    code_output.configure(bg='#3D2B27',foreground='red',insertbackground='red')
    file_label.configure(bg='#3D2B27',foreground='white')
    output_label.configure(bg='#3D2B27',foreground='red')
    background.configure(bg='#3D2B27')
def white():
    editor.configure(bg='white',foreground='black',insertbackground='black')
    output_label.configure(bg='white',foreground='black')
    code_output.configure(bg='#e8fafc',foreground='black',insertbackground='black')
    file_label.configure(bg='white',foreground='red')
    background.configure(bg='white')
def Classic():
    output_label.configure(bg='#d1f4f9',foreground='red')
    editor.configure(bg='#d1f4f9',foreground='black',insertbackground='black')
    code_output.configure(bg='#c5f1f7',foreground='black',insertbackground='black')

background = Label(root,width=300,height=300)
background.place(x=0,y=0)

def setting():
    setting = Tk()
    setting.attributes('-alpha',0.97)
    setting.title("Setting")
    setting.geometry('300x30')
    setting.resizable(False,False)
    var = int()
    whitetheme = Radiobutton(setting,text="WhiteTheme",variable=var,value=1,command=white)
    whitetheme.place(x=10,y=0)
    DarkTheme = Radiobutton(setting,text="DarkTheme",variable=var,value=4,command=theme)
    DarkTheme.place(x=110,y=0)
    classictheme = Radiobutton(setting,text="Classic",variable=var,value=3,command=Classic)
    classictheme.place(x=210,y=0)
    setting.mainloop()

def style():
    style = Tk()
    style.attributes('-alpha',0.97)
    style.title("Gui Temeplete")
    style.geometry('300x530')
    style.resizable(False,False)
    background = Label(style,bg='hotpink',width=300,height=530)
    background.place(x=0,y=0)
    style.mainloop()
def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)
def delete():
    code_output.delete('1.0',END)
    editor.delete('1.0',END)
def make():
    inputValue=editor.get("1.0","end-1c")

file1 = PhotoImage(file='Rectangle.png')
file_label = Label(root,border=0,image = file1)
file_label.place(x=300,y=10)

file2 = PhotoImage(file='folder.png')
file_label2 = Button(root,border=0,bg='#F10A29',activebackground='#F10A29',image = file2,command=open_file)
file_label2.place(x=360,y=17)

file3 = PhotoImage(file='save.png')
file_label3 = Button(root,border=0,bg='#F10A29',activebackground='#F10A29',image = file3,command=save_as)
file_label3.place(x=410,y=17)

file4 = PhotoImage(file='play.png')
file_label4 = Button(root,border=0,bg='#F10A29',activebackground='#F10A29',image = file4,command=run)
file_label4.place(x=460,y=17)

file6 = PhotoImage(file='update.png')
file_label6 = Button(root,border=0,bg='#F10A29',activebackground='#F10A29',image = file6,command=check_updates)
file_label6.place(x=500,y=17)

file7 = PhotoImage(file='setting.png')
file_label7 = Button(root,border=0,bg='#F10A29',activebackground='#F10A29',image = file7,command=setting)
file_label7.place(x=540,y=17)

file8 = PhotoImage(file='delete.png')
file_label8 = Button(root,border=0,bg='#F10A29',activebackground='#F10A29',image = file8,command=delete)
file_label8.place(x=575,y=17)

file9 = PhotoImage(file='make.png')
file_label9 = Button(root,border=0,bg='#F10A29',activebackground='#F10A29',image = file9,command=Comingsoon)
file_label9.place(x=615,y=17)

file10 = PhotoImage(file='download.png')
file_label10 = Button(root,border=0,bg='#F10A29',activebackground='#F10A29',image = file10)
file_label10.place(x=660,y=17)
#textbox
editor = Text(root,border=0,bg='#FFB6C1',width=94,font=('semibold',14))
editor.place(x=0,y=70)

code_output = Text(root,border=0,bg='red',foreground='black',width=100,height=5,font=('bold',15))
code_output.place(x=0,y=588)

output_label = Label(root,text="Ouput:",foreground='black',font=('bold',15),bg='#FFB6C1')
output_label.place(x=0,y=558)

root.mainloop()