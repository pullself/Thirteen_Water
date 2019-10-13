from PyQt5.Qt import *
import sys


class Search(QWidget):
    search_sg = pyqtSignal()
    back_sg = pyqtSignal()

    def __init__(self, parent=None):
        super(Search, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)
        self.head = QLabel(self)
        self.search = QLineEdit(self)
        self.butt = QPushButton(self)
        self.but = QPushButton(self)
        self.set_ui()

    def set_ui(self):
        self.search.setObjectName('search')
        self.search.resize(self.xr * 520, self.yr * 40)
        self.search.move(self.xr * 205, self.yr * 300)
        self.search.setPlaceholderText('请输入战局id')
        self.search.setTextMargins(20, 0, 0, 0)
        self.search.setStyleSheet('font-size:{}px;border-radius:{}px;'.format(int(self.zr * 16), self.zr * 15))
        self.head.setObjectName('head')
        self.head.resize(self.xr * 200, self.yr * 50)
        self.head.move(self.xr * 360, self.yr * 240)
        self.head.setText('搜索战局')
        self.head.setAlignment(Qt.AlignCenter)
        self.head.setStyleSheet('font-size:{}px;'.format(int(self.zr * 25)))
        self.but.setObjectName('button')
        self.but.resize(self.xr * 130, self.yr * 40)
        self.but.move(self.xr * 480, self.yr * 380)
        self.but.setText('返回')
        self.but.clicked.connect(self.back_for)
        self.butt.setObjectName('button')
        self.butt.resize(self.xr * 130, self.yr * 40)
        self.butt.move(self.xr * 320, self.yr * 380)
        self.butt.setText('搜索')
        self.butt.clicked.connect(self.search_for)
        self.setStyleSheet('#button{font-size:' + str(int(self.zr * 18)) + 'px;border-radius:' + str(
            self.zr * 15) + 'px;background-color:#333643;color:#ffffff;}#button:hover{background-color:#575B6E;}#button:pressed{background-color:#202129;}')

    def search_for(self):
        self.id = self.search.text()
        self.search_sg.emit()
        # self.search.setStyleSheet('border:4px solid;border-color:red')
        # self.search.setPlaceholderText('id不存在')

    def back_for(self):
        self.back_sg.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Search()
    window.showFullScreen()
    sys.exit(app.exec())
