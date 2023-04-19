import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import datetime
from tkinter import filedialog
from tkinter import scrolledtext

class ModernMenu(tk.Tk):
    def __init__(self, root):
        self.window = root
        self.window.title("Citation Management System")
        self.window.geometry("800x600")

        # Define the color themes
        self.color_themes = [
            {
                "background": "#F8F8F8",
                "title_bg": "#E0FFFF",
                "title_text": "#333333",
                "button_bg": "#008B8B",
                "button_fg": "#FFFFFF",
                "button_font": ("Helvetica", 16),
                "menu_item_hover": "#F0F8FF",
                "menu_item_active": "#00BFFF",
                "menu_item_border": "#00CED1",
                "button_exit_bg": "#DC143C"
            },
            {
                "background": "#F4F4F4",
                "title_bg": "#FFFFFF",
                "title_text": "#333333",
                "button_bg": "#008080",
                "button_fg": "#FFFFFF",
                "button_font": ("Helvetica", 16),
                "menu_item_hover": "#E2E2E2",
                "menu_item_active": "#72A0A5",
                "menu_item_border": "#4B696D",
                "button_exit_bg": "#C0392B"
            },
            {
                "background": "#2F2F2F",
                "title_bg": "#212121",
                "title_text": "#FFFFFF",
                "button_bg": "#008080",
                "button_fg": "#FFFFFF",
                "button_font": ("Helvetica", 16),
                "menu_item_hover": "#4B696D",
                "menu_item_active": "#72A0A5",
                "menu_item_border": "#4B696D",
                "button_exit_bg": "#C0392B"
            }
        ]

        self.color_theme_index = 0
        self.color_theme = self.color_themes[self.color_theme_index]
        self.window.configure(bg=self.color_theme["background"])

        # Create the title label
        self.title_label = tk.Label(
            self.window,
            text="Citation Management System",
            font=("Helvetica", 28, "bold"),
            fg=self.color_theme["title_text"],
            bg=self.color_theme["title_bg"],
            pady=10
        )
        self.title_label.pack(fill=tk.X)

        # Create the frame for the menu items
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(pady=20)

        # Create the menu items
        self.menu_item_1 = tk.Button(
            self.menu_frame,
            text="New Text Box",
            font=self.color_theme["button_font"],
            bg=self.color_theme["button_bg"],
            fg=self.color_theme["button_fg"],
            width=20,
            height=5,
            borderwidth=0,
            activebackground=self.color_theme["menu_item_active"],
            activeforeground=self.color_theme["button_fg"],
            highlightthickness=0,
            command=self.open_Text_box_for_citation
        )
        self.menu_item_1.grid(row=0, column=0, padx=10, pady=10)

        self.menu_item_2 = tk.Button(
            self.menu_frame,
            text="Open Text Box",
            font=self.color_theme["button_font"],
            bg=self.color_theme["button_bg"],
            fg=self.color_theme["button_fg"],
            width=20,
            height=5,
            borderwidth=0,
            activebackground=self.color_theme["menu_item_active"],
            activeforeground=self.color_theme["button_fg"],
            highlightthickness=0,
            command = Text_box_for_citation(tk.Toplevel()).open_file(self)
        )
        self.menu_item_2.grid(row=0, column=1, padx=10, pady=10)

        self.menu_item_3 = tk.Button(
            self.menu_frame,
            text="Library",
            font=self.color_theme["button_font"],
            bg=self.color_theme["button_bg"],
            fg=self.color_theme["button_fg"],
            width=20,
            height=5,
            borderwidth=0,
            activebackground=self.color_theme["menu_item_active"],
            activeforeground=self.color_theme["button_fg"],
            highlightthickness=0
        )
        self.menu_item_3.grid(row=0, column=2, padx=10, pady=10)

        self.menu_item_4 = tk.Button(
            self.menu_frame,
            text="Preference",
            font=self.color_theme["button_font"],
            bg=self.color_theme["button_bg"],
            fg=self.color_theme["button_fg"],
            width=20,
            height=5,
            borderwidth=0,
            activebackground=self.color_theme["menu_item_active"],
            activeforeground=self.color_theme["button_fg"],
            highlightthickness=0,
            command=self.toggle_color_theme
        )
        self.menu_item_4.grid(row=1, column=0, padx=10, pady=10)
        
        self.menu_item_5 = tk.Button(
            self.menu_frame,
            text="About us",
            font=self.color_theme["button_font"],
            bg=self.color_theme["button_bg"],
            fg=self.color_theme["button_fg"],
            width=20,
            height=5,
            borderwidth=0,
            activebackground=self.color_theme["menu_item_active"],
            activeforeground=self.color_theme["button_fg"],
            highlightthickness=0
        )
        self.menu_item_5.grid(row=1, column=1, padx=10, pady=10)
        
        self.menu_item_6 = tk.Button(
            self.menu_frame,
            text="Exit",
            font=self.color_theme["button_font"],
            bg=self.color_theme["button_exit_bg"],
            fg=self.color_theme["button_fg"],
            width=20,
            height=5,
            borderwidth=0,
            activebackground=self.color_theme["menu_item_active"],
            activeforeground=self.color_theme["button_fg"],
            highlightthickness=0,
            command=self.window.destroy
        )
        self.menu_item_6.grid(row=1, column=2, padx=10, pady=10)
        
    def toggle_color_theme(self):
        self.color_theme_index = (self.color_theme_index + 1) % len(self.color_themes)
        self.color_theme = self.color_themes[self.color_theme_index]
        self.window.configure(bg=self.color_theme["background"])
        self.title_label.configure(fg=self.color_theme["title_text"], bg=self.color_theme["title_bg"])
        self.menu_item_1.configure(bg=self.color_theme["button_bg"], activebackground=self.color_theme["menu_item_active"])
        self.menu_item_2.configure(bg=self.color_theme["button_bg"], activebackground=self.color_theme["menu_item_active"])
        self.menu_item_3.configure(bg=self.color_theme["button_bg"], activebackground=self.color_theme["menu_item_active"])
        self.menu_item_4.configure(bg=self.color_theme["button_bg"], activebackground=self.color_theme["menu_item_active"])
        self.menu_item_5.configure(bg=self.color_theme["button_bg"], activebackground=self.color_theme["menu_item_active"])
        self.menu_item_6.configure(bg=self.color_theme["button_exit_bg"], activebackground=self.color_theme["menu_item_active"])

    def open_Text_box_for_citation(self):
        Text_box_for_citation(self.window)
        
#separated

class Text_box_for_citation(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Text box for citation")
        self.geometry("800x600")

        # Create a menu bar
        self.menuBar = tk.Menu(self)

        # Create the File menu
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0, activebackground = 'red', activeforeground = 'yellow')
        self.fileMenu.add_command(label="New", command=self.new_file)
        self.fileMenu.add_command(label="Open", command=self.open_file)
        self.fileMenu.add_command(label="Save", command=self.save_file)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.quit)
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
        self.add_citation.add_command(label="Add Citation")
        self.menuBar.add_cascade(label="Add Citation", menu=self.add_citation)
        
        # Create Add Bibliography
        self.add_bibliography = tk.Menu(self.menuBar, tearoff = 0)
        self.add_bibliography.add_command(label="Add Bibliography")
        self.menuBar.add_cascade(label="Add Bibliography", menu=self.add_bibliography)
        
        #Create Citation Styles
        self.citation_styles = tk.Menu(self.menuBar, tearoff = 0)
        self.citation_styles.add_command(label="Citation styles")
        self.menuBar.add_cascade(label="Citation Styles", menu=self.citation_styles)
        
        # Add the menu bar to the window
        self.config(menu=self.menuBar)
        
        #Create Top blue bar
        self.text_modifyArea = tk.Frame(
            self,
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
        self.font_combobox_text.grid(row=0,column=0,ipadx=10)

        #Create Font combobox
        self.font_combobox = ttk.Combobox(
            self.text_modifyArea,
            font = ('Helvetica',12), width = 12
        )
        self.font_combobox['value'] = ('Arial','BEBAS NEUE','Calibri','Comic Sans MS','.VnArial','.VnVogue','Helvetica', 'Impact','Merriweather','Monaco', 'Times New Roman')
        self.font_combobox.current(6)
        self.font_combobox.grid(row=0,column=1,ipadx=20)

        #Create Size text for combobox
        self.size_combobox_text = tk.Label(
            self.text_modifyArea,
            bg = 'blue',
            fg = 'white',
            text = 'Size',
            font = ('Helvetica',15)
        ) 
        self.size_combobox_text.grid(row=0,column=2,ipadx=30)

        # Create Size combobox
        self.size_combobox = ttk.Combobox(
            self.text_modifyArea,
            font=('Helvetica', 12),
            width=3
        )
        self.size_combobox['values'] = list(range(1, 1001))
        self.size_combobox.current(11)
        self.size_combobox.grid(row=0, column=3, ipadx=10)

        # Create a scrolled text widget
        self.textArea = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=('Helvetica', 12))
        self.textArea.pack(fill=tk.BOTH, expand=True)

        # Bind the ComboboxSelected event to update_font function
        def update_font(event):
            font_name = self.font_combobox.get()
            self.textArea.configure(font=(font_name, 12))

        self.font_combobox.bind("<<ComboboxSelected>>", update_font)

        # Bind the ComboboxSelected event to update_font_size function
        def update_font_size(event):
            font_name = self.font_combobox.get()
            font_size = int(self.size_combobox.get())
            self.textArea.configure(font=(font_name, font_size))

        self.size_combobox.bind("<<ComboboxSelected>>", update_font_size)

        
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


        
if __name__ == "__main__":
    root = tk.Tk()
    modern_menu = ModernMenu(root)
    root.mainloop()