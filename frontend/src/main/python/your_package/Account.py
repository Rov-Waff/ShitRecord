from ui.ui_account import Ui_Dialog
from PySide6.QtWidgets import *
import sys,json

class Account(QDialog,Ui_Dialog):
    def __init__(self,father):
        super().__init__()
        self.father=father
        self.setupUi(self)
        self.cfg={}
        with open('frontend/src/main/python/your_package/cfg/config.json','r') as f:
            self.cfg=json.loads(f.read())
        self.btn_submit.clicked.connect(self.save_cfg)
        self.show()

    def save_cfg(self):
        self.cfg['name']=self.le_name.text()
        with open('frontend/src/main/python/your_package/cfg/config.json','w',)as f:
            json.dump(self.cfg,f,indent=4)
        self.father.load_cfg()
        self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Account()
    sys.exit(app.exec())