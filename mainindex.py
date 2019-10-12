from PyQt5.Qt import *
import sys
from Stools import change_vertical


class MainIndex(QWidget):
    def __init__(self):
        super(MainIndex, self).__init__()
        self.setWindowTitle('Hall')
        self.setObjectName('hall')
        self.resize(930, 640)
        self.setFixedSize(self.width(), self.height())
        self.set_ui()

    def set_ui(self):
        top_wi = QWidget(self)
        top_wi.setObjectName('top')
        top_wi.resize(930, 95)
        logo_la = QLabel(top_wi)
        logo_la.setObjectName('logo')
        logo_la.resize(65, 65)
        logo_la.move(29, 16)
        manual_but = QPushButton(self)
        manual_but.setObjectName('manual')
        manual_but.resize(180, 320)
        manual_but.move(112, 194)
        manual_but.setText(change_vertical('手动场'))
        manual_tex = QLabel(self)
        manual_tex.setObjectName('manual_tex')
        manual_tex.resize(34, 413)
        manual_tex.move(68, 152)
        manual_tex.setText(change_vertical('是当一辈子的懦夫，还是三十秒的勇士？'))
        auto_but = QPushButton(self)
        auto_but.setObjectName('auto')
        auto_but.resize(180, 320)
        auto_but.move(381, 194)
        auto_but.setText(change_vertical('自动场'))
        auto_tex = QLabel(self)
        auto_tex.setObjectName('auto_tex')
        auto_tex.resize(34, 413)
        auto_tex.move(323, 152)
        auto_tex.setText(change_vertical('机器就要由机器来终结'))
        home_but = QPushButton(self)
        home_but.setObjectName('home')
        home_but.resize(180, 320)
        home_but.move(660, 194)
        home_but.setText(change_vertical('沙之家'))
        home_tex = QLabel(self)
        home_tex.setObjectName('home_tex')
        home_tex.resize(34, 413)
        home_tex.move(595, 152)
        home_tex.setText(change_vertical('常回家看看！'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainIndex()
    window.show()
    sys.exit(app.exec())
