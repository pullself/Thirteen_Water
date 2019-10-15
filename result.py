from PyQt5.Qt import *
import sys
import json
from Stools import change_vertical


class ResultSingle(QWidget):
    result_exit_sg = pyqtSignal()

    def __init__(self, parent=None):
        super(ResultSingle, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)
        self.back1_wi = QWidget(self)
        self.resexit_but = QPushButton(self)
        self.id_head = QLabel(self.back1_wi)
        self.role1 = QWidget(self.back1_wi)
        self.role1_detail = QWidget(self.role1)
        self.role4 = QWidget(self.back1_wi)
        self.role4_detail = QWidget(self.role4)
        self.role4_special = QLabel(self.role4)
        self.set_ui()
        with open('result.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def set_ui(self):
        self.setWindowTitle('Result')
        self.setObjectName('result')
        self.resize(self.w, self.h)
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(10, 10)
        effect.setColor(QColor(0, 0, 0, 80))
        effect.setBlurRadius(20)
        self.back1_wi.setObjectName('back')
        self.back1_wi.resize(self.xr * 793, self.yr * 534)
        self.back1_wi.move(self.xr * 69, self.yr * 53)
        self.back1_wi.setGraphicsEffect(effect)
        back_x = 69
        back_y = 53
        effect1 = QGraphicsDropShadowEffect()
        effect1.setOffset(10, 10)
        effect1.setColor(QColor(0, 0, 0, 80))
        effect1.setBlurRadius(20)
        effect4 = QGraphicsDropShadowEffect()
        effect4.setOffset(10, 10)
        effect4.setColor(QColor(0, 0, 0, 80))
        effect4.setBlurRadius(20)
        self.resexit_but.setObjectName('resexit')
        self.resexit_but.resize(self.zr * 38, self.zr * 38)
        self.resexit_but.move(self.xr * 834, self.yr * 36)
        self.resexit_but.clicked.connect(self.result_exit)
        self.resexit_but.setStyleSheet('border-radius:{}px;'.format(self.zr * 18))
        self.id_head.setObjectName('id_head')
        self.id_head.resize(self.xr * 350, self.yr * 140)
        self.id_head.move(self.xr * 225, self.yr * 195)
        # self.id_head.setText('战局ID:4396')
        self.id_head.setAlignment(Qt.AlignCenter)
        self.id_head.setStyleSheet('font-size:{}px;'.format(int(self.zr * 50)))
        self.role1.setObjectName('role')
        self.role1.resize(self.xr * 716, self.yr * 87)
        self.role1.move(self.xr * (108 - back_x), self.yr * (77 - back_y))
        self.role1.setGraphicsEffect(effect1)
        # self.role1_head.setText('test')
        self.role1_detail.setObjectName('role_detail')
        self.role1_detail.resize(self.xr * 606, self.yr * 87)
        self.role1_detail.move(self.xr * 110, self.yr * 0)
        self.role4.setObjectName('role')
        self.role4.resize(self.xr * 716, self.yr * 87)
        self.role4.move(self.xr * (108 - back_x), self.yr * (467 - back_y))
        self.role4.setGraphicsEffect(effect4)
        self.role4_detail.setObjectName('role_detail')
        self.role4_detail.resize(self.xr * 606, self.yr * 87)
        self.role4_detail.move(self.xr * 110, self.yr * 0)
        self.role4_special.setObjectName('role_special')
        self.role4_special.resize(self.xr * 88, self.yr * 36)
        self.role4_special.move(self.xr * 70, self.yr * 26)
        self.role4_special.setAlignment(Qt.AlignCenter)
        for i in range(1, 14):
            if i >= 9:
                xp = 416
                t = 9
            elif i >= 4:
                xp = 239
                t = 4
            else:
                xp = 108
                t = 1
            if i == 3 or i == 8 or i == 13:
                exec('self.role4_lv{}=QLabel(self.role4_detail)'.format(i))
                exec('self.role4_lv{}.resize(self.xr*46,self.yr*67)'.format(i))
                exec('self.role4_lv{}.move(self.xr*(xp+({}-t)*20)+90,self.yr*10)'.format(i, i))
                exec('self.role4_lv{}.setStyleSheet("font-size:{}px;")'.format(i, int(self.zr * 17)))
                # exec('self.role4_lv{}.setText(change_vertical(" 葫芦"))'.format(i))
                exec('self.role4_lv{}.setAlignment(Qt.AlignCenter)'.format(i))
            exec('self.role1_card{}=QLabel(self.role1_detail)'.format(i))
            exec('self.role1_card{}.setObjectName("card")'.format(i))
            exec('self.role1_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role1_card{}.move(self.xr*i*33,self.yr*10)'.format(i, i))
            exec('self.role1_card{}.setScaledContents(True)'.format(i))
            exec('self.role4_card{}=QLabel(self.role4_detail)'.format(i))
            exec('self.role4_card{}.setObjectName("card")'.format(i))
            exec('self.role4_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role4_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
            exec('self.role4_card{}.setScaledContents(True)'.format(i))
        self.back1_wi.setStyleSheet(
            '#back{border-radius:' + str(self.zr * 25) + 'px;}#role{border-radius:' + str(
                self.zr * 18) + 'px;}#role_head{border-radius:' + str(self.zr * 15) + 'px;font-size:' + str(
                int(self.zr * 16)) + 'px;}#role_special{font-size:' + str(int(self.zr * 18)) + 'px;}')

    def result_exit(self):
        self.result_exit_sg.emit()

    def set_role(self, info):
        self.id_head.setText('战局ID:{}'.format(info['id']))
        self.role4_special.setText('{}'.format('散牌'))
        i = 1
        for card in info['origin_cards']:
            exec('self.role1_card{}.setPixmap(QPixmap("./resource/image/{}.jpg"))'.format(i, card))
            i += 1
        t = 3
        j = 1
        for de in info['cards']:
            exec('self.role4_lv{}.setText("{}")'.format(t, de['lv']))
            for card in de["card"]:
                exec('self.role4_card{}.setPixmap(QPixmap("./resource/image/{}.jpg"))'.format(j, card))
                j += 1
            t += 5


if __name__ == '__main__':
    with open('auto.json', 'r', encoding='UTF-8') as f:
        aa = json.load(f)
    app = QApplication(sys.argv)
    window = ResultSingle()
    window.set_role(aa)
    window.showFullScreen()
    sys.exit(app.exec())
