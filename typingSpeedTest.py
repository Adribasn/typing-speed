import customtkinter as ctk
import json
import random

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')

words = open('words.json')
data = json.load(words)

class App(ctk.CTk):
    WIDTH = 1820
    HEIGHT = 720
    def __init__(self):
        super().__init__()

        self.target = ctk.StringVar()
        self.randomIndex = random.randint(0, len(data["data"]) - 1)
        self.target.set(data["data"][self.randomIndex])

        self.geometry('1280x720')
        self.title('Typing Speed Test')

        self.grid_rowconfigure((0, 4), weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.resetButton = ctk.CTkButton(master=self, width=90, height=30, text="Reset", text_color='gray14', font=('Roboto Medium', 16))
        self.resetButton.grid(row=0, column=0, padx=20, pady=20, sticky='nw')

        self.statsFrame = ctk.CTkFrame(master=self, fg_color='transparent')
        self.statsFrame.grid(row=1, column=0, pady=(100, 50))

        self.statsFrame.grid_rowconfigure(0, weight=0)
        self.statsFrame.grid_columnconfigure((0, 4), weight=1)

        self.countdownFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5, border_color='#3EB489')
        self.countdownFrame.grid(row=0, column=0, padx=20)

        self.wordcountFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.wordcountFrame.grid(row=0, column=1, padx=20)

        self.charcountFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.charcountFrame.grid(row=0, column=2, padx=20)

        self.accuracyFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.accuracyFrame.grid(row=0, column=3, padx=20)

        self.wordFrame = ctk.CTkFrame(master=self, width=750, height=100, fg_color='transparent')
        self.wordFrame.grid(row=2, column=0)

        self.wordFrame.grid_rowconfigure(0, weight=0)
        self.wordFrame.grid_columnconfigure((0, 1), weight=1)

        self.targetFrame = ctk.CTkLabel(master=self.wordFrame, textvariable=self.target, font=('Roboto Medium', 32), text_color='#2CC985', width=300, height=100, fg_color='gray17', corner_radius=6)
        self.targetFrame.grid(row=0, column=0, padx=(0, 25))

        self.attemptFrame = ctk.CTkEntry(master=self.wordFrame, font=('Roboto Medium', 32), width=300, height=100, justify='center')
        self.attemptFrame.grid(row=0, column=1, padx=(25, 0))
        
        self.attemptFrame.bind('<Return>', self.changeTarget)
        self.mainloop()

    def changeTarget(self, event):
        if self.correctAnswer():
            self.randomIndex = random.randint(0, len(data["data"]) - 1)
            self.attemptFrame.delete(0, len(self.attemptFrame.get()))
            self.target.set(data["data"][self.randomIndex])

    def correctAnswer(self):
        if self.attemptFrame.get() == self.target.get():
            return True
        else:
            return False



if __name__ == "__main__":
    app = App()
    app.mainloop()

