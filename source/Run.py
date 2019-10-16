from card import Rank
from card import Card
import random
import pickle
import requests
import numpy as np
import json
import os
import Game

deck = list(Card)
rank_list = list(Rank)
suit_dict = {"suit_c": "@", "suit_d": '#', "suit_h": "&", "suit_s": "$"}
level_dict = {'0': '散牌', '1': '对子', '2': '两对', '3': '连对', '4': '三条', '5': '顺子',
              '6': '同花', '7': '葫芦', '8': '炸弹', '9': '同花顺'}


# & $ # *
# ♥ ♠ ♦ ♣
# h s d c
def train():
    change_Weight = np.zeros((5, 10, 10))
    for first in range(5):
        for second in range(10):
            for third in range(10):
                change_Weight[first][second][third] = (third + second * +first) / 100

    change_Times = np.zeros((5, 10, 10))
    for first in range(5):
        for second in range(10):
            for third in range(10):
                change_Times[first][second][third] = 1

    if os.path.exists("model/a.txt"):
        change_Weight = pickle.load(open('model/a.txt', 'rb'))
    else:
        pickle.dump(change_Weight, open('model/a.txt', 'wb'))

    if os.path.exists("model/b.txt"):
        change_Times = pickle.load(open('model/b.txt', 'rb'))
    else:
        pickle.dump(change_Times, open('model/b.txt', 'wb'))
    ##########################
    Auto = True
    real = False
    beta = 0.9
    ##########################
    if (Auto == True):
        for i in range(50000):
            deck = list(Card)
            rank_list = list(Rank)
            random.shuffle(deck)
            myhand = [deck.pop() for __ in range(13)]
            myhand_2 = [deck.pop() for __ in range(13, 26)]
            myhand_3 = [deck.pop() for __ in range(26, 39)]
            myhand_4 = [deck.pop() for __ in range(39, 52)]
            myhand_2.sort()
            myhand_3.sort()
            myhand_4.sort()
            myhand.sort()
            b = Game.begin_game(myhand_2, change_Weight, change_Times, beta=beta, is_Train=False, Auto=Auto, b=0,
                                real=real)
            c = Game.begin_game(myhand_3, change_Weight, change_Times, beta=beta, is_Train=False, Auto=Auto, b=0,
                                real=real)
            d = Game.begin_game(myhand_4, change_Weight, change_Times, beta=beta, is_Train=False, Auto=Auto, b=0,
                                real=real)
            change_Weight, change_Times = Game.begin_game(myhand, change_Weight, change_Times, beta=beta, is_Train=True,
                                                          Auto=Auto, b=[b, c, d], real=real)
            if (i % 10000 == 0):
                print(i)
            pickle.dump(change_Weight, open('model/a.txt', 'wb'))
            pickle.dump(change_Times, open('model/b.txt', 'wb'))
        print(change_Weight)
    else:
        for i in range(1):
            deck = list(Card)
            rank_list = list(Rank)
            random.shuffle(deck)
            myhand = [deck.pop() for __ in range(13)]
            myhand_2 = [deck.pop() for __ in range(13, 26)]
            myhand_2.sort()
            myhand.sort()
            print("你的手牌：自己拼一个最牛逼的记一下，然后和下面的进行对比，输入电脑摆的牌赢了多少")
            print(myhand_2)
            print("AI的手牌：")
            print(myhand)
            print("Game Start：")
            b = Game.begin_game(myhand, change_Weight, change_Times, beta, is_Train=False, Auto=Auto, b=None, real=real)
            three = b['level_3'][0]
            two = b['level_2'][0]
            one = b['level_1'][0]


def play(token):
    for i in range(1):
        try:
            url = "https://api.shisanshui.rtxux.xyz/game/open"
            headers = {'x-auth-token': token}
            response = requests.request("POST", url, headers=headers)
            result = response.text.encode("utf8")
            result = json.loads(result)
            print(result)
            id = result['data']['id']
            card = result['data']['card']
            card = card.replace("10", 'T')
            card = card.replace("*", '@')
            hand_card = card.split()
            url = "https://api.shisanshui.rtxux.xyz/game/submit"
            Weight = pickle.load(open('./model/a.txt', 'rb'))
            Times = pickle.load(open('./model/b.txt', 'rb'))
            beta = 0.9
            myhand = []
            for i in range(13):
                myhand.append(Card(str(hand_card[i][1]) + str(hand_card[i][0])))
            print(myhand)
            myhand.sort()
            b = Game.begin_game(myhand, Weight, Times, beta, is_Train=False, Auto=False, b=None, real=True)
            three = b['level_3'][0]
            shape_3 = b['level_3'][1]
            two = b['level_2'][0]
            shape_2 = b['level_2'][1]
            one = b['level_1'][0]
            shape_1 = b['level_1'][1]
            a = []
            c = ''
            for i in range(3):
                c = c + str(one[i])[1] + str(one[i])[0]
                if (i != 2):
                    c += ' '
            c = c.replace("T", '10')
            c = c.replace("@", '*')
            a.append(c)
            c = ''
            for i in range(5):
                c = c + str(two[i])[1] + str(two[i])[0]
                if (i != 4):
                    c += ' '
            c = c.replace("T", '10')
            c = c.replace("@", '*')
            a.append(c)
            c = ''
            for i in range(5):
                c = c + str(three[i])[1] + str(three[i])[0]
                if (i != 4):
                    c += ' '
            c = c.replace("T", '10')
            c = c.replace("@", '*')
            a.append(c)
            payload = str({'id': id, 'card': a})
            payload = payload.replace(': ', ':')
            payload = payload.replace(', ', ',')
            payload = payload.replace("'", '"')
            headers = {
                'content-type': "application/json",
                'x-auth-token': token
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            result = response.text.encode("utf8")
            result = json.loads(result)
            status = result['status']
            msg = result['data']['msg']
            if (msg != 'Success'):
                print("11111111111")
                print(myhand)
                print(three)
                print(two)
                print(one)
                break
            flag_hand = []
            for i in range(13):
                f = str(myhand[i])
                q = str(f[1]) + str(f[0])
                q = q.replace("T", '10')
                flag_hand.append(q)
        except:
            need = {'status': 1}
            print(need)
            return need
        need = {'status': status, 'id': id, 'msg': msg, 'origin_cards': flag_hand, 'cards': []}

        flag_one = []
        for i in range(3):
            a = str(one[i])
            b = a[1] + a[0].replace("T", '10')
            flag_one.append(b)
        flag_two = []
        for i in range(5):
            a = str(two[i])
            b = a[1] + a[0].replace("T", '10')
            flag_two.append(b)
        flag_three = []
        for i in range(5):
            a = str(three[i])
            b = a[1] + a[0].replace("T", '10')
            flag_three.append(b)
        flag = {'lv': level_dict[str(shape_1)], 'card': flag_one}
        need['cards'].append(flag)
        flag = {'lv': level_dict[str(shape_2)], 'card': flag_two}
        need['cards'].append(flag)
        flag = {'lv': level_dict[str(shape_3)], 'card': flag_three}
        need['cards'].append(flag)
        print(need)
        return need


def find_info(id, token):
    try:
        url = "https://api.shisanshui.rtxux.xyz/history/" + str(id)
        headers = {'x-auth-token': token}
        response = requests.request("GET", url, headers=headers)
        result = response.text.encode("utf8")
        result = json.loads(result)
        status = result['status']
        data = result['data']
    except:
        need = {'status': 1}
        return need
    if status == 0:
        need = {'status': status, 'id': data['id'], 'time': data['timestamp'], 'details': []}
    else:
        need = {'status': 1}
        return need
    data = data['detail']
    for i in range(4):
        a = data[i]
        b = []
        if len(a['card']) == 1:
            flag_card = a['card'][0].replace("*", '@').split()
            b.append({'card': flag_card})
        else:
            for j in range(3):
                flag_card = a['card'][j].replace("*", '@').split()
                b.append({'card': flag_card})
        flag = {'name': a['name'], 'score': a['score'], 'cards': b}
        need['details'].append(flag)
    # print(need)
    return need


if __name__ == '__main__':
    print(find_info(12943, '5c65c5fd-904f-4c7b-9979-6d473f91587b'))
