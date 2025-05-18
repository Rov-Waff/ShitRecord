from PySide6.QtWidgets import *
from ui.ui_MainWindow import Ui_Form
import sys
import json
import requests
import Account

class App(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config={}
        self.load_cfg()

        self.btn_account.clicked.connect(self.open_account_window)
        print(self.config)
        self.show()
    def load_cfg(self):
        with open('frontend/src/main/python/your_package/cfg/config.json','r') as f:
           self.config=json.loads(f.read())
    
    def open_account_window(self):
        self.account_window=Account.Account(self)
        print(self.config)

    def load_status(self):
        r=requests.post(f"{self.config['backend_url']}/getStatus")
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=App()
    sys.exit(app.exec())