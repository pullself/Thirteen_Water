from PyQt5.Qt import *
from index import Index
from register import Register
from mainindex import MainIndex
from search import Search
from result_four import Result
from home import Home
from ranking import Ranking
from singlerank import SingleRank
import sys


def show_mainindex():
    ind.hide()
    mainind.showFullScreen()


def show_register():
    ind.hide()
    regind.showFullScreen()


def register_ok():
    regind.hide()
    ind.showFullScreen()


def show_result_four():
    mainind.hide()
    resultind.showFullScreen()


def show_home():
    mainind.hide()
    homeind.showFullScreen()


def show_search():
    mainind.hide()
    searchind.showFullScreen()


def show_id():
    searchind.hide()
    resultind.showFullScreen()


def back_off():
    searchind.hide()
    mainind.showFullScreen()


def result_exit():
    resultind.hide()
    mainind.showFullScreen()


def home_exit():
    homeind.hide()
    mainind.showFullScreen()


def show_rank():
    homeind.hide()
    rankind.showFullScreen()


def show_single_rank():
    homeind.hide()
    sgrankind.showFullScreen()


def rank_exit():
    rankind.hide()
    homeind.showFullScreen()


def single_rank_exit():
    sgrankind.hide()
    homeind.showFullScreen()


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
    ind = Index(window)
    regind = Register(window)
    regind.hide()
    mainind = MainIndex(window)
    mainind.hide()
    searchind = Search(window)
    searchind.hide()
    resultind = Result(window)
    resultind.hide()
    homeind = Home(window)
    homeind.hide()
    rankind = Ranking(window)
    rankind.hide()
    sgrankind = SingleRank(window)
    sgrankind.hide()
    window.showFullScreen()
    ind.show_mainindex_sg.connect(show_mainindex)
    ind.show_register_sg.connect(show_register)
    regind.register_ok_sg.connect(register_ok)
    mainind.auto_pressed_sg.connect(show_result_four)
    mainind.home_pressed_sg.connect(show_home)
    mainind.search_pressed_sg.connect(show_search)
    searchind.search_sg.connect(show_id)
    searchind.back_sg.connect(back_off)
    resultind.result_exit_sg.connect(result_exit)
    homeind.home_exit_sg.connect(home_exit)
    homeind.rank_sg.connect(show_rank)
    homeind.single_rank_sg.connect(show_single_rank)
    rankind.rk_comeback_sg.connect(rank_exit)
    sgrankind.single_rk_comeback_sg.connect(single_rank_exit)
    sys.exit(app.exec())
