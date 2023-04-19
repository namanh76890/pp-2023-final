import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import datetime
from tkinter import filedialog
from tkinter import scrolledtext
import win32com.client as win32
import os
import win32api
from image_button import load_image
#from PIL import ImageTk, Image

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
            command=self.open_Text_box
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
            highlightthickness=0,
            command=self.open_CitationManagerApp
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
            highlightthickness=0,
            command=self.open_InfoWindow
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
        
    def open_CitationManagerApp(self):
        CitationManagerApp(self.window)
        
    def open_InfoWindow(self):
        InfoWindow(self.window)
        
    def open_Text_box(self):
        citation_box = Text_box_for_citation(self.window)
        citation_box.open_file()

        
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
        self.add_citation.add_command(label="Add Citation", command=self.add_citation_command)
        self.menuBar.add_cascade(label="Add Citation", menu=self.add_citation)
        
        self.citation_counter = 0
        
        # Create Add Bibliography
        self.add_bibliography = tk.Menu(self.menuBar, tearoff = 0)
        self.add_bibliography.add_command(label="Add Bibliography", command=self.generate_bibliography_window)
        self.menuBar.add_cascade(label="Add Bibliography", menu=self.add_bibliography)
        
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
        self.font_combobox['value'] = ('Helvetica', 'System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Bebas Neue', 'Lutschine ExtraBold Con x1', 'Lutschine Con x1', 'Dancing Script OT', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Text', 'Sitka Subheading', 'Sitka Heading', 'Sitka Display', 'Sitka Banner', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight', 'HoloLens MDL2 Assets', 'VNI-Vari', 'VNI-Allegie', 'VNI-Aptima', 'VNI-Ariston', 'VNI-Auchon', 'VNI-Avo', 'VNI-Awchon', 'VNI-Aztek', 'VNI-Bandit', 'VNI-Bodon', 'VNI-Bodon-Poster', 'VNI-Book', 'VNI-Broad', 'VNI-Brush', 'VNI-Centur', 'VNI-Commerce', 'VNI-Cooper', 'VNI-Coronet', 'VNI-Couri', 'VNI-Dom', 'VNI-Duff', 'VNI-Dur', 'VNI-Fato', 'VNI-Franko', 'VNI-Free', 'VNI-Garam', 'VNI-Goudy', '.VnBook-AntiquaH', '.VnArabiaH', '.VnArialH', '.VnArial NarrowH', '.VnAristoteH', '.VnAvantH', '.VnBahamasBH', '.VnBlackH', '.VnBodoniH', '.VnCentury SchoolbookH', '.VnClarendonH', '.VnCommercial ScriptH', '.VnCooperH', '.VnMonotype corsivaH', '.VnCourier NewH', 'VNI-Helve-Condense', 'VNI-Helve', '.VnExoticH', '.VnFreeH', '.VnGothicH', '.VnHelvetInsH', '.VnKoalaH', '.VnLincolnH', '.VnLinusH', '.VnMemorandumH', '.VnMysticalH', 'VNI-Hobo', '.VnParkH', '.VnPresentH', '.VnRevueH', '.VnSouthernH', '.VnTeknicalH', '.VnTifani HeavyH', '.VnTimeH', '.VnUniverseH', '.VnVogueH', 'Vinhan', 'VNI-Jamai', 'VNI-Juni', 'VNI-Korin', 'VNI-Kun', 'VNI-Linus', 'VNI-Lithos', 'VNI-Maria', 'VNI-Meli', 'VNI-Murray', '.Vn3DH', '.VnBook-Antiqua', '.VnArabia', '.VnArial', '.VnArial Narrow', '.VnAristote', '.VnAvant', '.VnBahamasB', '.VnBlack', '.VnBodoni', '.VnCentury Schoolbook', '.VnClarendon', '.VnCommercial Script', '.VnCooper', '.VnMonotype corsiva', '.VnCourier New', '.VnCourier', '.VnExotic', '.VnFree', '.VnGothic', 'VNI-Harrington', '.VnHelvetIns', 'VNI-HLThuphap', 'Vni 01 LinotypeZapfino one', 'Vni 02 LinotypeZapfino two', 'Vni 03 LinotypeZapfino Three', 'Vni 04 LinotypeZapfino four', 'Vni 05 SpringtimeFlourish', 'VNI 06 Springtime', 'Vni 07 WaterBrushROB', 'VNI 08 Springtime2', 'VNI 09 Baroque ', 'Vni 10 Swan Song', 'Vni 11 Springtime2', 'Vni 12 Alex', 'Vni 13 Annabelle', 'Vni 14 AlexBrush', 'VNI 15 Chops', 'Vni 16 Machina', 'Vni 17 Sandy', 'Vni 18 Mandalay', 'Vni 19 Walt Disney', 'Vni 20 University', 'Vni 21 Scrap Cursive', 'VNI 22 JackieO', 'Vni 23 Qwigley', 'VNI 24 Love', 'Vni 25 Ambiance BT Swash', 'VNI 26 Saliere', 'VNI 27 Bendigo', 'VNI 28 Zirkon', 'Vni 29 BrushMe', 'Vni 30 Shishoni Brush', 'VNI-Baybuom', 'VNI-Briquet', 'VNI-Butlong', 'VNI Cambodia', 'VNI-Disney', 'VNI-Diudang', 'VNI-DOS Sample Font ', 'VNI Greece', 'VNI Laos', 'VNI-Matisse', 'VNI-Internet Mail', 'VNI-Netbut', 'VNI-Nhatban', 'VNI-OngDoHL', 'VNI Russia', 'VNI-Script', 'VNI-Silver', 'VNI-Slogan', 'VNI-Souvir', 'VNI-Thanhcao', 'VNI-Thufapfan', 'VNI-Thufap1', 'VNI-Thufap2', 'VNI-Thufap3', 'VNI-Top', 'VNI-Truck', 'VNI-Trung Kien', 'VNI-Tubes', 'VNI-Univer', 'VNI-Viettay', 'VNI-Vivi', 'VNI-Whimsy', 'VNI-WIN Sample Font', 'VNI-Yahoo', 'VNI-Zap', '.VnKoala', '.VnLincoln', '.VnLinus', '.VnLucida sans', '.VnMemorandum', '.VnMystical', '.VnPark', '.VnPresent', '.VnRevue', '.VnShelley Allegro', '.VnSouthern', '.VnTifani Heavy', '.VnTime', '.VnUniverse', '.VnVogue', 'VNI-Palatin', 'VNI-Park', 'VNI-Present', 'VNI-Revue', 'VNI-Swiss-Condense', 'VNI-Tekon', 'VNI-Times', 'MT Extra', 'Arial Unicode MS', '@Arial Unicode MS', 'Century', 'Wingdings 2', 'Wingdings 3', 'Book Antiqua', 'Century Gothic', 'Haettenschweiler', 'MS Outlook', 'Tempus Sans ITC', 'Mistral', 'Lucida Handwriting', 'Kristen ITC', 'Juice ITC', 'Freestyle Script', 'Arial Narrow', 'Garamond', 'Monotype Corsiva', 'Algerian', 'Baskerville Old Face', 'Bauhaus 93', 'Bell MT', 'Berlin Sans FB', 'Bernard MT Condensed', 'Bodoni MT Poster Compressed', 'Britannic Bold', 'Broadway', 'Brush Script MT', 'Californian FB', 'Centaur', 'Chiller', 'Colonna MT', 'Cooper Black', 'Footlight MT Light', 'Harlow Solid Italic', 'Harrington', 'High Tower Text', 'Jokerman', 'Kunstler Script', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Magneto', 'Matura MT Script Capitals', 'Modern No. 20', 'Niagara Engraved', 'Niagara Solid', 'Old English Text MT', 'Onyx', 'Parchment', 'Playbill', 'Poor Richard', 'Ravie', 'Informal Roman', 'Showcard Gothic', 'Snap ITC', 'Stencil', 'Viner Hand ITC', 'Vivaldi', 'Vladimir Script', 'Wide Latin', 'Bookman Old Style', 'Bookshelf Symbol 7', 'MS Reference Sans Serif', 'MS Reference Specialty', 'Berlin Sans FB Demi', 'Merriweather Black', 'Merriweather', 'Merriweather Light')
        self.font_combobox.current(0)
        self.font_combobox.grid(row=0,column=1,ipadx=20)

        #Create Size text for combobox
        self.size_combobox_text = tk.Label(
            self.text_modifyArea,
            bg = 'blue',
            fg = 'white',
            text = 'Size',
            font = ('Helvetica',15)
        ) 
        self.size_combobox_text.grid(row=0,column=2,ipadx=10)

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
        self.textArea.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

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

        #Create Align text for combobox
        self.align_text = tk.Label(
            self.text_modifyArea,
            bg = 'blue',
            fg = 'white',
            text = 'Align',
            font = ('Helvetica',15)
        ) 
        self.align_text.grid(row=0,column=4,ipadx=10)
        
        # Create Align buttons
        self.leftAlignButton = tk.Button(
            self.text_modifyArea,
            bg = 'white',
            fg = 'blue',
            text="Left",
            font=('Helvetica', 12, 'bold'),
            relief=tk.FLAT,
            command=self.left_align
        )
        self.leftAlignButton.grid(row=0, column=5, ipadx=10)

        self.centerAlignButton = tk.Button(
            self.text_modifyArea,
            bg = 'white',
            fg = 'blue',
            text="Center",
            font=('Helvetica', 12, 'bold'),
            relief=tk.FLAT,
            command=self.center_align
        )
        self.centerAlignButton.grid(row=0, column=6, ipadx=10)

        self.rightAlignButton = tk.Button(
            self.text_modifyArea,
            bg = 'white',
            fg = 'blue',
            text="Right",
            font=('Helvetica', 12, 'bold'),
            relief=tk.FLAT,
            command=self.right_align
        )
        self.rightAlignButton.grid(row=0, column=7, ipadx=10)
        
        # Create Insert to Word
        self.Insert_to_Word = tk.Button(
            self,
            bg = 'blue',
            fg = 'white',
            text="Insert to Word",
            font=('Helvetica', 18, 'bold'),
            relief=tk.FLAT,
            command=self.add_to_word
        )
        self.Insert_to_Word.pack(expand=True, padx=10, pady=5)
        
        # Create Save image
        self.saved_btn_img = load_image("D:/Git/python/diskette.png", 30, 30)
        
        # Create Save button
        self.save_btn = tk.Button(
            self.text_modifyArea,
            text="",
            compound="center",  # This will center the text on top of the image
            borderwidth=0,
            padx=10,
            pady=10,
            image = self.saved_btn_img,
            bg = 'white',
            fg = 'white',
            command = self.save_file,
        ) 
        self.save_btn.grid(row = 0, column = 8, ipadx=10, padx = 40)
        #Create add bibliography style
        self.bibliography_style_var = tk.StringVar()
        self.bibliography_style_var.set("APA")
    
    def generate_bibliography(self):
        style = self.bibliography_style_var.get()
        bibliography = self.manager.generate_bibliography(style)

        # Tạo cửa sổ mới để hiển thị danh mục tài liệu tham khảo
        bibliography_win = tk.Toplevel(self)
        bibliography_win.title("Bibliography")

        bibliography_text = tk.Text(bibliography_win, wrap=tk.WORD)
        bibliography_text.pack(padx=10, pady=10)

        for entry in bibliography:
            bibliography_text.insert(tk.END, entry + "\n\n")

        close_button = ttk.Button(bibliography_win, text="Close", command=bibliography_win.destroy)
        close_button.pack(pady=10)
    def generate_bibliography_window(self):
        generate_bibliography_win = tk.Toplevel(self)
        generate_bibliography_win.title("Generate Bibliography")

        style_label = ttk.Label(generate_bibliography_win, text="Style:")
        style_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        style_combobox = ttk.Combobox(generate_bibliography_win, textvariable=self.bibliography_style_var, values=["APA", "MLA", "Chicago"])
        style_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        generate_button = ttk.Button(generate_bibliography_win, text="Generate", command=self.generate_bibliography)
        generate_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        style_var = tk.StringVar(generate_bibliography_win)
        style_var.set("APA")
        style_combobox.grid()
        
    def open_CitationManagerApp(self):
        CitationManagerApp(self)    

    def left_align(self):
        if self.textArea.tag_ranges("sel"):
            current_tags = self.textArea.tag_names("sel.first")
            if "left" in current_tags:
                self.textArea.tag_remove("left", "sel.first", "sel.last")
            else:
                self.textArea.tag_remove("center", "sel.first", "sel.last")
                self.textArea.tag_remove("right", "sel.first", "sel.last")
                self.textArea.tag_add("left", "sel.first", "sel.last")
                self.textArea.tag_configure("left", justify="left")

    def center_align(self):
        if self.textArea.tag_ranges("sel"):
            current_tags = self.textArea.tag_names("sel.first")
            if "center" in current_tags:
                self.textArea.tag_remove("center", "sel.first", "sel.last")
            else:
                self.textArea.tag_remove("left", "sel.first", "sel.last")
                self.textArea.tag_remove("right", "sel.first", "sel.last")
                self.textArea.tag_add("center", "sel.first", "sel.last")
                self.textArea.tag_configure("center", justify="center")
    
    def right_align(self):
        if self.textArea.tag_ranges("sel"):
            current_tags = self.textArea.tag_names("sel.first")
            if "right" in current_tags:
                self.textArea.tag_remove("right", "sel.first", "sel.last")
            else:
                self.textArea.tag_remove("left", "sel.first", "sel.last")
                self.textArea.tag_remove("center", "sel.first", "sel.last")
                self.textArea.tag_add("right", "sel.first", "sel.last")
                self.textArea.tag_configure("right", justify="right")
        
    # Create Citation style window
    def citation_style_window(self):
        citation_style_window = tk.Toplevel(self)
        citation_style_window.geometry("200x200")
        citation_style_window.title("Citation style")

        tk.Label(citation_style_window, text="Choose a Citation Style").grid(column=0, row=0, columnspan=2, sticky=tk.EW, padx=20, pady=10)
        cs = tk.Listbox(citation_style_window, width=5, height=3)
        cs.grid(column=0, row=1, columnspan=2, sticky=tk.NSEW, padx=20, pady=10)
        cs.insert(0, 'APA')
        cs.insert(1, 'MLA')
        cs.insert(2, 'Chicago')
    
        Confirm_btn = tk.Button(
            citation_style_window,
            width=20,
            text='Confirm',
            font=('Helvetica',12),
            command=citation_style_window.destroy
        )
        Confirm_btn.grid(column=0, row=2, columnspan=2, padx=20, pady=10)

    def add_citation_command(self):
        self.citation_counter += 1
        citation_text = f"({self.citation_counter})"
        self.textArea.insert(tk.INSERT, citation_text)
        self.open_CitationManagerApp()
        
    def new_file(self):
        self.textArea.delete("1.0", tk.END)

    def open_file(self):
        filePath = tk.filedialog.askopenfilename()
        encodings = ['utf-8', 'latin-1', 'cp1252']
        for encoding in encodings:
            try:
                with open(filePath, "r", encoding=encoding) as file:
                    fileContents = file.read()
                    self.textArea.delete("1.0", tk.END)
                    self.textArea.insert(tk.END, fileContents)
                break
            except UnicodeDecodeError:
                pass

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

    def add_to_word(self):
                #filename = f"my_document_{self.citation_counter}.docx"
        #self.add_to_word(filename)
        # Create a new Word application object
        word = win32.gencache.EnsureDispatch('Word.Application')

        # Add a new document to the Word application object
        doc = word.Documents.Add()

        # Get the text from the textbox
        text = self.textArea.get('1.0', 'end')

        # Split the text into lines
        lines = [line for line in text.split('\n') if line.strip()]

        # Insert the text into the document
        doc.Range().InsertAfter(text)

        # Prompt the user to select a file location and type
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=(("Word Documents", "*.docx"), ("Text Files", "*.txt"), ("All Files", "*.*")))

        # Determine the file type and set the appropriate encoding and file format
        if file_path.endswith(".txt"):
            encoding = 65001
            file_format = win32.constants.wdFormatText
        else:
            encoding = None
            file_format = win32.constants.wdFormatDocumentDefault

        # Save the document to the selected location with the appropriate encoding and file format
        doc.SaveAs(file_path, FileFormat=file_format, Encoding=encoding)

        # Close the Word document and the Word application object
        doc.Close()
        word.Quit()
        
        # Open Word document
        win32api.ShellExecute(0, 'open', file_path, '', '', 1)






#!/usr/bin/env python
# coding: utf-8

# In[55]:
class MyHTMLParser:
    def __init__(self):
        self.author_name = None
        self.publication_date = None
        self.doi=None
        self.publisher=None
    def get_author_and_publication_year(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            author = soup.find('a', {'data-test': 'author-name'})
            publication_date = soup.find('a', {'data-track-action': 'publication date'})
            doi=  soup.find('meta', {'name': 'prism.doi'})
            publisher=soup.find('meta', {'name': 'dc.publisher'})
            if author and author.text:
                self.author_name = author.text.strip()
            if publication_date and publication_date.text:
                self.publication_date = publication_date.text.strip()
            if doi and doi.text:
                self.doi = doi.text.strip()
            if publisher and publisher.text:
                self.publisher = publisher.text.strip()
            return self.author_name, self.publication_date,self.doi,self.publisher
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None, None, None, None
# https://link.springer.com/article/10.1007/s13762-022-03948-9


class Citation:
    def __init__(self, select_type, citation_type, authors, title, publication_year, publisher=None, doi=None,url=None):
        self.select_type = select_type
        self.citation_type = citation_type if citation_type in ["journal", "book"] else None
        self.authors = authors
        self.title = title
        self.publication_year = publication_year
        self.publisher = publisher 
        self.doi = doi
        self.url= url


class CitationManager:
    def __init__(self):
        self.citations = []

    def add_citation(self, citation):
        self.citations.append(citation)

    def remove_citation(self, citation):
        self.citations.remove(citation)

    def search_citations(self, query):
        results = []
        for citation in self.citations:
            if query.lower() in citation.title.lower() or any(query.lower() in author.lower() for author in citation.authors):
                results.append(citation)
        return results

    def sort_citations(self, key):
        return sorted(self.citations, key=lambda x: getattr(x, key))

    def generate_bibliography(self, style):
        bibliography = []
        for citation in self.citations:
            bibliography.append(format_citation(citation, style))
        return bibliography


def format_citation(citation, style):
    if style == 'APA':
        return format_apa(citation)
    elif style == 'MLA':
        return format_mla(citation)
    elif style == 'Chicago':
        return format_chicago(citation)
    else:
        raise ValueError(f"Unknown citation style: {style}")

def format_mla(citation):
    authors = ', '.join(citation.authors[:-1]) + ', and ' + citation.authors[-1]

    result = f"{authors} ({citation.authors}). {citation.title}. {citation.publisher}. {citation.url}."
    if citation.url:
        result += f" Retrieved from {citation.url}"
    return result

def format_apa(citation):
    authors = ', '.join(citation.authors[:-1]) + ', & ' + citation.authors[-1]
    result = f"{authors} ({citation.publication_year}). {citation.title}. {citation.publisher}. {citation.url}."
    if citation.url:
        result += f" Retrieved from {citation.url}"
    return result

def format_chicago(citation):
    authors = ', '.join(citation.authors[:-1]) + ', and ' + citation.authors[-1]
    result = f"{authors} ({citation.authors}). {citation.publication_year}. {citation.title}."

    # Thêm URL vào cuối trích dẫn (nếu có)
    if citation.url:
        result += f" Accessed {citation.url}"

    return result


class CitationManagerApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Citation Manager")
        self.geometry("1000x800")

        self.manager = CitationManager()

        self.create_widgets()
        self.url_entry = None
        self.bibliography_style_var = tk.StringVar()
        self.bibliography_style_var.set("APA")
    def create_widgets(self):
            self.main_frame = ttk.Frame(self)
            self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            self.title_label = ttk.Label(self.main_frame, text="Citation Manager", font=("Arial", 16, "bold"))
            self.title_label.pack(pady=20)

            self.add_citation_button = ttk.Button(self.main_frame, text="Add Citation", command=self.add_citation_window)
            self.add_citation_button.pack()
            
            self.remove_citation_button = ttk.Button(self.main_frame, text="Remove Citation", command=self.remove_citation)
            self.remove_citation_button.pack(pady=10)

            self.search_label = ttk.Label(self.main_frame, text="Search")
            self.search_label.pack(pady=10)

            self.search_entry = ttk.Entry(self.main_frame)
            self.search_entry.pack()

            self.search_button = ttk.Button(self.main_frame, text="Search", command=self.search_citations)
            self.search_button.pack(pady=10)

            self.citation_listbox = tk.Listbox(self.main_frame)
            self.citation_listbox.pack(fill=tk.BOTH, expand=True)

            self.generate_bibliography_button = ttk.Button(self.main_frame, text="Generate Bibliography", command=self.generate_bibliography_window)
            self.generate_bibliography_button.pack(pady=20)

    def add_citation_window(self):
        add_citation_win = tk.Toplevel(self)
        def submit():
            select_type = select_type_var.get()
            if select_type == "Manual":
                citation_type = "book"  # or "journal", depending on the type of the citation
                authors = author_entry.get().split(', ')
                title = title_entry.get()
                if not title:
                    title = ""
                publication_year = int(year_entry.get())
                url = url_entry.get()
                citation = Citation(select_type, citation_type, authors, title, publication_year, url=url, doi=doi_entry.get(), publisher=publisher_entry.get())
            elif select_type == "Auto":
                citation_type = "book"  # or "journal", depending on the type of the citation
                url = url_entry.get()
                parser = MyHTMLParser()
                author_name, publication_year_from_url,doi, publisher = parser.get_author_and_publication_year(url)
                if author_name:
                    authors = [author_name]
                else:
                    authors = []
                if publication_year_from_url:
                    publication_year = publication_year_from_url
                else:
                    publication_year = 0
                title = ""
                citation = Citation(select_type, citation_type, authors, title, publication_year, url=url, doi=doi_entry.get(), publisher=publisher_entry.get())




            self.manager.add_citation(citation)
            self.citation_listbox.insert(tk.END, f"{citation.title} {', '.join(citation.authors)}, {citation.publication_year}")

            add_citation_win.destroy()

            if url_entry.winfo_exists():
                url_entry.delete(0, tk.END)
            if author_entry.winfo_exists():
                author_entry.delete(0, tk.END)
                author_entry.insert(0, author_name)
            if year_entry.winfo_exists():
                year_entry.delete(0, tk.END)
                year_entry.insert(0, publication_year_from_url)


        def show_manual_fields():
            author_label.grid()
            author_entry.grid()
            title_label.grid()
            title_entry.grid()
            year_label.grid()
            year_entry.grid()
            url_label.grid
            url_entry.grid

        def show_auto_fields():
            author_label.grid_remove()
            author_entry.grid_remove()
            title_label.grid_remove()
            title_entry.grid_remove()
            year_label.grid_remove()
            year_entry.grid_remove()
            doi_label.grid_remove()
            doi_entry.grid_remove()
            publisher_label.grid_remove()
            publisher_entry.grid_remove()
            url_label.grid()
            url_entry.grid()
            add_citation_win = tk.Toplevel(self)
            add_citation_win.title("Add Citation")

        select_type_label = ttk.Label(add_citation_win, text="select_type")
        select_type_label.grid(row=0, column=0)
        select_type_var = tk.StringVar(value="Manual")
        select_type_radio_manual = ttk.Radiobutton(add_citation_win, text="Manual", variable=select_type_var, value="Manual", command=show_manual_fields)
        select_type_radio_manual.grid(row=0, column=1)
        select_type_radio_auto = ttk.Radiobutton(add_citation_win, text="Auto", variable=select_type_var, value="Auto", command=show_auto_fields)
        select_type_radio_auto.grid(row=0, column=2)

        fields_frame = ttk.Frame(add_citation_win)
        fields_frame.grid(row=1, column=0, columnspan=3)
        
        author_label = ttk.Label(add_citation_win, text="Authors (separated by ', ')")
        author_label.grid(row=1, column=0)
        author_entry = ttk.Entry(add_citation_win)
        author_entry.grid(row=1, column=1)

        title_label = ttk.Label(add_citation_win, text="Title")
        title_label.grid(row=2, column=0)
        title_entry = ttk.Entry(add_citation_win)
        title_entry.grid(row=2, column=1)

        year_label = ttk.Label(add_citation_win, text="Publication Year")
        year_label.grid(row=3, column=0)
        year_entry = ttk.Entry(add_citation_win)
        year_entry.grid(row=3, column=1)
        
        doi_label = ttk.Label(add_citation_win, text="DOI:")
        doi_label.grid(row=4, column=0)
        doi_entry = ttk.Entry(add_citation_win)
        doi_entry.grid(row=4, column=1)

        publisher_label = ttk.Label(add_citation_win, text="Publisher:")
        publisher_label.grid(row=5, column=0)
        publisher_entry = ttk.Entry(add_citation_win)
        publisher_entry.grid(row=5, column=1)

        url_label = ttk.Label(add_citation_win, text="URL")
        url_label.grid(row=6, column=0)
        url_entry = ttk.Entry(add_citation_win)
        url_entry.grid(row=6, column=1)
        self.url_entry = url_entry
        
        submit_button = ttk.Button(add_citation_win, text="Submit", command=submit)
        submit_button.grid(row=7, column=1, sticky="E")
       
        
    def remove_citation(self):
        selected_index = self.citation_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No citation selected.")
            return

        selected_citation = self.manager.citations[selected_index[0]]
        self.manager.remove_citation(selected_citation)
        self.citation_listbox.delete(selected_index)

    def search_citations(self):
        query = self.search_entry.get()
        results = self.manager.search_citations(query)

        self.citation_listbox.delete(0, tk.END)
        for result in results:
            self.citation_listbox.insert(tk.END, result.title)
        
    def generate_bibliography(self):
        style = self.bibliography_style_var.get()
        bibliography = self.manager.generate_bibliography(style)

        # Tạo cửa sổ mới để hiển thị danh mục tài liệu tham khảo
        bibliography_win = tk.Toplevel(self)
        bibliography_win.title("Bibliography")

        bibliography_text = tk.Text(bibliography_win, wrap=tk.WORD)
        bibliography_text.pack(padx=10, pady=10)

        for entry in bibliography:
            bibliography_text.insert(tk.END, entry + "\n\n")

        close_button = ttk.Button(bibliography_win, text="Close", command=bibliography_win.destroy)
        close_button.pack(pady=10)
    def generate_bibliography_window(self):
        generate_bibliography_win = tk.Toplevel(self)
        generate_bibliography_win.title("Generate Bibliography")

        style_label = ttk.Label(generate_bibliography_win, text="Style:")
        style_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        style_combobox = ttk.Combobox(generate_bibliography_win, textvariable=self.bibliography_style_var, values=["APA", "MLA", "Chicago"])
        style_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        generate_button = ttk.Button(generate_bibliography_win, text="Generate", command=self.generate_bibliography)
        generate_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        style_var = tk.StringVar(generate_bibliography_win)
        style_var.set("APA")
        style_combobox.grid()

#separate

#Button 5: About us
class InfoWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Student Information")
        
        table_frame = tk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        table = ttk.Treeview(table_frame, columns=("name", "id", "dept", "group"))
        table.heading("name", text="Name")
        table.heading("id", text="Student ID")
        table.heading("dept", text="Department")
        table.heading("group", text="Group")
        
        table.insert("", "end", values=("Vũ Đức Thành", "BI12-354", "Data Science", "2 MATH"))
        table.insert("", "end", values=("Hà Hải Long", "BI12-256", "Data Science", "2 MATH"))
        table.insert("", "end", values=("Phạm Minh Hoàng", "BI12-175", "Data Science", "2 MATH"))
        table.insert("", "end", values=("Nguyễn Nam Anh", "BI12-027", "Applied Mathematics", "2 MATH"))
        table.insert("", "end", values=("Nguyễn Thanh Bình", "BI12-055", "Applied Mathematics", "2 MATH"))
        
        table.pack(fill=tk.BOTH, expand=True)
        
if __name__ == "__main__":
    root = tk.Tk()
    modern_menu = ModernMenu(root)
    root.mainloop()