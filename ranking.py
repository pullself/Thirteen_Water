from PyQt5.Qt import *
import sys


class Ranking(QWidget):
    def __init__(self,parent=None):
        super(Ranking, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)
        self.back2_wi = QWidget(self)
        self.rankexit_but = QPushButton(self)
        self.header1 = QLabel(self.back2_wi)
        self.comeback_but = QPushButton(self.back2_wi)
        self.next_but = QPushButton(self.back2_wi)
        self.table = QWidget(self.back2_wi)
        self.tablein = QGridLayout()
        self.headers = ['昵称', '排名', '积分', '详情']
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle('Rank')
        self.setObjectName('rank')
        self.resize(self.w, self.h)
        self.back2_wi.setObjectName('back')
        self.back2_wi.resize(self.xr*793, self.yr*534)
        self.back2_wi.move(self.xr*69, self.yr*53)
        self.rankexit_but.setObjectName('resexit')
        self.rankexit_but.resize(self.zr*38, self.zr*38)
        self.rankexit_but.move(self.xr*834, self.yr*36)
        self.header1.setObjectName('header')
        self.header1.resize(self.xr*172, self.yr*36)
        self.header1.move(self.xr*24, self.yr*10)
        self.comeback_but.setObjectName('comeback')
        self.comeback_but.resize(self.xr*80, self.yr*36)
        self.comeback_but.move(self.xr*67, self.yr*467)
        self.next_but.setObjectName('next')
        self.next_but.resize(self.zr*38, self.zr*38)
        self.next_but.move(self.xr*725, self.yr*468)
        # table = QTableWidget(back2_wi)
        # table.setObjectName('table')
        # table.resize(746, 382)
        # table.move(24, 61)
        # table.setRowCount(5)
        # table.setColumnCount(4)
        # table.setHorizontalHeaderLabels(['昵称', '排名', '积分', '详情'])
        # table.verticalHeader().setVisible(False)
        # for i in range(0, 4):
        #     table.setColumnWidth(i, 186)
        # for i in range(0, 5):
        #     table.setRowHeight(i, 70)
        self.table.setObjectName('table')
        self.table.resize(self.xr*746, self.yr*382)
        self.table.move(self.xr*24, self.yr*61)
        self.tablein.setSpacing(0)
        self.tablein.setContentsMargins(0, 0, 0, 0)
        self.table.setLayout(self.tablein)
        li = ['yellow', 'red', 'blue']
        for i in range(0, 4):
            for j in range(0, 5):
                exec('self.tableheader{}_{} = QLabel()'.format(i, j))
                exec('self.tableheader{}_{}.setObjectName("table_unit")'.format(i, j))
                exec('self.tableheader{}_{}.setStyleSheet("background-color: {};")'.format(i, j, li[i % 3]))
                exec('self.tablein.addWidget(self.tableheader{}_{}, {}, {})'.format(i, j, i, j))


if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        with open('result.qss', 'r') as f:
            app.setStyleSheet(f.read())
        window = Ranking()
        window.showFullScreen()
        sys.exit(app.exec())
