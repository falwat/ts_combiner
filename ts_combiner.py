"""
TSCombiner class.

Copyright (c) 2022 falwat<falwat@163.com>, under MIT licence.
"""

import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from mainwindow import Mainwindow


class TSCombiner(Mainwindow):
    """
    TS Combiner.

    Combine multiple TS files into a single TS file.
    """
    def __init__(self):
        super().__init__()

        ttk.Label(self.mainframe, text='Input Filenames:').grid(row=0, column=0, sticky=NE)
        self.tree = ttk.Treeview(self.mainframe)
        self.tree.grid(column=1, row=0, sticky=NSEW)
        ttk.Button(self.mainframe, text='...', command=self.select_infiles).grid(row=0, column=2, sticky=N)

        ttk.Label(self.mainframe, text='Output Filename:').grid(row=1, column=0, sticky=S)
        self.outfileVar = StringVar()
        self.outfileEntry = ttk.Entry(self.mainframe, textvariable=self.outfileVar)
        self.outfileEntry.grid(row=1, column=1, sticky=NSEW)
        ttk.Button(self.mainframe, text='...', command=self.select_outfile).grid(row=1, column=2, sticky=NSEW)

        self.deleteInfilesVar = BooleanVar()
        ttk.Checkbutton(self.mainframe, text='Delete Input Files', variable=self.deleteInfilesVar).grid(row=2, column=1, sticky=W)
        
        ttk.Button(self.mainframe, text='Run', command=self.run).grid(row=2, column=2, sticky=NSEW)

        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=3, pady=3)

        # set window's title.
        self.title('TS Combiner')
        # set window's geometry size
        self.geometry('800x600')
        self.showmessage('Ready.')
    
    def select_infiles(self):
        self.infiles = filedialog.askopenfilenames()
        if len(self.infiles) > 0:
            self.remove_all()
        for fn in self.infiles:
            self.tree.insert('', 'end', text=fn) 

    def select_outfile(self):
        self.outfile = filedialog.asksaveasfilename()
        self.outfileVar.set(self.outfile)

    def remove_all(self):
        top_items = self.tree.get_children()
        for item in top_items:
            self.tree.delete(item)

    def run(self):
        outfile = self.outfileVar.get()
        if len(outfile) == 0:
            messagebox.showerror('Error', 'The output filename can not be empty!')
            return
        with open(outfile, 'wb') as fout:
            for fn in self.infiles:
                with open(fn, 'rb') as fin:
                    data = fin.read()
                    fout.write(data)
                if self.deleteInfilesVar.get():
                    os.remove(fn)
        messagebox.showinfo('Info', 'Process Done!')

if __name__ == '__main__':
    mw = TSCombiner()
    mw.mainloop()