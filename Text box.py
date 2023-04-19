import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk

def text_style(self):
        self.text_font = "Helvetica"
        self.text_size = 12

def natural_numbers_tuple():
    intTuple = ()
    for i in range(1, 99):
        intTuple += (i,)
    return intTuple

        
class Text_box_for_citation:
    def __init__(self, window):
        self.window = window
        self.window.title("Text box for citation")
        self.window.geometry("800x600")

        # Create a menu bar
        self.menuBar = tk.Menu(self.window)

        # Create the File menu
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0, activebackground = 'red', activeforeground = 'yellow', bg = 'blue')
        self.fileMenu.add_command(label="New", command=self.new_file)
        self.fileMenu.add_command(label="Open", command=self.open_file)
        self.fileMenu.add_command(label="Save", command=self.save_file)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.window.quit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        # Create the Edit menu
        self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label="Cut", command=self.cut)
        self.editMenu.add_command(label="Copy", command=self.copy)
        self.editMenu.add_command(label="Paste", command=self.paste)
        self.editMenu.add_command(label="Delete all", command=self.delete_all)
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)
        
        # Create Add Citation
        self.add_citation = tk.Menu(self.menuBar, tearoff = 0)
        self.add_citation.add_command(label="Add Citation", command=self.add_citation_command)
        self.menuBar.add_cascade(label="Add Citation", menu=self.add_citation)
        
        self.citation_counter = 0
        
        # Create Add Bibliography
        self.add_bibliography = tk.Menu(self.menuBar, tearoff = 0)
        self.add_bibliography.add_command(label="Add Bibliography")
        self.menuBar.add_cascade(label="Add Bibliography", menu=self.add_bibliography)
        
        #Create Citation Styles
        self.citation_styles = tk.Menu(self.menuBar, tearoff = 0)
        self.citation_styles.add_command(label="Citation styles")
        self.menuBar.add_cascade(label="Citation Styles", menu=self.citation_styles)
        
        # Add the menu bar to the window
        self.window.config(menu=self.menuBar)
        
        #Create Top blue bar
        self.text_modifyArea = tk.Frame(
            self.window,
            height = 30,
            bg = 'blue'
        )
        self.text_modifyArea.pack(fill = tk.X, side = tk.TOP)

        #Create Font text for combobox
        self.font_combobox_text = tk.Label(
            self.text_modifyArea,
            bg = 'blue',
            fg = 'white',
            text = 'Font',
            font = ('Helvetica',15)
        ) 
        self.font_combobox_text.grid(row=0,column=0,ipadx=20)
        
        #Create Font combobox
        self.font_combobox = ttk.Combobox(
            self.text_modifyArea,
            font = ('Helvetica',12), width = 12
        )
        self.font_combobox['value'] = ('Arial', 'Calibiri', 'Comic Sans', 'Helvetica', 'Monaco', 'Montserrat', 'Myriad Pro', 'Times New Roman')
        self.font_combobox.current(0)
        self.font_combobox.grid(row=0,column=1,ipadx=20)
        
        # Create a scrolled text widget
        text_style(self)
        self.textArea = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=(self.text_font, self.text_size))
        self.textArea.pack(fill=tk.BOTH, expand=True)
    
    def add_citation_command(self):
        self.citation_counter += 1
        citation_text = f"({self.citation_counter})"
        self.textArea.insert(tk.INSERT, citation_text)
        self.new_window()

    def new_window(self):
        new_window = tk.Toplevel(self.window)
        new_window.geometry("200x200")
        new_window.title(f"Citation {self.citation_counter}")
        
    def new_file(self):
        self.textArea.delete("1.0", tk.END)

    def open_file(self):
        filePath = tk.filedialog.askopenfilename()
        with open(filePath, "r") as file:
            fileContents = file.read()
            self.textArea.delete("1.0", tk.END)
            self.textArea.insert(tk.END, fileContents)

    def save_file(self):
        filePath = tk.filedialog.asksaveasfilename(defaultextension=".txt")
        with open(filePath, "w") as file:
            fileContents = self.textArea.get("1.0", tk.END)
            file.write(fileContents)

    def cut(self):
        self.textArea.event_generate("<<Cut>>")

    def copy(self):
        self.textArea.event_generate("<<Copy>>")

    def paste(self):
        self.textArea.event_generate("<<Paste>>")
    
    def delete_all(self):
        self.textArea.delete(1.0, tk.END)
        
        
if __name__ == '__main__':
    window = tk.Tk()
    Text_box_for_citation(window)
    window.mainloop()