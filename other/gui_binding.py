import tkinter as tk

def insert_data_in_list():
    list_box.insert(tk.END, f"{name.get()} {lastname.get()}") # Insert data in list
    name.set("") # Clear name input
    lastname.set("") # Clear lastname input
    text_input_name.focus() # Put cursor over name input

# Define window
window = tk.Tk()
window.geometry("450x200")
window.title("Viculacion de datos")

# Define widgets
label_name = tk.Label(window, text="Nombre:")
name = tk.StringVar()
text_input_name = tk.Entry(window, textvariable=name)

label_lastname = tk.Label(window, text="Apellido:")
lastname = tk.StringVar()
text_input_lastname = tk.Entry(window, textvariable=lastname)

confirm_button = tk.Button(window, text="Añadir", command=insert_data_in_list) # Here is where we call the function

list_box = tk.Listbox(window)

# Define grid
label_name.grid(row=0, column=0)
text_input_name.grid(row=0, column=1)
label_lastname.grid(row=1, column=0)
text_input_lastname.grid(row=1, column=1)
confirm_button.grid(row=2, column=0, columnspan=2)
list_box.grid(row=3, column=0, columnspan=2)

# Define main loop
window.mainloop()