import customtkinter as ctk

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')
window = ctk.CTk()
window.geometry('1280x720')
window.title('Typing Speed Test')

reset = ctk.CTkButton(master=window, width=90, height=30, text="Reset", text_color='#000000', font=('Roboto Medium', 16))
reset.pack(padx=20, pady=20, side='top', anchor='nw')

window.mainloop()