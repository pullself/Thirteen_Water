from PyQt5.Qt import *
import sys


class Index(QWidget):
    show_mainindex_sg = pyqtSignal()
    def __init__(self, parent=None):
        super(Index, self).__init__(parent)
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
        self.login_but = QPushButton(self.ind_wi)
        self.joke_but = QPushButton(self.ind_wi)
        self.register_but = QPushButton(self.ind_wi)
        self.imp_la = QLabel(self.ind_wi)
        self.account_le = QLineEdit(self.ind_wi)
        self.psw_le = QLineEdit(self.ind_wi)
        self.set_ui()
        with open('index.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def set_ui(self):
        self.setWindowTitle('Login')
        self.setObjectName('index')
        self.resize(self.w, self.h)
        self.top_wi.setObjectName('top')
        self.top_wi.resize(930 * self.xr, 95 * self.yr)
        self.logo_la.setObjectName('logo')
        self.logo_la.resize(65 * self.zr, 65 * self.zr)
        self.logo_la.move(29 * self.xr, 16 * self.yr)
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(10, 10)
        effect.setColor(QColor(0, 0, 0, 80))
        effect.setBlurRadius(20)
        self.ind_wi.setObjectName('login')
        self.ind_wi.resize(327 * self.xr, 388 * self.yr)
        self.ind_wi.move(300 * self.xr, 150 * self.yr)
        self.ind_wi.setGraphicsEffect(effect)
        self.joke_but.setObjectName('joke')
        self.joke_but.resize(130 * self.xr, 30 * self.yr)
        self.joke_but.move(76 * self.xr, 234 * self.yr)
        self.joke_but.setFlat(True)
        self.joke_but.setText('忘记密码？我也没办法')
        self.login_but.setObjectName('button')
        self.login_but.move(64 * self.xr, 260 * self.yr)
        self.login_but.resize(202 * self.xr, 45 * self.yr)
        self.login_but.setText('登陆')
        self.login_but.clicked.connect(self.login)
        self.register_but.setObjectName('button')
        self.register_but.move(64 * self.xr, 315 * self.yr)
        self.register_but.resize(202 * self.xr, 45 * self.yr)
        self.register_but.setText('注册')
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
        self.ind_wi.setStyleSheet('#input{border-radius:' + str(self.zr * 20) + 'px;}' + '#button{border-radius:' + str(
            self.zr * 20) + 'px;'+'font-size:'+str(int(self.zr*18))+'px;}')

    def login(self):
        account_p = self.account_le.text()
        psw_p = self.psw_le.text()
        self.show_mainindex_sg.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Index()
    window.showFullScreen()
    sys.exit(app.exec())
