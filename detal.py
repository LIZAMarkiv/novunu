from io import BytesIO

import requests
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *

def detali_novun(item):
    window = QDialog()
    mainlinee = QVBoxLayout()
    new = item.data_dict
    ll1 = QLabel(new["title"])
    foto = QLabel("фото")
    img_url = new['image_url']
    if img_url:
        response = requests.get(img_url)
        data = BytesIO(response.content)

        pixmap = QPixmap()
        pixmap.loadFromData(data.read())
        foto.setPixmap(pixmap)





    mainlinee.addWidget(ll1)
    mainlinee.addWidget(foto)
    window.setLayout(mainlinee)
    window.show()
    window.exec()