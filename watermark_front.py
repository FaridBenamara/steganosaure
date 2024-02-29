from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import os
import hidden_watermark

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.split(__file__)[0], "watermark_front.ui"), self)

        self.browse_button.clicked.connect(self.browse_image)
        self.watermark_button.clicked.connect(self.watermark_image)
        self.extract_message_button.clicked.connect(self.extract_message)

    def browse_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self, 'Selectionne une image', '', 'All Files (*)')
        self.image_label.setPixmap(QPixmap(self.image_path))
        self.watermark_button.setEnabled(True)
        self.extract_message_button.setEnabled(True)

    def watermark_image(self):
        message = self.message_plain_text_edit.toPlainText()
        password = self.password_plain_text_edit.toPlainText()
        hidden_watermark.lsb1_stegano_with_vigenere(self.image_path, message, password)

    def extract_message(self):
        password = self.password_plain_text_edit.toPlainText()
        hidden_message = hidden_watermark.lsb1_extract_message_with_vigenere(self.image_path, password)
        self.message_plain_text_edit.setPlainText(hidden_message)