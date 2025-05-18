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
        
        self.http_response=''
        print(self.config)
        self.show()
        self.load_status()
    def load_cfg(self):
        with open('frontend/src/main/python/your_package/cfg/config.json','r') as f:
           self.config=json.loads(f.read())
    
    def open_account_window(self):
        self.account_window=Account.Account(self)
        print(self.config)

    def load_status(self):
        try:
            self.http_response=requests.post(f"{self.config['backend_url']}/stat/getStatus",data=self.config)
            if self.http_response.status_code!=200:
                QMessageBox.warning(self,"Error","无法连接到拉屎服务器，检查账号配置和您的网络")
        except:
            QMessageBox.warning(self,"Error","账号配置不正确")
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=App()
    sys.exit(app.exec())