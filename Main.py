import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.geometry("700x700")
window.title("PyPad")

class tools():
    def __init__(self):
        self.font = "Arial"
        self.fontsize = 12
        self.fontType = ""
        self.savelocation = ""

    def save(self):    
        if(self.savelocation == ""):
            self.save_as()
        else:
            t = editor.get("1.0", "end-1c")
            file_ = open(self.savelocation, "w+")
            file_.write(t)
            file_.close()

    def save_as(self):
        t = editor.get("1.0", "end-1c")
        self.savelocation = filedialog.asksaveasfilename()
        file_ = open(self.savelocation, "w+")
        file_.write(t)
        file_.close()

    def open(self):
        editor.delete("1.0", "end")
        file_ = open(filedialog.askopenfilename() , 'r')
        if file_ != '':
            txt = file_.read()
            editor.insert("insert",txt)
            file_.close()
        else:
            pass


    def change_fonts(self, fontchange):
        self.font = fontchange
        if(self.fontType != ""):
            editor.config(font = (self.font, self.fontsize, self.fontType))
        else:
            editor.config(font = (self.font, self.fontsize))
    
    def change_fontsizeEvent(self, var, entry):
        self.fontsize = var.get()
        entry.destroy()
        try:
            if(self.fontType != ""):
                editor.config(font = (self.font, self.fontsize, self.fontType))
            else:
                editor.config(font = (self.font, self.fontsize))
        except tk.TclError:
            pass
        
    def delEntryTextEvent(self, event, ix):
        ix.set("")
    
    def change_fontsize(self):
        i = tk.StringVar()
        input_ = tk.Entry(window, textvariable = i)
        input_.insert(0, "(Integer) Enter to apply")
        input_.bind("<FocusIn>", lambda event, ix = i: self.delEntryTextEvent(event, ix))
        input_.bind("<Return>", lambda event, var = i, entry = input_: self.change_fontsizeEvent(var, entry))
        input_.place(x = 0, y = 0)
        
    def change_fontType(self, type_):
        if(type_ == "italic"):
            if(self.fontType == ""):
                self.fontType += "italic "
            else:
                self.fontType += " italic"
        elif(type_ == "bold"):
            if(self.fontType == ""):
                self.fontType += "bold "
            else:
                self.fontType += " bold"
        elif(type_ == "underline"):
            if(self.fontType == ""):
                self.fontType += "underline "
            else:
                self.fontType += " underline"
        elif(type_ == ""):
            self.fontType = ""
        if(self.fontType != ""):
            editor.tag_configure("style", font = (self.font, self.fontsize, type_))
            try:
                editor.tag_add("style", "sel.first", "sel.last")
            except tk.TclError:
                editor.config(font = (self.font, self.fontsize, self.fontType))
        else:
            editor.tag_remove("style", "1.0", "end")
            editor.config(font = (self.font, self.fontsize))

utils = tools()

global editor
editor = tk.Text(window, height = 700, width = 99)
editor.grid()

MenuBar = tk.Menu(window)
FileMenu = tk.Menu(MenuBar, tearoff = 0)
Style = tk.Menu(MenuBar, tearoff = 0)
Fontx = tk.Menu(MenuBar, tearoff = 0)
FontType = tk.Menu(MenuBar, tearoff = 0)

FileMenu.add_command(label = "Open", command = utils.open)
FileMenu.add_command(label = "Save", command = utils.save)
FileMenu.add_command(label = "Save As", command = utils.save_as)


Fontx.add_command(label = "Helvetica", command = lambda: utils.change_fonts("Helvetica"))
Fontx.add_command(label = "Comic Sans", command = lambda: utils.change_fonts("Comic Sans"))
Fontx.add_command(label = "Arial", command = lambda: utils.change_fonts("Arial"))
Fontx.add_command(label = "Times", command = lambda: utils.change_fonts("Times"))
Fontx.add_command(label = "Courier", command = lambda: utils.change_fonts("Courier"))
Fontx.add_command(label = "Verdana", command = lambda: utils.change_fonts("Verdana"))

FontType.add_command(label = "Bold", command = lambda: utils.change_fontType("bold"))
FontType.add_command(label = "Italic", command = lambda: utils.change_fontType("italic"))
FontType.add_command(label = "Underline", command = lambda: utils.change_fontType("underline"))
FontType.add_command(label = "Reset", command = lambda: utils.change_fontType(""))


Style.add_cascade(label = "Font", menu = Fontx)
Style.add_cascade(label = "Font Options", menu = FontType)
Style.add_command(label = "Font Size", command = utils.change_fontsize)

MenuBar.add_cascade(label="File", menu = FileMenu)
MenuBar.add_cascade(label="Styling", menu = Style)

window.config(menu = MenuBar)

window.mainloop()