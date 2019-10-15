from PyQt5.Qt import *
import sys
import json


class SingleRank(QWidget):
    single_rk_comeback_sg = pyqtSignal()
    detail_sg = pyqtSignal(str)

    def __init__(self, parent=None):
        super(SingleRank, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)
        self.inlist = {}
        self.back2_wi = QWidget(self)
        self.rankexit_but = QPushButton(self)
        self.header1 = QLabel(self.back2_wi)
        self.comeback_but = QPushButton(self.back2_wi)
        self.next_but = QPushButton(self.back2_wi)
        self.table = QWidget(self.back2_wi)
        self.tablein = QGridLayout()
        self.headers = ['对局id', '分数', '时间', '详情']
        self.set_ui()
        with open('rank.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def set_ui(self):
        self.setWindowTitle('SingleRank')
        self.setObjectName('singlerank')
        self.resize(self.w, self.h)
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(10, 10)
        effect.setColor(QColor(0, 0, 0, 80))
        effect.setBlurRadius(20)
        effect1 = QGraphicsDropShadowEffect()
        effect1.setOffset(10, 10)
        effect1.setColor(QColor(0, 0, 0, 80))
        effect1.setBlurRadius(20)
        self.back2_wi.setObjectName('back')
        self.back2_wi.resize(self.xr * 793, self.yr * 534)
        self.back2_wi.move(self.xr * 69, self.yr * 53)
        self.back2_wi.setGraphicsEffect(effect)
        self.header1.setObjectName('header')
        self.header1.resize(self.xr * 172, self.yr * 36)
        self.header1.move(self.xr * 24, self.yr * 10)
        self.header1.setText('过往战绩')
        self.header1.setAlignment(Qt.AlignCenter)
        self.comeback_but.setObjectName('comeback')
        self.comeback_but.resize(self.xr * 80, self.yr * 36)
        self.comeback_but.move(self.xr * 67, self.yr * 467)
        self.comeback_but.setText('返回')
        self.comeback_but.clicked.connect(self.come_back)
        self.comeback_but.setGraphicsEffect(effect1)
        self.next_but.setObjectName('next')
        self.next_but.resize(self.zr * 38, self.zr * 38)
        self.next_but.move(self.xr * 725, self.yr * 468)
        self.next_but.setStyleSheet('border-radius:{}px;'.format(self.zr * 18))
        self.next_but.clicked.connect(self.next)
        self.table.setObjectName('table')
        self.table.resize(self.xr * 746, self.yr * 382)
        self.table.move(self.xr * 24, self.yr * 61)
        self.tablein.setSpacing(0)
        self.tablein.setContentsMargins(0, 0, 0, 0)
        self.table.setLayout(self.tablein)
        li = ['#f5f0e3', '#cccccc']
        for i in range(0, 5):
            for j in range(0, 4):
                if j == 3 and i != 0:
                    exec('self.tableheader{}_{} = QPushButton()'.format(i, j))
                    exec('self.tableheader{}_{}.setMinimumHeight(self.yr *382/5)'.format(i, j))
                    exec('self.tableheader{}_{}.setText("详情")'.format(i, j))
                    exec('self.tableheader{}_{}.clicked.connect(self.details{})'.format(i, j, i))
                else:
                    exec('self.tableheader{}_{} = QLabel()'.format(i, j))
                    exec('self.tableheader{}_{}.setAlignment(Qt.AlignCenter)'.format(i, j))
                if i == 0:
                    exec('self.tableheader{}_{}.setObjectName("table_head")'.format(i, j))
                    exec('self.tableheader{}_{}.setText("{}")'.format(i, j, self.headers[j]))
                else:
                    exec('self.tableheader{}_{}.setObjectName("table_unit")'.format(i, j))
                exec('self.tableheader{}_{}.setStyleSheet("background-color:{};")'.format(i, j, li[(i + j) % 2]))
                exec('self.tablein.addWidget(self.tableheader{}_{}, {}, {})'.format(i, j, i, j))
        self.back2_wi.setStyleSheet(
            '#back{border-radius:' + str(self.zr * 20) + 'px;}#header{border-radius:' + str(
                self.zr * 15) + 'px;font-size:' + str(
                int(self.zr * 18)) + 'px;}#comeback{border-radius:' + str(self.zr * 15) + 'px;font-size:' + str(
                int(self.zr * 16)) + 'px;}#table_unit{font-size:' + str(
                int(self.zr * 18)) + 'px;}#table_head{font-size:' + str(int(self.zr * 20)) + 'px;font-weight:bold}')

    def come_back(self):
        self.single_rk_comeback_sg.emit()

    def get_list(self, info):
        print(info)
        if len(info) >= 4:
            li = info[:4]
            self.inlist = info[4:]
        else:
            li = info
            self.inlist = info
        self.set_table(li)

    def set_table(self, mp):
        lens = len(mp)
        for i in range(1, lens + 1):
            self.next_but.setEnabled(True)
            exec('self.tableheader{}_0.setText("{}")'.format(i, mp[i - 1]['id']))
            exec('self.tableheader{}_1.setText("{}")'.format(i, mp[i - 1]['score']))
            exec('self.tableheader{}_2.setText("{}")'.format(i, mp[i - 1]['time']))
        if lens < 4:
            for i in range(lens + 1, 5):
                self.next_but.setEnabled(False)
                exec('self.tableheader{}_0.clear()'.format(i))
                exec('self.tableheader{}_1.clear()'.format(i))
                exec('self.tableheader{}_2.clear()'.format(i))

    def next(self):
        if len(self.inlist) >= 4:
            li = self.inlist[:4]
            self.inlist = self.inlist[4:]
        else:
            li = self.inlist
        self.set_table(li)

    def details1(self):
        if self.tableheader1_0.text() != '':
            self.detail_sg.emit(self.tableheader1_0.text())

    def details2(self):
        if self.tableheader2_0.text() != '':
            self.detail_sg.emit(self.tableheader2_0.text())

    def details3(self):
        if self.tableheader3_0.text() != '':
            self.detail_sg.emit(self.tableheader3_0.text())

    def details4(self):
        if self.tableheader4_0.text() != '':
            self.detail_sg.emit(self.tableheader4_0.text())


if __name__ == '__main__':
    with open('个人列表.json', 'r', encoding='UTF-8') as f:
        aa = json.load(f)
    app = QApplication(sys.argv)
    window = SingleRank()
    window.get_list(aa)
    window.showFullScreen()
    sys.exit(app.exec())
