import tkinter as tk

# Create a window
window = tk.Tk()
window.geometry("300x200") # Define the size of the window
window.title("GUI Example") # Define the title of the window

# Add widgets
label = tk.Label(window, text="Hello World!", bg='orange') # Defines a label with color orange
text_input = tk.Entry(window) # Defines a text input
button = tk.Button(window, text="Click me!") # Defines a button
selected_option = tk.IntVar() # Defines a variable to store the selected option
seleccion_button = tk.Checkbutton(window, text="Seleccionar", variable=selected_option) # Defines a checkbutton
list = tk.Listbox(window) # Defines a listbox

# Pack the widgets
label.pack(side=tk.TOP, fill=tk.X) # Set the label at the top of the window and fill the width
text_input.pack()
button.pack()
seleccion_button.pack()
list.pack()

# Add items to the list
list.insert(0, "Item 1")
list.insert(1, "Item 2")
list.insert(2, "Item 3")

# Define the main loop
window.mainloop()

