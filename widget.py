from PySide6.QtWidgets import QWidget, QMessageBox
from widget_ui import Ui_Widget

import re
import qrcode
from PIL import Image

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QR Code Generator")
        self.button_generate_qr.clicked.connect(self.generate_qr)

    def generate_qr(self):
        url = self.lineedit_url.text()

        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        if re.match(regex, url) is None:
            # Invalid URL
            msgBox = QMessageBox()
            msgBox.setText("Invalid URL")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            # Valid URL
            qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
            qr.add_data(url)
            qr.make(fit = True)
            qr_img = qr.make_image(fill = "black", back_color = "white")
            qr_img.save("qrcode_image.png")
            img = Image.open("qrcode_image.png")
            img.show()
            



