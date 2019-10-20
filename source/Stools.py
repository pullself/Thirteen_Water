import requests
import json
import time


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
    if res == '':
        return {"status": 1}
    else:
        return res.json()


def login(ac, psw):
    url = 'https://api.shisanshui.rtxux.xyz/auth/login'
    payload = '{"username":' + '"{}"'.format(ac) + ',"password":' + '"{}"'.format(psw) + '}'
    headers = {'content-type': 'application/json'}
    res = requests.request('POST', url, data=payload, headers=headers)
    if res == '':
        return {"status": 1}
    else:
        return res.json()


def srank(id, token):
    url = "https://api.shisanshui.rtxux.xyz/history"
    querystring = {"page": 1, "limit": 18, "player_id": id}
    headers = {'x-auth-token': token}
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text.encode("utf8")
    result = json.loads(result)
    print(result)
    if result != '' and result['status'] == 0:
        try:
            status = result['status']
            data = result['data']
            need = {'status': status, 'details': []}
            for j in range(18):
                a = data[j]
                time_array = time.localtime(a['timestamp'])
                time_str = time.strftime("%Y-%m-%d %H:%M:%S",time_array)
                flag = {'id': a['id'], 'score': a['score'], 'time': time_str}
                need['details'].append(flag)
        except:
            need = {'status': 1}
    else:
        need = {'status': 1}
    print(need)
    return need


def rank():
    url = "https://api.shisanshui.rtxux.xyz/rank"
    response = requests.request("GET", url)
    result = response.text.encode("utf8")
    result = json.loads(result)
    if result != '':
        try:
            need = {'status': 0, 'details': []}
            for i in range(len(result)):
                a = result[i]
                flag = {'id': a['player_id'], 'name': a['name'], 'score': a['score']}
                need['details'].append(flag)
        except:
            need = {'status': 1}
    else:
        need = {'status': 1}
    return need


if __name__ == "__main__":
    srank(1050, "d0b4a33d-22c2-43cf-92ff-0af2b63a21ee")
