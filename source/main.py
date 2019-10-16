from PyQt5.Qt import *
from index import Index
from register import Register
from mainindex import MainIndex
from search import Search
from result import ResultSingle
from result_four import Result
from home import Home
from ranking import Ranking
from singlerank import SingleRank
import sys
from Run import find_info

usr_id = None
token_p = None


def show_mainindex(ids, token):
    global usr_id
    global token_p
    print(token)
    print(ids)
    usr_id = ids
    token_p = token
    ind.hide()
    mainind.get_token(token_p)
    mainind.showFullScreen()


def show_register():
    ind.hide()
    regind.showFullScreen()


def register_ok():
    regind.hide()
    ind.showFullScreen()


def show_result(res):
    mainind.hide()
    sresultind.set_role(res)
    sresultind.showFullScreen()


def show_home():
    mainind.hide()
    homeind.get_id(usr_id)
    homeind.get_token(token_p)
    homeind.showFullScreen()


def show_search():
    mainind.hide()
    searchind.get_token(token_p)
    searchind.showFullScreen()


def show_id(res):
    searchind.hide()
    res = res['details']
    resultind.set_role(res)
    resultind.showFullScreen()


def back_off():
    searchind.hide()
    mainind.showFullScreen()


def result_exit():
    resultind.hide()
    mainind.showFullScreen()


def sresult_exit():
    sresultind.hide()
    mainind.showFullScreen()


def home_exit():
    homeind.hide()
    mainind.showFullScreen()


def show_rank(res):
    homeind.hide()
    rankind.get_list(res)
    rankind.showFullScreen()


def show_single_rank(res):
    homeind.hide()
    sgrankind.get_list(res)
    sgrankind.showFullScreen()


def rank_exit():
    rankind.hide()
    homeind.showFullScreen()


def single_rank_exit():
    sgrankind.hide()
    homeind.showFullScreen()


def show_de(id_p):
    res = find_info(id_p, token_p)
    if res['status'] == 0:
        resultind.set_role(res['details'])
        sgrankind.hide()
        resultind.showFullScreen()


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
        self.resize(self.w, self.h)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./resource/image/back.jpg").scaled(self.size())))
        self.setPalette(palette)


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
    sresultind = ResultSingle(window)
    sresultind.hide()
    resultind = Result(window)
    resultind.hide()
    homeind = Home(window)
    homeind.hide()
    rankind = Ranking(window)
    rankind.hide()
    sgrankind = SingleRank(window)
    sgrankind.hide()
    window.showFullScreen()
    # 登陆界面切换主界面
    ind.show_mainindex_sg.connect(show_mainindex)
    # 登陆界面切换注册界面
    ind.show_register_sg.connect(show_register)
    # 注册界面切登陆界面
    regind.register_ok_sg.connect(register_ok)
    # 主界面切自动对战
    mainind.auto_pressed_sg.connect(show_result)
    # 主界面切用户中心
    mainind.home_pressed_sg.connect(show_home)
    # 主界面切搜索
    mainind.search_pressed_sg.connect(show_search)
    # 搜索切结果
    searchind.search_sg.connect(show_id)
    # 搜索返回
    searchind.back_sg.connect(back_off)
    # 自动对战返回
    sresultind.result_exit_sg.connect(sresult_exit)
    # 结果返回
    resultind.result_exit_sg.connect(result_exit)
    # 用户中心返回
    homeind.home_exit_sg.connect(home_exit)
    # 用户中心切排行榜
    homeind.rank_sg.connect(show_rank)
    # 用户中心切个人战绩
    homeind.single_rank_sg.connect(show_single_rank)
    # 排行榜返回
    rankind.rk_comeback_sg.connect(rank_exit)
    # 个人战绩返回
    sgrankind.single_rk_comeback_sg.connect(single_rank_exit)
    # 详情
    sgrankind.detail_sg.connect(show_de)
    sys.exit(app.exec())
