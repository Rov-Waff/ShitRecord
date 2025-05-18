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
        self.btn_rec.clicked.connect(self.do_shit)
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
            r=requests.post(f"{self.config['backend_url']}/stat/getStatus",data=self.config)
            if r.status_code!=200:
                QMessageBox.warning(self,"Error","无法连接到拉屎服务器，检查账号配置和您的网络")
            else:
                self.lb_today.setText(r.content['n_today'])
                self.lb_total.setText(r.content['n_total'])
        except:
            QMessageBox.warning(self,"Error","账号配置不正确")

    def do_shit(self):
        try:
            r=requests.post(f"{self.config['backend_url']}/doShit",data=self.config)
            if r.status_code!=200:
                QMessageBox.warning(self,"Error","无法连接到拉屎服务器，检查账号配置和您的网络")
            else:
                QMessageBox.information(self,"Congratulations!","拉屎成功，记得洗手")
                self.load_status()

        except:
            QMessageBox.warning(self,"Error","账号配置不正确")

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=App()
    sys.exit(app.exec())