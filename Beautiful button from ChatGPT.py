import tkinter as tk

class ModernButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            font=("Helvetica", 12, "bold"),
            bg="#1c1c1c",
            fg="#FFFFFF",
            activebackground="#2c2c2c",
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            highlightthickness=2,
            highlightcolor="#FFFFFF",
            highlightbackground="#FFFFFF",
            cursor="hand2"
        )
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        
    def _on_enter(self, event):
        self.config(
            bg="#FFFFFF",
            fg="#1c1c1c",
            highlightcolor="#1c1c1c",
            highlightbackground="#FFFFFF"
        )
        
    def _on_leave(self, event):
        self.config(
            bg="#1c1c1c",
            fg="#FFFFFF",
            highlightcolor="#FFFFFF",
            highlightbackground="#1c1c1c"
        )

# Usage
root = tk.Tk()
root.config(bg="blue")
button1 = ModernButton(root, text="Click Me")
button1.grid(column=0, row=0, padx=0, pady=0)
button2 = ModernButton(root, text="Fuck Me")
button2.grid(column=0, row=1, padx=0, pady=0)
root.mainloop()
