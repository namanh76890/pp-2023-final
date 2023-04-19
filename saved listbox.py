import tkinter as tk

# Create a file to store the options
filename = "options.txt"

# Create the main window
root = tk.Tk()
root.title("Listbox Example")

# Create the Listbox
lb = tk.Listbox(root, selectmode=tk.MULTIPLE)
lb.pack()

# Load the options from the file
if filename:
    try:
        with open(filename, "r") as f:
            for line in f:
                lb.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# Add a button to add items to the Listbox
def add_item():
    item = entry.get()
    if item:
        lb.insert(tk.END, item)
        entry.delete(0, tk.END)

# Add a button to remove selected items from the Listbox
def remove_item():
    selected = lb.curselection()
    for index in selected[::-1]:
        lb.delete(index)

# Save the options to the file when the program exits
def save_options():
    with open(filename, "w") as f:
        for item in lb.get(0, tk.END):
            f.write(item + "\n")

root.protocol("WM_DELETE_WINDOW", save_options)

# Add a text box to enter new items
entry = tk.Entry(root)
entry.pack()

# Add a button to add items to the Listbox
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()

# Add a button to remove selected items from the Listbox
remove_button = tk.Button(root, text="Remove", command=remove_item)
remove_button.pack()

# Add a button to remove selected items from the Listbox
save_button = tk.Button(root, text="Save", command=save_options)
save_button.pack()

# Add a Quit button to close the program
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

# Start the main loop
root.mainloop()
