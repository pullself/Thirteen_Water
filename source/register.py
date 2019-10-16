from PyQt5.Qt import QWidget, pyqtSignal, QApplication, QLabel, QPushButton, QGraphicsDropShadowEffect, QColor, \
    QLineEdit
import sys
from Stools import register


class Register(QWidget):
    register_ok_sg = pyqtSignal()

    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)
        self.top_wi = QWidget(self)
        self.logo_la = QLabel(self.top_wi)
        self.ind_wi = QWidget(self)
        self.register_but = QPushButton(self.ind_wi)
        self.imp_la = QLabel(self.ind_wi)
        self.account_le = QLineEdit(self.ind_wi)
        self.psw_le = QLineEdit(self.ind_wi)
        self.name_le = QLineEdit(self.ind_wi)
        self.set_ui()
        with open('index.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def set_ui(self):
        self.setWindowTitle('Register')
        self.setObjectName('register')
        self.resize(self.w, self.h)
        self.top_wi.setObjectName('top')
        self.top_wi.resize(930 * self.xr, 95 * self.yr)
        self.logo_la.setObjectName('logo')
        self.logo_la.resize(65 * self.xr, 65 * self.zr)
        self.logo_la.move(29 * self.xr, 16 * self.yr)
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(10, 10)
        effect.setColor(QColor(0, 0, 0, 80))
        effect.setBlurRadius(20)
        self.ind_wi.setObjectName('login')
        self.ind_wi.resize(327 * self.xr, 388 * self.yr)
        self.ind_wi.move(300 * self.xr, 150 * self.yr)
        self.ind_wi.setGraphicsEffect(effect)
        self.register_but.setObjectName('button')
        self.register_but.move(64 * self.xr, 315 * self.yr)
        self.register_but.resize(202 * self.xr, 45 * self.yr)
        self.register_but.setText('注册新用户')
        self.register_but.clicked.connect(self.register)
        self.imp_la.setObjectName('imp_label')
        self.imp_la.resize(100 * self.zr, 100 * self.zr)
        self.imp_la.move(115 * self.xr + 100 * (self.xr - self.zr) / 2, 15 * self.yr)
        self.imp_la.setStyleSheet('border-radius:{}px;'.format(self.zr * 49))
        self.account_le.setObjectName('input')
        self.account_le.setTextMargins(20, 0, 0, 0)
        self.account_le.resize(213 * self.xr, 45 * self.yr)
        self.account_le.move(59 * self.xr, 126 * self.yr)
        self.account_le.setPlaceholderText('账号')
        self.psw_le.setObjectName('input')
        self.psw_le.setTextMargins(20, 0, 0, 0)
        self.psw_le.resize(213 * self.xr, 45 * self.yr)
        self.psw_le.move(59 * self.xr, 181 * self.yr)
        self.psw_le.setPlaceholderText('密码')
        self.psw_le.setEchoMode(QLineEdit.Password)
        self.name_le.setObjectName('input')
        self.name_le.setTextMargins(20, 0, 0, 0)
        self.name_le.resize(213 * self.xr, 45 * self.yr)
        self.name_le.move(59 * self.xr, 236 * self.yr)
        self.name_le.setPlaceholderText('昵称')
        self.ind_wi.setStyleSheet('#input{border-radius:' + str(self.zr * 20) + 'px;}' + '#button{border-radius:' + str(
            self.zr * 20) + 'px;' + 'font-size:' + str(int(self.zr * 18)) + 'px;}')

    def register(self):
        account_p = self.account_le.text()
        psw_p = self.psw_le.text()
        # name_p = self.name_le.text()
        dic = register(account_p, psw_p)
        if dic['status'] == 1001:
            self.account_le.clear()
            self.psw_le.clear()
            self.account_le.setStyleSheet('border:4px solid;border-color:red;')
            self.account_le.setPlaceholderText('账号已存在')
        elif dic['status'] == 0:
            self.register_ok_sg.emit()
        else:
            self.account_le.clear()
            self.psw_le.clear()
            self.account_le.setStyleSheet('border:4px solid;border-color:red;')
            self.account_le.setPlaceholderText('未知错误')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Register()
    window.showFullScreen()
    sys.exit(app.exec())
