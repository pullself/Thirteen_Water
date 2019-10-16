from PyQt5.Qt import QWidget, pyqtSignal, QApplication, QLabel, QPushButton, QGraphicsDropShadowEffect, QColor, Qt, \
    QPixmap
import sys
import json
from Stools import change_vertical


class Result(QWidget):
    result_exit_sg = pyqtSignal()

    def __init__(self, parent=None):
        super(Result, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)
        self.back1_wi = QWidget(self)
        self.resexit_but = QPushButton(self)
        self.role1 = QWidget(self.back1_wi)
        self.role1_head = QLabel(self.role1)
        self.role1_detail = QWidget(self.role1)
        self.role1_special = QLabel(self.role1_detail)
        self.role2 = QWidget(self.back1_wi)
        self.role2_head = QLabel(self.role2)
        self.role2_detail = QWidget(self.role2)
        self.role2_special = QLabel(self.role2_detail)
        self.role3 = QWidget(self.back1_wi)
        self.role3_head = QLabel(self.role3)
        self.role3_detail = QWidget(self.role3)
        self.role3_special = QLabel(self.role3_detail)
        self.role4 = QWidget(self.back1_wi)
        self.role4_head = QLabel(self.role4)
        self.role4_detail = QWidget(self.role4)
        self.role4_special = QLabel(self.role4_detail)
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
        effect2 = QGraphicsDropShadowEffect()
        effect2.setOffset(10, 10)
        effect2.setColor(QColor(0, 0, 0, 80))
        effect2.setBlurRadius(20)
        effect3 = QGraphicsDropShadowEffect()
        effect3.setOffset(10, 10)
        effect3.setColor(QColor(0, 0, 0, 80))
        effect3.setBlurRadius(20)
        effect4 = QGraphicsDropShadowEffect()
        effect4.setOffset(10, 10)
        effect4.setColor(QColor(0, 0, 0, 80))
        effect4.setBlurRadius(20)
        self.resexit_but.setObjectName('resexit')
        self.resexit_but.resize(self.zr * 38, self.zr * 38)
        self.resexit_but.move(self.xr * 834, self.yr * 36)
        self.resexit_but.clicked.connect(self.result_exit)
        self.resexit_but.setStyleSheet('border-radius:{}px;'.format(self.zr * 18))
        self.role1.setObjectName('role')
        self.role1.resize(self.xr * 716, self.yr * 87)
        self.role1.move(self.xr * (108 - back_x), self.yr * (77 - back_y))
        self.role1.setGraphicsEffect(effect1)
        self.role1_head.setObjectName('role_head')
        self.role1_head.resize(self.xr * 90, self.yr * 50)
        self.role1_head.move(self.xr * 10, self.yr * 16)
        # self.role1_head.setText('test')
        self.role1_head.setAlignment(Qt.AlignCenter)
        self.role1_detail.setObjectName('role_detail')
        self.role1_detail.resize(self.xr * 606, self.yr * 87)
        self.role1_detail.move(self.xr * 110, self.yr * 0)
        self.role1_special.setObjectName('role_special')
        self.role1_special.resize(self.xr * 88, self.yr * 36)
        self.role1_special.move(self.xr * 10, self.yr * 26)
        # self.role1_special.setText('test')
        self.role1_special.setAlignment(Qt.AlignCenter)
        self.role2.setObjectName('role')
        self.role2.resize(self.xr * 716, self.yr * 87)
        self.role2.move(self.xr * (108 - back_x), self.yr * (207 - back_y))
        self.role2.setGraphicsEffect(effect2)
        self.role2_head.setObjectName('role_head')
        self.role2_head.resize(self.xr * 90, self.yr * 50)
        self.role2_head.move(self.xr * 10, self.yr * 16)
        self.role2_head.setAlignment(Qt.AlignCenter)
        self.role2_detail.setObjectName('role_detail')
        self.role2_detail.resize(self.xr * 606, self.yr * 87)
        self.role2_detail.move(self.xr * 110, self.yr * 0)
        self.role2_special.setObjectName('role_special')
        self.role2_special.resize(self.xr * 88, self.yr * 36)
        self.role2_special.move(self.xr * 10, self.yr * 26)
        self.role2_special.setAlignment(Qt.AlignCenter)
        self.role3.setObjectName('role')
        self.role3.resize(self.xr * 716, self.yr * 87)
        self.role3.move(self.xr * (108 - back_x), self.yr * (337 - back_y))
        self.role3.setGraphicsEffect(effect3)
        self.role3_head.setObjectName('role_head')
        self.role3_head.resize(self.xr * 90, self.yr * 50)
        self.role3_head.move(self.xr * 10, self.yr * 16)
        self.role3_head.setAlignment(Qt.AlignCenter)
        self.role3_detail.setObjectName('role_detail')
        self.role3_detail.resize(self.xr * 606, self.yr * 87)
        self.role3_detail.move(self.xr * 110, self.yr * 0)
        self.role3_special.setObjectName('role_special')
        self.role3_special.resize(self.xr * 88, self.yr * 36)
        self.role3_special.move(self.xr * 10, self.yr * 26)
        self.role3_special.setAlignment(Qt.AlignCenter)
        self.role4.setObjectName('role')
        self.role4.resize(self.xr * 716, self.yr * 87)
        self.role4.move(self.xr * (108 - back_x), self.yr * (467 - back_y))
        self.role4.setGraphicsEffect(effect4)
        self.role4_head.setObjectName('role_head')
        self.role4_head.resize(self.xr * 90, self.yr * 50)
        self.role4_head.move(self.xr * 10, self.yr * 16)
        self.role4_head.setAlignment(Qt.AlignCenter)
        self.role4_detail.setObjectName('role_detail')
        self.role4_detail.resize(self.xr * 606, self.yr * 87)
        self.role4_detail.move(self.xr * 110, self.yr * 0)
        self.role4_special.setObjectName('role_special')
        self.role4_special.resize(self.xr * 88, self.yr * 36)
        self.role4_special.move(self.xr * 10, self.yr * 26)
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
                exec('self.role1_lv{}=QLabel(self.role1_detail)'.format(i))
                exec('self.role1_lv{}.resize(self.xr*46,self.yr*67)'.format(i))
                exec('self.role1_lv{}.move(self.xr*(xp+({}-t)*20)+95,self.yr*10)'.format(i, i))
                exec('self.role1_lv{}.setStyleSheet("font-size:{}px;")'.format(i, int(self.zr * 17)))
                exec('self.role1_lv{}.setAlignment(Qt.AlignCenter)'.format(i))
                exec('self.role2_lv{}=QLabel(self.role2_detail)'.format(i))
                exec('self.role2_lv{}.resize(self.xr*46,self.yr*67)'.format(i))
                exec('self.role2_lv{}.move(self.xr*(xp+({}-t)*20)+95,self.yr*10)'.format(i, i))
                exec('self.role2_lv{}.setStyleSheet("font-size:{}px;")'.format(i, int(self.zr * 17)))
                exec('self.role2_lv{}.setAlignment(Qt.AlignCenter)'.format(i))
                exec('self.role3_lv{}=QLabel(self.role3_detail)'.format(i))
                exec('self.role3_lv{}.resize(self.xr*46,self.yr*67)'.format(i))
                exec('self.role3_lv{}.move(self.xr*(xp+({}-t)*20)+95,self.yr*10)'.format(i, i))
                exec('self.role3_lv{}.setStyleSheet("font-size:{}px;")'.format(i, int(self.zr * 17)))
                exec('self.role3_lv{}.setAlignment(Qt.AlignCenter)'.format(i))
                exec('self.role4_lv{}=QLabel(self.role4_detail)'.format(i))
                exec('self.role4_lv{}.resize(self.xr*46,self.yr*67)'.format(i))
                exec('self.role4_lv{}.move(self.xr*(xp+({}-t)*20)+95,self.yr*10)'.format(i, i))
                exec('self.role4_lv{}.setStyleSheet("font-size:{}px;")'.format(i, int(self.zr * 17)))
                exec('self.role4_lv{}.setAlignment(Qt.AlignCenter)'.format(i))
            exec('self.role1_card{}=QLabel(self.role1_detail)'.format(i))
            exec('self.role1_card{}.setObjectName("card")'.format(i))
            exec('self.role1_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role1_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
            exec('self.role1_card{}.setScaledContents(True)'.format(i))
            exec('self.role2_card{}=QLabel(self.role2_detail)'.format(i))
            exec('self.role2_card{}.setObjectName("card")'.format(i))
            exec('self.role2_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role2_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
            exec('self.role2_card{}.setScaledContents(True)'.format(i))
            exec('self.role3_card{}=QLabel(self.role3_detail)'.format(i))
            exec('self.role3_card{}.setObjectName("card")'.format(i))
            exec('self.role3_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role3_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
            exec('self.role3_card{}.setScaledContents(True)'.format(i))
            exec('self.role4_card{}=QLabel(self.role4_detail)'.format(i))
            exec('self.role4_card{}.setObjectName("card")'.format(i))
            exec('self.role4_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role4_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
            exec('self.role4_card{}.setScaledContents(True)'.format(i))
        self.back1_wi.setStyleSheet(
            '#back{border-radius:' + str(self.zr * 25) + 'px;}#role{border-radius:' + str(
                self.zr * 18) + 'px;}#role_head{border-radius:' + str(self.zr * 15) + 'px;font-size:' + str(
                int(self.zr * 20)) + 'px;}#role_special{font-size:' + str(int(self.zr * 18)) + 'px;}')

    def result_exit(self):
        self.result_exit_sg.emit()

    def set_role(self, info):
        i = 1
        # print(info)
        for role in info:
            exec('self.role{}_head.setText("{}")'.format(i, role['name']))
            exec('self.role{}_special.setText("{}")'.format(i, str(role['score']) + '分'))
            # t = 3
            j = 1
            for de in role['cards']:
                # exec('self.role{}_lv{}.setText("{}")'.format(i, t, de['lv']))
                for card in de["card"]:
                    exec('self.role{}_card{}.setPixmap(QPixmap("./resource/image/{}.jpg"))'.format(i, j, card))
                    j += 1
                # t += 5
            i += 1


if __name__ == '__main__':
    with open('suit.json', 'r', encoding='UTF-8') as f:
        aa = json.load(f)
    app = QApplication(sys.argv)
    window = Result()
    window.set_role(aa)
    window.showFullScreen()
    sys.exit(app.exec())
