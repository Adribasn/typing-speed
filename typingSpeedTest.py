import customtkinter as ctk
import json
import random
import time

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')

words = open('words.json')
data = json.load(words)

class App(ctk.CTk):
    WIDTH = 1820
    HEIGHT = 720
    def __init__(self):
        super().__init__()

        self.running = False
        self.hasRun = False

        self.target = ctk.StringVar()
        self.randomIndex = random.randint(0, len(data["data"]) - 1)
        self.target.set(data["data"][self.randomIndex])

        self.count = 60
        self.countdownTime = ctk.StringVar()
        self.countdownTime.set('60s')

        self.wordcount = ctk.StringVar()
        self.wordcount.set('0')
        self.tempWordcount = 0

        self.charcount = ctk.StringVar()
        self.charcount.set('0')
        self.tempCharcount = 0

        self.accuracy = ctk.StringVar()
        self.accuracy.set('0')
        self.failedAttempts = 0

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

        self.countdownFrame.grid_rowconfigure(0, weight=1)
        self.countdownFrame.grid_columnconfigure(0, weight=1)
        self.countdownFrame.grid_propagate(False)
        self.countdownText = ctk.CTkLabel(master=self.countdownFrame, textvariable=self.countdownTime, font=('Roboto Medium', 32), text_color='#3EB489')
        self.countdownText.grid(row=0, column=0)    

        self.wordcountFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.wordcountFrame.grid(row=0, column=1, padx=20)

        self.wordcountFrame.grid_rowconfigure((0,1), weight=0)
        self.wordcountFrame.grid_columnconfigure(0, weight=1)
        self.wordcountFrame.grid_propagate(False)
        self.wordcountText = ctk.CTkLabel(master=self.wordcountFrame, textvariable=self.wordcount, font=('Roboto Medium', 36))
        self.wordcountText.grid(row=0, column=0, pady=(15, 0))
        self.wordcountSubText = ctk.CTkLabel(master=self.wordcountFrame, text='words/min', font=('Roboto Light', 16))
        self.wordcountSubText.grid(row=1, column=0)

        self.charcountFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.charcountFrame.grid(row=0, column=2, padx=20)

        self.charcountFrame.grid_rowconfigure((0,1), weight=0)
        self.charcountFrame.grid_columnconfigure(0, weight=1)
        self.charcountFrame.grid_propagate(False)
        self.charcountText = ctk.CTkLabel(master=self.charcountFrame, textvariable=self.charcount, font=('Roboto Medium', 36))
        self.charcountText.grid(row=0, column=0, pady=(15, 0))
        self.charcountSubText = ctk.CTkLabel(master=self.charcountFrame, text='chars/min', font=('Roboto Light', 16))
        self.charcountSubText.grid(row=1, column=0)

        self.accuracyFrame = ctk.CTkFrame(master=self.statsFrame, width=100, height=100, border_width=5)
        self.accuracyFrame.grid(row=0, column=3, padx=20)

        self.accuracyFrame.grid_rowconfigure((0,1), weight=0)
        self.accuracyFrame.grid_columnconfigure(0, weight=1)
        self.accuracyFrame.grid_propagate(False)
        self.accuracyText = ctk.CTkLabel(master=self.accuracyFrame, textvariable=self.accuracy, font=('Roboto Medium', 36))
        self.accuracyText.grid(row=0, column=0, pady=(15, 0))
        self.accuracySubText = ctk.CTkLabel(master=self.accuracyFrame, text='% accuracy', font=('Roboto Light', 16))
        self.accuracySubText.grid(row=1, column=0)

        self.wordFrame = ctk.CTkFrame(master=self, width=750, height=100, fg_color='transparent')
        self.wordFrame.grid(row=2, column=0)

        self.wordFrame.grid_rowconfigure(0, weight=0)
        self.wordFrame.grid_columnconfigure((0, 1), weight=1)

        self.targetFrame = ctk.CTkLabel(master=self.wordFrame, textvariable=self.target, font=('Roboto Medium', 32), text_color='#2CC985', width=300, height=100, fg_color='gray17', corner_radius=6)
        self.targetFrame.grid(row=0, column=0, padx=(0, 25))

        self.attemptFrame = ctk.CTkEntry(master=self.wordFrame, font=('Roboto Medium', 32), width=300, height=100, justify='center')
        self.attemptFrame.grid(row=0, column=1, padx=(25, 0))
        
        self.attemptFrame.bind('<Return>', self.changeTarget)
        self.resetButton.bind('<Button-1>', self.reset)
        self.countdown(self.count)
        self.mainloop()

    def changeTarget(self, event):
        if self.hasRun == False:
            self.running = True
            self.hasRun = True
        
        if self.running:
            if self.correctAnswer():
                self.tempWordcount += 1
                self.tempCharcount += len(self.target.get())

                self.randomIndex = random.randint(0, len(data["data"]) - 1)
                self.attemptFrame.delete(0, len(self.attemptFrame.get()))
                self.target.set(data["data"][self.randomIndex])
            else:
                self.failedAttempts += 1
        else:
            if self.correctAnswer():
                self.attemptFrame.delete(0, len(self.attemptFrame.get()))

            

    def correctAnswer(self):
        if self.attemptFrame.get() == self.target.get():
            return True
        else:
            return False
        
    def countdown(self, count):
        self.countdownTime.set(str(self.count) + 's') 
        if self.count > 0:
            self.count -= 1
            self.after(1000, self.countdown, self.count)
        else:
            self.after(1000, self.countdown, self.count)
            self.running = False
            self.wordcount.set(str(self.tempWordcount))
            self.charcount.set(str(self.tempCharcount))
            self.accuracy.set(str(int(((self.tempWordcount - self.failedAttempts) / self.tempWordcount) * 100)))

        if self.running == False:
            if self.hasRun == False:
                self.count = 60
                self.tempWordcount = 0
                self.tempCharcount = 0
                self.failedAttempts = 0
                self.wordcount.set('0')
                self.charcount.set('0')
                self.accuracy.set('0')

    def reset(self, event):
        self.running = True
        self.count = 60
        self.tempWordcount = 0
        self.tempCharcount = 0
        self.failedAttempts = 0
        self.wordcount.set('0')
        self.charcount.set('0')
        self.accuracy.set('0')
        self.randomIndex = random.randint(0, len(data["data"]) - 1)
        self.attemptFrame.delete(0, len(self.attemptFrame.get()))
        self.target.set(data["data"][self.randomIndex])

if __name__ == "__main__":
    app = App()
    app.mainloop()

