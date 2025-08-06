import requests
from main import*
from mone import*

def novun(category = "",timeframe = "", country = ""):
    response = requests.get(
        f"https://newsdata.io/api/1/latest?apikey=pub_79505cc93b3e45f7be6b47dc1e09d43c&category={category}&timeframe={timeframe}&country={country}")
    print(response.status_code)
    result = response.json()

    window = QDialog()
    mainlinee = QVBoxLayout()
    ll = QLabel("Схоже до вашого запиту:")

    mainlinee.addWidget(ll)

    window.setLayout(mainlinee)
    window.show()
    window.exec()