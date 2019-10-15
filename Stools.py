import sys
import requests
import json


def change_vertical(ori):
    ans = ''
    for s in ori:
        ans = ans + s + '\n'
    ans.strip('\n')
    return ans


def register(ac, psw):
    url = 'https://api.shisanshui.rtxux.xyz/auth/register'
    payload = '{"username":' + '"{}"'.format(ac) + ',"password":' + '"{}"'.format(psw) + '}'
    headers = {'content-type': 'application/json'}
    res = requests.request('POST', url, data=payload, headers=headers)
    if res == None:
        return {"status": 1}
    else:
        return res.json()


def login(ac, psw):
    url = 'https://api.shisanshui.rtxux.xyz/auth/login'
    payload = '{"username":' + '"{}"'.format(ac) + ',"password":' + '"{}"'.format(psw) + '}'
    headers = {'content-type': 'application/json'}
    res = requests.request('POST', url, data=payload, headers=headers)
    if res == None:
        return {"status": 1}
    else:
        return res.json()


def srank(id, token):
    url = "https://api.shisanshui.rtxux.xyz/history"
    querystring = {"page": 1, "limit": 20, "player_id": id}
    headers = {'x-auth-token': token}
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text.encode("utf8")
    result = json.loads(result)
    print(result)
    if result != '':
        status = result['status']
        data = result['data']
        need = {'status': status, 'details': []}
        for i in range(1):
            for j in range(20):
                a = data[j]
                flag = {'id': a['id'], 'score': a['score'], 'time': a['timestamp']}
                need['details'].append(flag)
    else:
        need = {'status': 1}
    return need


def rank():
    url = "https://api.shisanshui.rtxux.xyz/rank"
    response = requests.request("GET", url)
    result = response.text.encode("utf8")
    result = json.loads(result)
    if result != '':
        need = {'status': 0, 'details': []}
        for i in range(len(result)):
            a = result[i]
            flag = {'id': a['player_id'], 'name': a['name'], 'score': a['score']}
            need['details'].append(flag)
    else:
        need = {'status': 1}
    return need


if __name__ == "__main__":
    register('scksck', '123456')
