import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication, QListWidget, QLineEdit)

from chatterbotapi import ChatterBotFactory, ChatterBotType

class Chat(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        grid = QGridLayout()
        self.setLayout(grid)

        send = QPushButton('Chat')
        send.clicked.connect(self.send_msg)
        grid.addWidget(send, 0, 1)

        self.listbox = QListWidget()
        grid.addWidget(self.listbox, 1, 0)

        self.entry = QLineEdit()
        grid.addWidget(self.entry, 0, 0)

        self.factory = ChatterBotFactory()
        self.bot = self.factory.create(ChatterBotType.CLEVERBOT)
        self.botsession = self.bot.create_session()

        self.move(300, 150)
        self.setWindowTitle('RoboChatZone')
        self.show()

    def send_msg(self):
        if len(self.entry.text()) > 0:
            self.msg = self.entry.text()
            self.listbox.addItem(self.msg)
            self.entry.clear()
        else:
            try:
                self.msg = self.botsession.think(self.msg)
                if self.msg[0:2]== "b'" or self.msg[0:2] == "b\"":
                    self.listbox.addItem(self.msg[2:])
                else:
                    self.listbox.addItem(self.msg)
            except:
                self.msg = self.entry.text()
                self.listbox.addItem(self.msg)
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Chat()
    sys.exit(app.exec_())
