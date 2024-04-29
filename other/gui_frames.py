import tkinter as tk

# Define a window
window = tk.Tk()
window.geometry("450x200")
window.title("Main window with frames")

# Define the frames
left_frame = tk.Frame(window, bg='red', width=150, height=200)
confirm_button = tk.Button(left_frame, text="Confirm")
delete_button = tk.Button(left_frame, text="Delete")
undo_button = tk.Button(left_frame, text="Undo")

right_frame = tk.Frame(window, bg='blue', width=300, height=200)
label_frame = tk.Label(right_frame, text="Datos del usuario:")
label_name = tk.Label(right_frame, text="Name:")
text_input_name = tk.Entry(right_frame)
label_lastname = tk.Label(right_frame, text="Last name:")
text_input_lastname = tk.Entry(right_frame)

label_result = tk.Label(window, text="Result:")

# Define grid for the left frame
left_frame.grid(row=0, column=0, sticky=tk.W)
confirm_button.grid(row=0, column=0)
delete_button.grid(row=1, column=0)
undo_button.grid(row=2, column=0)

# Define grid for the right frame
right_frame.grid(row=0, column=1, sticky=tk.W)
label_frame.grid(row=0, column=0, columnspan=2)
label_name.grid(row=1, column=0, sticky=tk.W)
text_input_name.grid(row=1, column=1)
label_lastname.grid(row=2, column=0, sticky=tk.W)
text_input_lastname.grid(row=2, column=1)

# Define grid for the result label
label_result.grid(row=1, column=0, columnspan=2)

# Define the main loop
window.mainloop()