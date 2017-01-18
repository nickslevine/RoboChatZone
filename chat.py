import sys
import pickle
import os
import time

from chatterbotapi import ChatterBotFactory, ChatterBotType


if sys.version_info < (3, 0):
	# Python 2
	import Tkinter as tk
else:
	# Python 3
	import tkinter as tk

class App:
	def __init__(self, master):
            self.enter = tk.Entry(master)
            self.enter.grid(row=0, column=0)

            self.send = tk.Button(master, text="Send", command=self.send_message)
            self.send.grid(row=0, column=1)

            self.text = tk.StringVar()
            self.textbox = tk.Message(master, textvariable=self.text)
            self.textbox.grid(row=1, column=0)

        def send_message(self):
            self.msg = self.enter.get()
            self.transcript = self.msg
            self.enter.delete(0, 'end')
            self.text.set(self.transcript)

            self.factory = ChatterBotFactory()

            self.bot = self.factory.create(ChatterBotType.CLEVERBOT)
            self.botsession = self.bot.create_session()
            for x in range(0,5):
                self.msg = self.botsession.think(self.msg)
                self.transcript += "\n\n" + self.msg
                print(self.msg)
                update_text(self)

def update_text(self):
    self.text.set(self.transcript)

root = tk.Tk()
root.title("RoboChatZone")
app = App(root)
root.mainloop()
