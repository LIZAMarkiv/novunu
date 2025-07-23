from PyQt6.QtWidgets import*


app = QApplication([])
window = QWidget()

main_line = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

l1 = QLabel("НОВИНИ АМЕРИКИ")
l2 = QLabel("Оберіть категорію")
k1 = QPushButton("Здоров'я")
k2 = QPushButton("Технології")
k3 = QPushButton("Спорт")
k4 = QPushButton("Наука")


main_line.addWidget(l1)
main_line.addWidget(l2)

h1.addWidget(k1)
h1.addWidget(k2)
h2.addWidget(k3)
h2.addWidget(k4)

main_line.addLayout(h1)
main_line.addLayout(h2)





window.setLayout(main_line)
window.show()
app.exec()