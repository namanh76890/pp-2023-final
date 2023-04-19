import tkinter as tk
from tkinter import*


root = tk.Tk()
root.title("CMS")
root.geometry("1920x1180")

  
tk.Label(root, text = "Choose a Citation Style").grid(column = 2, row = 1, sticky = tk.EW, padx = 20, pady = 10)
cs = Listbox(root)
cs.grid(column = 2, row = 2, sticky = tk.EW, padx = 20, pady= 10)
cs.insert(0,'APA')
cs.insert(1,'MLA')
cs.insert(2, 'Chicago')

    
def checkkey(event):
	
	value = event.widget.get()
	print(value)
	
	# get data from l
	if value == '':
		data = l
	else:
		data = []
		for item in l:
			if value.lower() in item.lower():
				data.append(item)				

	# update data in listbox
	update(data)


def update(data):
	
	# clear previous data
	lb.delete(0, 'end')

	# put new data
	for item in data:
		lb.insert('end', item)


# Driver code
l = ('C','C++','Java',
	'Python','Perl',
	'PHP','ASP','JS' )



#creating text box
e = Entry(root)
e.grid(column = 2, row = 6, sticky = tk.EW, padx = 20, pady =10)
e.bind('<KeyRelease>', checkkey)

#creating list box
tk.Label(root, text = "List of Citations").grid(column = 2, row = 5, sticky = tk.EW, padx = 20, pady = 10)
lb = Listbox(root)
lb.grid(column = 2, row = 7, sticky = tk.EW, padx = 20, pady =10)
update(l)
def selected_item():
	
	# Traverse the tuple returned by
	# curselection method and print
	# corresponding value(s) in the listbox
	for i in lb.curselection():
		print(lb.get(i))

# Create a button widget and
# map the command parameter to
# selected_item function
btn = Button(root, text='Print Selected', command=selected_item)

# Placing the button and listbox
btn.grid(column = 2, row = 10, sticky = tk.EW, padx = 20, pady =10)


root.mainloop()



  










  










  










  






