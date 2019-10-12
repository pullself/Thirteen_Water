from PyQt5.Qt import *
from index import Index
from mainindex import MainIndex
from result_four import Result
from home import Home
import sys


class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.h = self.screenRect.height()
        self.w = self.screenRect.width()
        self.xr = self.w / 930
        self.yr = self.h / 640
        self.zr = min(self.xr, self.yr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()


    def show_mainindex():
        ind.hide()
        mainind.showFullScreen()


    def show_result_four():
        mainind.hide()
        resultind.showFullScreen()


    def show_home():
        mainind.hide()
        homeind.showFullScreen()


    def result_exit():
        resultind.hide()
        mainind.showFullScreen()

    def home_exit():
        homeind.hide()
        mainind.showFullScreen()


    ind = Index(window)
    mainind = MainIndex(window)
    mainind.hide()
    resultind = Result(window)
    resultind.hide()
    homeind = Home(window)
    homeind.hide()
    window.showFullScreen()
    ind.show_mainindex_sg.connect(show_mainindex)
    mainind.auto_pressed_sg.connect(show_result_four)
    mainind.home_pressed_sg.connect(show_home)
    resultind.result_exit_sg.connect(result_exit)
    homeind.home_exit_sg.connect(home_exit)
    sys.exit(app.exec())
