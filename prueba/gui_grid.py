import tkinter as tk

# Define a window
window = tk.Tk()
window.geometry("450x200")
window.title("GUI with grid style")

# Add widgets
label_name = tk.Label(window, text="Name:")
text_input_name = tk.Entry(window)
label_lastname = tk.Label(window, text="Last name:")
text_input_lastname = tk.Entry(window)

confirm_button = tk.Button(window, text="Confirm")

label_result = tk.Label(window, text="Result:")

# Define the grid
label_name.grid(row=0, column=0, sticky=tk.W)
text_input_name.grid(row=0, column=1)
label_lastname.grid(row=1, column=0, sticky=tk.W)
text_input_lastname.grid(row=1, column=1)
confirm_button.grid(row=0, column=3, rowspan=2, columnspan=2)
label_result.grid(row=3, column=0, columnspan=2)

# Set up main loop
window.mainloop()