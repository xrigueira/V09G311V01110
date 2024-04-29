import tkinter as tk

def confirm_action():
    print('Confirmed')

# Define a window
window = tk.Tk()
window.geometry("450x200")

# Define the widgets
label_name = tk.Label(window, text="Name:")
text_input_name = tk.Entry(window)
confirm_button = tk.Button(window, text="Confirm", command=confirm_action)

# Define grid for the widgets
label_name.grid(row=0, column=0, sticky=tk.W)
text_input_name.grid(row=0, column=1)
confirm_button.grid(row=1, columnspan=2)

# Define the main loop
window.mainloop()