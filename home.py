from PyQt5.Qt import *
import sys


class Home(QWidget):
    home_exit_sg = pyqtSignal()

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)
        self.vertical_img = QLabel(self)
        self.role_data_wi = QWidget(self)
        self.rankexit_but = QPushButton(self)
        self.role_header = QLabel(self.role_data_wi)
        self.role_name = QLabel(self.role_data_wi)
        self.role_rank = QPushButton(self.role_data_wi)
        self.ranking = QPushButton(self.role_data_wi)
        self.role_details = QWidget(self.role_data_wi)
        self.bigcard_la = QLabel(self.role_details)
        self.bigcard_wi = QWidget(self.role_details)
        self.rate_la = QLabel(self.role_details)
        self.rate_wi = QLabel(self.role_details)
        self.role_special = QLabel(self.bigcard_wi)
        self.set_ui()
        with open('home.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def set_ui(self):
        self.setWindowTitle('Home')
        self.setObjectName('home')
        self.resize(self.w, self.h)
        self.vertical_img.setObjectName('vertical')
        self.vertical_img.resize(self.xr * 205, self.yr * 534)
        self.vertical_img.move(self.xr * 79, self.yr * 39)
        self.role_data_wi.setObjectName('role_data_wi')
        self.role_data_wi.resize(self.xr * 552, self.yr * 534)
        self.role_data_wi.move(self.xr * 320, self.yr * 39)
        self.rankexit_but.setObjectName('resexit')
        self.rankexit_but.resize(self.zr * 38, self.zr * 38)
        self.rankexit_but.move(self.xr * 852, self.yr * 18)
        self.rankexit_but.clicked.connect(self.home_exit)
        self.role_header.setObjectName('role_header')
        self.role_header.resize(self.zr * 70, self.zr * 70)
        self.role_header.move(self.xr * 38, self.yr * 10)
        self.role_name.setObjectName('role_name')
        self.role_name.resize(self.xr * 129, self.yr * 43)
        self.role_name.move(self.xr * 129, self.yr * 21)
        self.role_name.setStyleSheet('border-radius:{}px;'.format(self.zr * 18))
        self.role_rank.setObjectName('button')
        self.role_rank.resize(self.xr * 120, self.yr * 31)
        self.role_rank.move(self.xr * 269, self.yr * 27)
        self.role_rank.setText('个人战绩')
        self.ranking.setObjectName('button')
        self.ranking.resize(self.xr * 120, self.yr * 31)
        self.ranking.move(self.xr * 399, self.yr * 27)
        self.ranking.setText('排行榜')
        self.role_details.setObjectName('role_details')
        self.role_details.resize(self.xr * 500, self.yr * 435)
        self.role_details.move(self.xr * 28, self.yr * 89)
        self.bigcard_la.setObjectName('icon')
        self.bigcard_la.resize(self.xr * 120, self.yr * 23)
        self.bigcard_la.move(self.xr * 12, self.yr * 34)
        self.bigcard_la.setText('最近大牌')
        self.bigcard_la.setAlignment(Qt.AlignCenter)
        self.bigcard_wi.setObjectName('bigcard')
        self.bigcard_wi.resize(self.xr * 477, self.yr * 120)
        self.bigcard_wi.move(self.xr * 12, self.yr * 84)
        for i in range(1, 14):
            if i >= 9:
                xp = 330
                t = 9
            elif i >= 4:
                xp = 190
                t = 4
            else:
                xp = 90
                t = 1
            exec('self.role_card{}=QLabel(self.bigcard_wi)'.format(i))
            exec('self.role_card{}.setObjectName("card")'.format(i))
            exec('self.role_card{}.resize(self.xr*40,self.yr*56)'.format(i))
            exec('self.role_card{}.move(self.xr*(xp+({}-t)*20),self.yr*28)'.format(i, i))
        self.role_special.setObjectName('role_special')
        self.role_special.resize(self.xr * 65, self.yr * 32)
        self.role_special.move(self.xr * 15, self.yr * 40)
        self.rate_la.setObjectName('icon')
        self.rate_la.resize(self.xr * 120, self.yr * 23)
        self.rate_la.move(self.xr * 12, self.yr * 234)
        self.rate_la.setText('近期趋势')
        self.rate_la.setAlignment(Qt.AlignCenter)
        self.rate_wi.setObjectName('rate')
        self.rate_wi.resize(self.xr * 477, self.yr * 120)
        self.rate_wi.move(self.xr * 12, self.yr * 284)
        self.role_data_wi.setStyleSheet(
            '#role_data_wi{border-radius:' + str(self.zr * 20) + 'px;}#role_header{border-radius:' + str(
                self.zr * 35) + 'px;}#button{border-radius:' + str(self.zr * 15) + 'px;}#icon{border-radius:' + str(
                self.zr * 10) + 'px;}')

    def home_exit(self):
        self.home_exit_sg.emit()


if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Home()
        window.showFullScreen()
        sys.exit(app.exec())
