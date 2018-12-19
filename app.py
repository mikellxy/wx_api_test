import time
import xmltodict
from hashlib import sha1

from flask import Flask, request, jsonify

TOKEN = 'lixinyu'

app = Flask(__name__)


@app.route('/weixin', methods=['POST', 'GET'])
def weixin():
    if request.method == 'GET':
        params = {
            'signature': request.args.get('signature'),
            'timestamp': request.args.get('timestamp'),
            'nonce': request.args.get('nonce'),
            'echostr': request.args.get('echostr'),
            'token': TOKEN,
        }
        result = validate_signature(params)
        if result is True:
            return params['echostr']
        return 'False'
    else:
        print(request.data, type(request.data))
        xml = xmltodict.parse(request.data)['xml']
        app_name = xml['ToUserName']
        user = xml['FromUserName']
        reply_dict = {
            'xml': {
                'ToUserName': user,
                'FromUserName': app_name,
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': 'Hello World!'
            }
        }
        return xmltodict.unparse(reply_dict)


def validate_signature(kwargs):
    params = {
        'token': kwargs['signature'],
        'timestamp': kwargs['timestamp'],
        'nonce': kwargs['nonce'],
    }
    sorted_params = sorted([v for k, v in params.items()])
    params_str = ''.join(sorted_params)
    sig = sha1(params_str.encode('utf-8')).hexdigest()
    return sig == kwargs['signature']


if __name__ == '__main__':
    app.run('0.0.0.0', 80)


