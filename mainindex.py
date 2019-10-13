from PyQt5.Qt import *
import sys
from Stools import change_vertical


class MainIndex(QWidget):
    auto_pressed_sg = pyqtSignal()
    home_pressed_sg = pyqtSignal()
    search_pressed_sg = pyqtSignal()

    def __init__(self, parent=None):
        super(MainIndex, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)
        self.top_wi = QWidget(self)
        self.logo_la = QLabel(self.top_wi)
        self.manual_but = QPushButton(self)
        # self.manual_tex = QLabel(self)
        self.auto_but = QPushButton(self)
        # self.auto_tex = QLabel(self)
        self.home_but = QPushButton(self)
        # self.home_tex = QLabel(self)
        self.set_ui()
        with open('mainindex.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def set_ui(self):
        self.setWindowTitle('Hall')
        self.setObjectName('hall')
        self.resize(self.w, self.h)
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
        self.top_wi.setObjectName('top')
        self.top_wi.resize(self.xr * 930, self.yr * 95)
        self.logo_la.setObjectName('logo')
        self.logo_la.resize(self.zr * 65, self.zr * 65)
        self.logo_la.move(self.xr * 29, self.yr * 16)
        self.manual_but.setObjectName('box')
        self.manual_but.resize(self.xr * 180, self.yr * 320)
        self.manual_but.move(self.xr * 112, self.yr * 194)
        self.manual_but.setText(change_vertical('战局搜索'))
        self.manual_but.setStyleSheet('border-radius:{}px;font-size:{}px;'.format(self.zr * 20, int(self.zr * 30)))
        self.manual_but.setGraphicsEffect(effect1)
        self.manual_but.clicked.connect(self.search_press)
        # self.manual_tex.setObjectName('manual_tex')
        # self.manual_tex.resize(self.xr * 34, self.yr * 413)
        # self.manual_tex.move(self.xr * 68, self.yr * 152)
        # self.manual_tex.setText(change_vertical('是当一辈子的懦夫，还是三十秒的勇士？'))
        # self.manual_tex.setStyleSheet('font-size:{}px;'.format(int(self.zr * 17)))
        self.auto_but.setObjectName('box')
        self.auto_but.resize(self.xr * 180, self.yr * 320)
        self.auto_but.move(self.xr * 381, self.yr * 194)
        self.auto_but.setText(change_vertical('自动场'))
        self.auto_but.setStyleSheet('border-radius:{}px;font-size:{}px;'.format(self.zr * 20, int(self.zr * 30)))
        self.auto_but.setGraphicsEffect(effect2)
        self.auto_but.clicked.connect(self.auto_press)
        # self.auto_tex.setObjectName('auto_tex')
        # self.auto_tex.resize(self.xr * 34, self.yr * 413)
        # self.auto_tex.move(self.xr * 340, self.yr * 152)
        # self.auto_tex.setText(change_vertical('机器就要由机器来终结'))
        # self.auto_tex.setStyleSheet('font-size:{}px;'.format(int(self.zr * 17)))
        self.home_but.setObjectName('box')
        self.home_but.resize(self.xr * 180, self.yr * 320)
        self.home_but.move(self.xr * 660, self.yr * 194)
        self.home_but.setText(change_vertical('沙之家'))
        self.home_but.setStyleSheet('border-radius:{}px;font-size:{}px;'.format(self.zr * 20, int(self.zr * 30)))
        self.home_but.setGraphicsEffect(effect3)
        self.home_but.clicked.connect(self.home_press)
        # self.home_tex.setObjectName('home_tex')
        # self.home_tex.resize(self.xr * 34, self.yr * 413)
        # self.home_tex.move(self.xr * 610, self.yr * 152)
        # self.home_tex.setText(change_vertical('常回家看看！'))
        # self.home_tex.setStyleSheet('font-size:{}px;'.format(int(self.zr * 17)))

    def auto_press(self):
        self.auto_pressed_sg.emit()

    def home_press(self):
        self.home_pressed_sg.emit()

    def search_press(self):
        self.search_pressed_sg.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainIndex()
    window.showFullScreen()
    sys.exit(app.exec())
