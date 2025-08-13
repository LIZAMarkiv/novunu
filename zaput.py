import requests
from PyQt6.QtWidgets import *
from detal import*


def novun(category = "",timeframe = "", country = ""):
    print(category)
    params = {
        "category": category,
        "timeframe": timeframe,
        "country": country,
    }
    response = requests.get(
        f"https://newsdata.io/api/1/latest?apikey=pub_79505cc93b3e45f7be6b47dc1e09d43c", params=params)
    print(response.status_code)
    result = response.json()
    print(result)

    window = QDialog()
    mainlinee = QVBoxLayout()
    ll = QLabel("Схоже до вашого запиту:")
    list_widget = QListWidget()
    for item in result["results"]:
        print(item)
        list_item = QListWidgetItem(item["title"])
        list_item.data_dict = item
        list_widget.addItem(list_item)
        #list_widget.addItem(item['image_url'])
    list_widget.itemClicked.connect(detali_novun)
    mainlinee.addWidget(ll)
    mainlinee.addWidget(list_widget)
    window.setLayout(mainlinee)
    window.show()
    window.exec()