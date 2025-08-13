from PyQt6.QtWidgets import*
from mone import *

app = QApplication([])
window = QWidget()
app.setStyleSheet("""
            QWidget {
                background-color: #f0f8ff;
            }
            QLabel {
                color: #333;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #6a5acd;
                color: white;
                font-size: 14px;
                border-radius: 8px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #483d8b;
            }
        """)

main_line = QVBoxLayout()

h1 = QHBoxLayout()
h2 = QHBoxLayout()

h3 = QHBoxLayout()


l1 = QLabel("НОВИНИ СВІТУ")
l2 = QLabel("Оберіть категорію")
k1 = QPushButton("Злочиність")
k2 = QPushButton("Технологія")
k3 = QPushButton("Спорт")
k4 = QPushButton("Туризм")
k5 = QPushButton("Бізнес")
k6 = QPushButton("Навколишнє середовище")

main_line.addWidget(l1)
main_line.addWidget(l2)

h1.addWidget(k1)
h1.addWidget(k2)
h2.addWidget(k3)
h2.addWidget(k4)
h3.addWidget(k5)
h3.addWidget(k6)


main_line.addLayout(h1)
main_line.addLayout(h2)
main_line.addLayout(h3)


k1.clicked.connect(lambda _,: pokaz_novun("crime"))
k2.clicked.connect(lambda _,: pokaz_novun("technology"))
k3.clicked.connect(lambda _,:pokaz_novun("sports"))
k4.clicked.connect(lambda _,:pokaz_novun("tourism"))
k5.clicked.connect(lambda _,:pokaz_novun("business"))
k6.clicked.connect(lambda _,:pokaz_novun("environment"))

window.setLayout(main_line)
window.show()
app.exec()
