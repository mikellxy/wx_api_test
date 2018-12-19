import json
import requests

from .settings import Config

get_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'
create_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={access_token}'



def get_token(appid, secret, url=get_token_url):
    url = url.format(appid=appid, secret=secret)
    resp = requests.get(url)
    return resp.json().get('access_token')


def update_menu(token, menu_data, url=create_menu_url):
    url = url.format(access_token=token)
    menu_json = json.dumps(menu_data)
    resp = requests.post(url=url, data=menu_json)
    return resp.json()


def main():
    menu_data = {
        "button": [
            {
                "type": "click",
                "name": "hello",
                "key": "HIT_ME"
            }

        ]
    }
    token = get_token(Config.APPID, Config.SECRET)
    ret = update_menu(token, menu_data)
    print(ret)


if __name__ == '__main__':
    main()

