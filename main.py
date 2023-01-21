import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()  # create window root

root.geometry('800x500')


def test_button():
    print('pressed')


frame = customtkinter.CTkFrame(master=root)  # create frame, bind to root window
frame.pack(pady=20, padx=60, fill='both', expand=True)

# create label, bind to frame
label = customtkinter.CTkLabel(master=frame, text='This is a label', font=('Roboto', 24))
label.pack(pady=12, padx=10)

# create text input, bind to frame
input_ = customtkinter.CTkEntry(master=frame, placeholder_text='This is an input', show="*")
input_.pack(pady=12, padx=10)

# create button, bind to frame
# test_button() is callback
button = customtkinter.CTkButton(master=frame, text='This is a button', command=test_button)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text='This is a checkbox')
checkbox.pack(pady=12, padx=10)

root.mainloop()
