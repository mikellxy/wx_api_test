import json
import requests

get_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'
create_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={access_token}'
appid = 'wx67ce505cc57ed363'
secret = '8fdc163f9f6275688c095b99c92bd6d0'


def get_token(appid=appid, secret=secret, url=get_token_url):
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
    token = get_token()
    ret = update_menu(token, menu_data)
    print(ret)


if __name__ == '__main__':
    main()

