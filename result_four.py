from PyQt5.Qt import *
import sys


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
        self.back1_wi.setObjectName('back')
        self.back1_wi.resize(self.xr * 793, self.yr * 534)
        self.back1_wi.move(self.xr * 69, self.yr * 53)
        back_x = 69
        back_y = 53
        self.resexit_but.setObjectName('resexit')
        self.resexit_but.resize(self.zr * 38, self.zr * 38)
        self.resexit_but.move(self.xr * 834, self.yr * 46)
        self.resexit_but.clicked.connect(self.result_exit)
        self.role1.setObjectName('role')
        self.role1.resize(self.xr * 716, self.yr * 87)
        self.role1.move(self.xr * (108 - back_x), self.yr * (77 - back_y))
        self.role1_head.setObjectName('role_head')
        self.role1_head.resize(self.zr * 80, self.zr * 80)
        self.role1_head.move(self.xr * 10, self.yr * 4)
        self.role1_detail.setObjectName('role_detail')
        self.role1_detail.resize(self.xr * 606, self.yr * 87)
        self.role1_detail.move(self.xr * 110, self.yr * 0)
        self.role1_special.setObjectName('role_special')
        self.role1_special.resize(self.xr * 88, self.yr * 36)
        self.role1_special.move(self.xr * 10, self.yr * 26)
        # self.role1_but = QPushButton(self.role1_detail)
        # self.role1_but.setObjectName('role_but')
        # self.role1_but.resize(38, 38)
        # self.role1_but.move(555, 25)
        self.role2.setObjectName('role')
        self.role2.resize(self.xr * 716, self.yr * 87)
        self.role2.move(self.xr * (108 - back_x), self.yr * (207 - back_y))
        self.role2_head.setObjectName('role_head')
        self.role2_head.resize(self.zr * 80, self.zr * 80)
        self.role2_head.move(self.xr * 10, self.yr * 4)
        self.role2_detail.setObjectName('role_detail')
        self.role2_detail.resize(self.xr * 606, self.yr * 87)
        self.role2_detail.move(self.xr * 110, self.yr * 0)
        self.role2_special.setObjectName('role_special')
        self.role2_special.resize(self.xr * 88, self.yr * 36)
        self.role2_special.move(self.xr * 10, self.yr * 26)
        self.role3.setObjectName('role')
        self.role3.resize(self.xr * 716, self.yr * 87)
        self.role3.move(self.xr * (108 - back_x), self.yr * (337 - back_y))
        self.role3_head.setObjectName('role_head')
        self.role3_head.resize(self.zr * 80, self.zr * 80)
        self.role3_head.move(self.xr * 10, self.yr * 4)
        self.role3_detail.setObjectName('role_detail')
        self.role3_detail.resize(self.xr * 606, self.yr * 87)
        self.role3_detail.move(self.xr * 110, self.yr * 0)
        self.role3_special.setObjectName('role_special')
        self.role3_special.resize(self.xr * 88, self.yr * 36)
        self.role3_special.move(self.xr * 10, self.yr * 26)
        self.role4.setObjectName('role')
        self.role4.resize(self.xr * 716, self.yr * 87)
        self.role4.move(self.xr * (108 - back_x), self.yr * (467 - back_y))
        self.role4_head.setObjectName('role_head')
        self.role4_head.resize(self.zr * 80, self.zr * 80)
        self.role4_head.move(self.xr * 10, self.yr * 4)
        self.role4_detail.setObjectName('role_detail')
        self.role4_detail.resize(self.xr * 606, self.yr * 87)
        self.role4_detail.move(self.xr * 110, self.yr * 0)
        self.role4_special.setObjectName('role_special')
        self.role4_special.resize(self.xr * 88, self.yr * 36)
        self.role4_special.move(self.xr * 10, self.yr * 26)
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
            exec('self.role1_card{}=QLabel(self.role1_detail)'.format(i))
            exec('self.role1_card{}.setObjectName("card")'.format(i))
            exec('self.role1_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role1_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
            exec('self.role2_card{}=QLabel(self.role2_detail)'.format(i))
            exec('self.role2_card{}.setObjectName("card")'.format(i))
            exec('self.role2_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role2_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
            exec('self.role3_card{}=QLabel(self.role3_detail)'.format(i))
            exec('self.role3_card{}.setObjectName("card")'.format(i))
            exec('self.role3_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role3_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
            exec('self.role4_card{}=QLabel(self.role4_detail)'.format(i))
            exec('self.role4_card{}.setObjectName("card")'.format(i))
            exec('self.role4_card{}.resize(self.xr*46,self.yr*67)'.format(i))
            exec('self.role4_card{}.move(self.xr*(xp+({}-t)*20),self.yr*10)'.format(i, i))
        self.back1_wi.setStyleSheet(
            '#back{border-radius:' + str(self.zr * 25) + 'px;}#role{border-radius:' + str(
                self.zr * 18) + 'px;}#role_head{border-radius:' + str(self.zr * 39) + 'px;}')

    def result_exit(self):
        self.result_exit_sg.emit()

if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication(sys.argv)

        window = Result()
        window.showFullScreen()
        sys.exit(app.exec())
