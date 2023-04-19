import tkinter as tk

class ModernMenu:
    def __init__(self, root):
        self.window = root
        self.window.title("Citation Management System")
        self.window.geometry("800x600")

        # Define the color theme
        self.color_theme = {
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
        }
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
            highlightthickness=0
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
            highlightthickness=0
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
            highlightthickness=0
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
            command=self.window.quit
        )
        self.menu_item_6.grid(row=1, column=2, padx=10, pady=10)
        
if __name__ == "__main__":
    root = tk.Tk()
    modern_menu = ModernMenu(root)
    root.mainloop()
