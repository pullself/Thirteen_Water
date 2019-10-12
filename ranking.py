from PyQt5.Qt import *
import sys


class Ranking(QWidget):
    def __init__(self):
        super(Ranking, self).__init__()
        self.setWindowTitle('Rank')
        self.setObjectName('rank')
        self.resize(930, 640)
        self.setFixedSize(self.width(), self.height())
        self.set_ui()

    def set_ui(self):
        back2_wi = QWidget(self)
        back2_wi.setObjectName('back')
        back2_wi.resize(793, 534)
        back2_wi.move(69, 53)
        rankexit_but = QPushButton(self)
        rankexit_but.setObjectName('resexit')
        rankexit_but.resize(38, 38)
        rankexit_but.move(834, 46)
        header1 = QLabel(back2_wi)
        header1.setObjectName('header')
        header1.resize(172, 36)
        header1.move(24, 10)
        comeback_but = QPushButton(back2_wi)
        comeback_but.setObjectName('comeback')
        comeback_but.resize(80, 36)
        comeback_but.move(67, 467)
        next_but = QPushButton(back2_wi)
        next_but.setObjectName('next')
        next_but.resize(38, 38)
        next_but.move(725, 468)
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
        table = QWidget(back2_wi)
        table.setObjectName('table')
        table.resize(746, 382)
        table.move(24, 61)
        tablein = QGridLayout()
        tablein.setSpacing(0)
        tablein.setContentsMargins(0, 0, 0, 0)
        table.setLayout(tablein)
        headers = ['昵称', '排名', '积分', '详情']
        li = ['yellow', 'red', 'blue']
        for i in range(0, 4):
            for j in range(0, 5):
                exec('tableheader{}_{} = QLabel()'.format(i, j))
                exec('tableheader{}_{}.setObjectName("table_unit")'.format(i, j))
                exec('tableheader{}_{}.setStyleSheet("background-color: {};")'.format(i, j, li[i % 3]))
                exec('tablein.addWidget(tableheader{}_{}, {}, {})'.format(i, j, i, j))


if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        with open('result.qss', 'r') as f:
            app.setStyleSheet(f.read())
        window = Ranking()
        window.show()
        sys.exit(app.exec())
