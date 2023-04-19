import tkinter as tk
def window(self):
    self.window = root
    self.window.title("Citation Management System")
    self.window.geometry("1920x1080")

def background(self):
    self.bg = tk.Frame(
        self.window,
        bg='#ffffff'
    )
    self.bg.place(relwidth=1920,relheight=1080)
    
def left_button_bar(self):
    self.left_bar = tk.Frame(
        self.window,
        bg='#011E11'
    )
    self.left_bar.place(width=170,height=540)
    
def button_frame_list(self):
    self.btn_frame_for_list = tk.Frame(
        self.left_bar,
        bg='#ffffff',
    )
    self.btn_frame_for_list.place(x=0, y=0,width=360,height = 540)
    
def add_citation_button(self):
    self.add_citation_btn=tk.Button(
        self.btn_frame_for_list,
        bg='#12FF46',
        foreground="#011E11",
        text="Add citation",
        bd=2,
        font=("Bebas Neue Regular", 13),
        width=15,
        relief=tk.FLAT
    )
    self.add_citation_btn.grid(row=0, column=0, padx=2, pady=2)
    
def delete_citation_button(self):
    self.del_citation_btn=tk.Button(
        self.btn_frame_for_list,
        bg='#12FF46',
        foreground="#011E11",
        text="Delete citation",
        bd=2,
        font=("Bebas Neue Regular", 13),
        width=15,
        relief=tk.FLAT
    )
    self.del_citation_btn.grid(row=1, column=0, padx=2, pady=2)

def edit_citation_button(self):
    self.edi_citation_btn=tk.Button(
        self.btn_frame_for_list,
        bg='#12FF46',
        foreground="#011E11",
        text="Edit citation",
        bd=2,
        font=("Bebas Neue Regular", 13),
        width=15,
        relief=tk.FLAT
    )
    self.edi_citation_btn.grid(row=3, column=0, padx=2, pady=2)

def folder_button(self):
    self.fol_citation_btn=tk.Button(
        self.btn_frame_for_list,
        bg='#12FF46',
        foreground="#011E11",
        text="Folder",
        bd=2,
        font=("Bebas Neue Regular", 13),
        width=15,
        relief=tk.FLAT
    )
    self.fol_citation_btn.grid(row=2, column=0, padx=2, pady=2)
    
def display_button(self):
    self.dis_btn=tk.Button(
        self.btn_frame_for_list,
        bg='#12FF46',
        foreground="#011E11",
        text="Folder",
        bd=2,
        font=("Bebas Neue Regular", 13),
        width=15,
        relief=tk.FLAT
    )
    self.dis_btn.place(x=40, y=70)
    
    
class Management:#"là frame cha"
    def __init__(self, root):
        (self)
        #"mỗi khi tạo frame gì phải có 1 hàm  đi kèm, thầy sơn sử dụng hàm Pack"
        background(self)
        #Tạo frame mới từ tkinter, thanh xanh bên trái
        left_button_bar(self)
        
        #"3 kiểu frame: pack, place, read (trong moodle slide)"
        
        #Button frame for Display
        button_frame_list(self)
        
        #display Add citation button
        add_citation_button(self)
        
        #display Delete citation Button
        delete_citation_button(self)
        
        #display Edit citation Button
        edit_citation_button(self)
        
        #display Folder Button
        folder_button(self)
        
        #display Display Button
        display_button(self)
        
        #frame in the right for the Data frame
        self.btn_frame_for_input = tk.Frame(
            self.left_bar,
            bg='#4a536b',
        )
        self.btn_frame_for_list.place(x=10,y=230,width=200,height=100)
        
        self.title_label = tk.Label(
            self.window,
            text="Citation Management System",
            font=("Bebas Neue Regular",20,"bold"),
            padx=100,
            pady=10,
            bg='#ffffff',
            relief=tk.GROOVE
        )
        
        self.title_label.pack(side=tk.TOP, fill=tk.X)

        #Frame for display information
        self.info_frame = tk.Frame(
            self.window,
            bg='#aed6dc',
            height=400,
            width=600
        )
        self.info_frame.pack()
        
#"dưới này là frame con"
if __name__ == "__main__": 
    root = tk.Tk()
    obj = Management(root)
    root.mainloop()