from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
import pyperclip

zElements = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
    'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, " ": 100
}


class projectGui(QMainWindow):
    def __init__(self):
        super(projectGui, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        uic.loadUi("mygui.ui", self)
        self.show()
        self.encrypt.clicked.connect(self.encryption)
        self.copy.clicked.connect(self.copyText)
        self.decrypt.clicked.connect(self.decryption)

    def encryption(self):
        text = self.textEdit.toPlainText()
        if text:
            key = int(self.key.text())
            mod = 26
            # translate text to numbers
            translated_text = ""
            for char in text:
                if char.upper() in zElements:
                    translated_text += str(zElements[char.upper()])+" "
            # encrypt to number with given key and mod
            translated_text = translated_text.split(" ")
            encrypted_num = ""
            for i in translated_text:
                if i:
                    if int(i) == 100:
                        encrypted_num += str(i)+" "
                    else:
                        i = ((int(i)+key) % mod)
                        encrypted_num += str(i)+" "
            # translate numbers to text again after encryption
            encrypted_num = encrypted_num.split(" ")
            encrypted_text = ""
            for i in encrypted_num:
                    if i:
                        for key, val in zElements.items():
                            if int(i) == val:
                                encrypted_text += key
            # load encrypted text
            self.loadText(encrypted_text.lower())
        else:
            self.loadText("enter any text first")

    def decryption(self):
        decrypted_text = self.textEdit.toPlainText()
        if decrypted_text:
            key = int(self.key.text())
            mod = 26
            # translate text to numbers
            translated_text = ""
            for char in decrypted_text:
                if char.upper() in zElements:
                    translated_text += str(zElements[char.upper()])+" "
            # encrypt to number with given key and mod
            translated_text = translated_text.split(" ")
            encrypted_num = ""
            for i in translated_text:
                if i:
                    if int(i) == 100:
                        encrypted_num += str(i)+" "
                    else:
                        i = ((int(i)-key) % mod)
                        encrypted_num += str(i)+" "
            # translate numbers to text again after decryption
            encrypted_num = encrypted_num.split(" ")
            decrypted_text = ""
            for i in encrypted_num:
                    if i:
                        for key, val in zElements.items():
                            if int(i) == val:
                                decrypted_text += key
            # load encrypted text
            self.loadText(decrypted_text.lower())
        else:
            self.loadText("enter any text first")

    def loadText(self, text):
        self.textEdit_2.setText(text)

    def copyText(self):
        text = self.textEdit_2.toPlainText()
        pyperclip.copy(text)


def main():
    app = QApplication([])
    window = projectGui()
    app.exec_()


if __name__ == '__main__':
    main()