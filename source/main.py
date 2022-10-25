from tkinter import *
from tkinter import DISABLED, INSERT, NORMAL
from tkinter import ttk
import tkinter
from tkinter.filedialog import asksaveasfile

# TKINTER WINDOW - GENERATE AND CONFIG
window = Tk()
window.title("README.md | MARKDOWN GENERATOR")
#window_icon = PhotoImage(file="favicon.png")
#window.iconphoto(False, window_icon)

#OUTPUT FRAME
frame = Frame()
frame.grid(column=3, sticky="E", rowspan=13)
out = Text(frame, width=57, height=30, background="lightgrey")
out.grid(column=3, sticky="W", rowspan=13, pady=5, padx=10)

# WINDOW GEOMETRY
window.geometry('1070x510')
window.minsize(width=1070, height=510)
window.maxsize(width=1070, height=510)

# MENUBAR
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Save", command=asksaveasfile)
filemenu.add_command(label="Save as...", command=asksaveasfile)
filemenu.add_command(label="Close", command=window.quit())

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)


# COMMAND FOR INITIALIZE BUTTON;
# THIS FUNCTION WILL CREATE A MD FILE AND \
# WILL APPEND THE TITLE AND HEADER TO THE DISPLAYBOX
def initialize():
    # Get the value of the title entry widget.
    title = title_entry.get()
    description = to_append.get("1.0", END)

    # Displays an error when the project was initialized without a title or a description.
    if title == "" or description == "":
        make_file_btn['state'] = NORMAL
        tkinter.messagebox.showerror("ERROR", "VERIFY ENTRIES in TITLE /DESCRIPTION ")
        title_entry.config(state="normal")

    # ELSE: Displays a success window, enable remaining buttons, and disables the title entry widget.
    else:
        tkinter.messagebox.showinfo("SUCCESS", f"SUCCESFULLY INITIALIZED {fname_entry.get()} FILE. {title}")
        make_file_btn.config(state="disabled")

        # ENABLE REST OF BUTTONS
        if (append_file_btn['state'] == NORMAL):
            append_file_btn['state'] = DISABLED
            save_file_btn['state'] = DISABLED
        else:
            append_file_btn['state'] = NORMAL
            save_file_btn['state'] = NORMAL
            # quit_file_btn['state'] = tk.NORMAL

        # CLEAR ENTRIES
        title_entry.config(state="disabled")
        to_append.delete("1.0", END)

        # WRITE AS THE README HEADER
        header_string = f'''
<!--HTTPS://DAVINCI-IT.GITHUB.IO-->
<!--READme.md TEMPLATE-->
---
# __{title}__
![image](https://img.shields.io/badge/Markdown-ffffff?style=for-the-badge&logo=markdown&logoColor=black)
![image](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
---
### __CONNECT WITH ME:__
<p align='center'>
<a href='https://twitter.com/It_vince01'>
<img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="twitter_link"/></a>
<a href='https://www.linkedin.com/in/vincent-de-torres-854612240/'>
<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin"/></a>
<a href='https://ko-fi.com/devinci'>
<img src="https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white" alt="kofi_link"/></a>
</p>
---
OVERVIEW
{description}
---
'''
        filename = fname_entry.get()
        fname_entry.config(state="disable")
        out.insert(INSERT, chars=header_string)


# COMMAND FOR APPEND BUTTON;
# THIS FUNCTION WILL CREATE PULL THE INPUT STRING \
# RE-FORMAT ACCORDING TO THE SELECTED OPTION FROM THE RADIOBUTTONS\
# INSERT TO THE OUTPUT FRAME.
def append():
    radio = rad.get()
    entry = to_append.get("1.0", END)

    # H2
    if radio == 'A':
        conf_entry = f'\n## __{entry.strip()}__\n'
        out.insert(INSERT, chars=conf_entry)
        to_append.delete("1.0", END)
    # H3
    elif radio == 'B':
        conf_entry = f'\n### __{entry.strip()}__\n'
        out.insert(INSERT, chars=conf_entry)
        to_append.delete("1.0", END)

    # H4
    elif radio == 'C':
        conf_entry = f'\n#### {entry.strip()}\n'
        out.insert(INSERT, chars=conf_entry)
        to_append.delete("1.0", END)

    # BULLET
    elif radio == 'D':
        conf_entry = f'\n-{entry.strip()}\n'
        out.insert(INSERT, chars=conf_entry)
        to_append.delete("1.0", END)

    # CODE
    elif radio == 'E':
        conf_entry = f'```\n{entry.strip()}\n```'
        out.insert(INSERT, chars=conf_entry)
        to_append.delete("1.0", END)

    # IMAGE
    elif radio == 'F':
        conf_entry = f'\n![image](./assets/img/{entry.strip()})\n'
        out.insert(INSERT, chars=conf_entry)
        to_append.delete("1.0", END)
    # elif rad =='F':
    # else:

#COMMAND FOR SAVE BUTTON;
def save_file(out=None):
    top_win = asksaveasfile(initialfile='READme.md', defaultextension=".md",
                      filetypes=[("All Files", "*.*"), ("Markdown File", "*.md")])
    top_win.writelines(out.get("1.0", END))

#GUI-USING TKINTER WIDGETS

#(0,0)
title = Label(window, text="READme.md |", font="SourceCode 25 bold", justify="center", foreground="#051821").grid(row=0,column=0,pady=10,padx=10)

#(1,1); FILE NAME LABEL & FILE NAME ENTRY
fname = Label(window, text="FILENAME .md")
fname_entry = Entry(window, width=55)

fname.grid(row=1, column=0, sticky=W)
fname_entry.grid(row=1, column=1, sticky=W)

fname_entry.insert(index=1, string="READme.md")

#(2,2); MARDOWN TITLE LABEL & ENTRY WIDGETS
md_title = Label(window, text="TITLE")
title_entry = Entry(window, width=55)

md_title.grid(row=2, column=0, sticky=W)
title_entry.grid(row=2, column=1, sticky=W)

# SEPERATOR
separator = Label(window, text=f"{'_' * 100}").grid(row=3, columnspan=3, sticky=W)

# APPEND ENTRY BOX
to_append = Text(window, width=57, height=10)
to_append.grid(row=4, columnspan=3, sticky=W, padx=10)

# RADIO OPTIONS
rad = StringVar()

r1 = Radiobutton(window, text='H2', variable=rad, value='A', tristatevalue=False)
r1.grid(row=5, column=0, sticky=W)

r2 = Radiobutton(window, text='H3', variable=rad, value='B', tristatevalue=False)
r2.grid(row=6, column=0, sticky=W)

r3 = Radiobutton(window, text='PARAGRAPH', variable=rad, value='C', tristatevalue=False)
r3.grid(row=7, column=0, sticky=W)

r4 = Radiobutton(window, text='BULLET', variable=rad, value='D', tristatevalue=False)
r4.grid(row=5, column=1, sticky=W)

r4 = Radiobutton(window, text='CODE', variable=rad, value='E', tristatevalue=False)
r4.grid(row=6, column=1, sticky=W)

r5 = Radiobutton(window, text='IMAGE', variable=rad, value='F', tristatevalue=False)
r5.grid(row=7, column=1, sticky=W)

# MAIN BUTTONS
make_file_btn = Button(window, text='INITIALIZE', font='SourceCodePro 12 bold', foreground="white", width=25,
                       command=initialize, background="#348493")
make_file_btn.grid(row=9, column=0, padx=1, pady=1, sticky=W)

append_file_btn = Button(window, text='APPEND', command=append, font='SourceCodePro 12 bold', foreground="white",
                         width=25, state="disabled", background="lightgrey")
append_file_btn.grid(row=10, column=0, sticky=W, padx=1, pady=1)

save_file_btn = Button(window, text='SAVE', command=lambda: save_file(), width=25, state="disabled",
                       font='SourceCodePro 12 bold', foreground="white", background="lightgrey")
save_file_btn.grid(row=9, column=1, sticky=W, padx=1, pady=1)

#MAINLOOP
window.config(menu=menubar)
window.mainloop()

