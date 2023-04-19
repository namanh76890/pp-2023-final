class Font_window(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        #Text
        self.title("Font")
        self.geometry("200x200")
        label = tk.Label(self, text ="Font", font = ('Helvetica', 14))
        label.pack()
        
        #Combobox
        self.fontMenu = ttk.Combobox(self, font=('Helvetica', 14), width = 20)
        self.fontMenu['value'] = ('Arial', 'Calibiri', 'Comic Sans', 'Helvetica', 'Monaco', 'Montserrat', 'Myriad Pro', 'Times New Roman')
        self.fontMenu.current(0)
        self.fontMenu.pack()
        
        #Button
        self.confirm_btn = tk.Button(
            self,
            bg = 'blue',
            fg = 'white',
            text = 'confirm',
            command = self.change_font,
        )
        self.confirm_btn.pack()
        
    def change_font(self):
        self.text_font = self.fontMenu.get()

class Text_size_window(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        #Text
        self.title("Size")
        self.geometry("200x200")
        label = tk.Label(self, text ="Size", font = ('Helvetica', 14))
        label.pack()
        
        #Combobox
        self.sizeMenu = ttk.Combobox(self, font=('Helvetica', 14), width = 20)
        self.sizeMenu['value'] = natural_numbers_tuple(self)
        self.sizeMenu.current(0)
        self.sizeMenu.pack()
        
        #Button
        self.confirm_btn = tk.Button(
            self,
            bg = 'blue',
            fg = 'white',
            text = 'confirm',
            command = self.change_size,
        )
        self.confirm_btn.pack()
        
    def change_size(self):
        self.text_size = self.sizeMenu.get()