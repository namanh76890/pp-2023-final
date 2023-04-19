import tkinter as tk

class Management:#"là frame cha"
    def __init__(self, root):
        self.window = root
        self.window.title("Student management")
        self. window.geometry("1200x675")
        #"mỗi khi tạo frame gì phải có 1 hàm  đi kèm, thầy sơn sử dụng hàm Pack"
        self.detail_frame = tk.Frame(
            self.window,
            bg='#8B8B83'
        )
        self.detail_frame.place(width=200,height=400)
        #"3 kiểu frame: pack, place, read (trong moodle slide)"
        #"dưới là frame con"
        #Button frame for Display
        self.btn_frame_for_list = tk.Frame(
            self.detail_frame,
            bg='#CDCDAD',
            relief=tk.GROOVE
        )
        self.btn_frame_for_list.place(x=10, y=30,width=200, height = 100)
        
        #display Student button
        self.stdlist_btn=tk.Button(
            self.btn_frame_for_list,
            bg='#4a536b',
            foreground="white",
            text="Student List",
            bd=2,
            font=("Times New Roman", 13),
            width=15,
            relief=tk.FLAT
        )
        self.stdlist_btn.grid(row=0, column=0, padx=2, pady=2)
        
        #display Course Button
        self.crslist_btn=tk.Button(
            self.btn_frame_for_list,
            bg='#4a536b',
            foreground="white",
            text="Course List",
            bd=2,
            font=("Times New Roman", 13),
            width=15,
            relief=tk.SUNKEN
        )
        self.crslist_btn.grid(row=1, column=0, padx=2, pady=2)
        
        #Button Frame for Adding
        self.btn_frame_for_input = tk.Frame(
            self.detail_frame,
            bg='#4a536b',
        )
        self.btn_frame_for_input.place(x=10,y=230,width=200,height=100)
        
        self.add_btn = tk.Button(
            self.btn_frame_for_input,
            bg='#4a536b',
            foreground="white",
            text="Input info",
            font=("Times New Roman", 13),
            width=15,
            relief=tk.RIDGE
        )
        self.add_btn.grid(row=0, column = 0, padx=2, pady =2)
        
        #frame in the right for the Data frame
        self.data_frame = tk.Frame(
            self.window, #"chọn parent frame"
            relief=tk.GROOVE,
            bg='#CDCDAD'
        )
        self.data_frame.place(x=200, width = 600, height=800)
        
        self.title_label = tk.Label(
            self.data_frame,
            text="Student Management System",
            font=("Times New Romans",13,"bold"),
            padx=100,
            pady=10,
            bg='#E0E0EE',
            relief=tk.GROOVE
        )
        self.title_label.pack(side=tk.TOP, fill=tk.X)

        #Frame for display information
        self.info_frame = tk.Frame(
            self.data_frame,
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


