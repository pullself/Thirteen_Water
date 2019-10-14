import sys
import requests


def change_vertical(ori):
    ans = ''
    for s in ori:
        ans = ans + s + '\n'
    ans.strip('\n')
    return ans

def register(ac,psw):
    url = 'https://api.shisanshui.rtxux.xyz/auth/register'
    payload = '{"username":'+'"{}"'.format(ac)+',"password":'+'"{}"'.format(psw)+'}'
    headers = {'content-type':'application/json'}
    res = requests.request('POST',url,data=payload,headers=headers)
    if res.json()['status']==1001:
        return 1
    else:
        return str(res.json()['data']['user_id'])


def login(ac,psw):
    url = 'https://api.shisanshui.rtxux.xyz/auth/login'
    payload = '{"username":'+'"{}"'.format(ac)+',"password":'+'"{}"'.format(psw)+'}'
    headers = {'content-type':'application/json'}
    res = requests.request('POST',url,data=payload,headers=headers)
    js = res.json()
    print(js)
 

if __name__ == "__main__":
    login('scksck','12346')
