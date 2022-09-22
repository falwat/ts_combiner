"""
Mainwindow class.

Mainwindow contain a empty menubar, toolbar, statusbar and mainframe.
You can create your own Mainwindow inherited from this.

Copyright (c) 2022 falwat<falwat@163.com>, under MIT licence.
"""

from tkinter import *
from tkinter import ttk

class Mainwindow(Tk):
    """
    Basic Mainwindow that contain a empty menubar, toolbar, statusbar 
    and mainframe.
    """
    def __init__(self) -> None:
        super().__init__()

        # tool bar
        self.toolbar = ttk.Frame(self, padding='3 3 3 3')
        # mainframe. 
        # all widget need to add to mainframe, 
        # except menubar item, toolbar item and statusbar item
        self.mainframe = ttk.Frame(self, padding='3 3 3 3')
        # status bar
        self.statusbar = ttk.Frame(self, padding='3 3 3 0')

        self.toolbar.grid(column=0, row=0, sticky=NSEW)
        self.mainframe.grid(column=0, row=1, sticky=NSEW)
        self.statusbar.grid(column=0, row=2, sticky=NSEW)

        self.option_add('*tearOff', FALSE)
        # Create Menubar
        win = self.winfo_toplevel()
        self.menubar = Menu(win)
        win['menu'] = self.menubar

        self.statusmsg = StringVar()
        self.statusLabel = Label(self.statusbar, textvariable=self.statusmsg)
        self.statusLabel.grid(column=0, row=0, sticky=SW)

        self.toolbar.rowconfigure(0, weight=1)
        self.statusbar.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
    
    def showmessage(self, msg : str):
        self.statusmsg.set(msg)


class Demo(Mainwindow):
    """
    Demo window inherited from Mainwindow.
    """
    def __init__(self):
        super().__init__()
        # set window's title.
        self.title('Demo')
        # set window's geometry size
        self.geometry('600x400')
        self.showmessage('Ready.')

if __name__ == '__main__':
    mw = Demo()
    mw.mainloop()
    