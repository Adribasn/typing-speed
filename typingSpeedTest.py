import customtkinter as ctk

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')

class App(ctk.CTk):
    WIDTH = 1820
    HEIGHT = 720
    def __init__(self):
        super().__init__()
    
        self.geometry('1280x720')
        self.title('Typing Speed Test')

        self.grid_rowconfigure((0, 4), weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.resetButton = ctk.CTkButton(master=self, width=90, height=30, text="Reset", font=('Roboto', 16))
        self.resetButton.grid(row=0, column=0, padx=20, pady=20)

        self.statsFrame = ctk.CTkFrame(master=self)
        self.statsFrame.grid(row=1, column=0)

        self.statsFrame.grid_rowconfigure(0, weight=0)
        self.statsFrame.grid_columnconfigure((0, 4), weight=1)

        self.countdownFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5, border_color='#3EB489')
        self.countdownFrame.grid(row=0, column=0)

        self.wordcountFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.wordcountFrame.grid(row=0, column=1)

        self.charcountFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.charcountFrame.grid(row=0, column=2)

        self.accuracyFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.accuracyFrame.grid(row=0, column=3)

        self.typebox = ctk.CTkFrame(master=self, width=750, height=100)
        self.typebox.grid(row=2, column=0)

        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()