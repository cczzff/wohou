import requests

if __name__ == '__main__':
    data = {
        'username': "15273165640",
        'password': '123456'
    }
    token_info = requests.post('http://127.0.0.1:8000/api-token-auth/', data=data)
    token = token_info.json()
    token = token['token']

    headers = {'Authorization': 'Token {}'.format(token)}
    banners = requests.get('http://127.0.0.1:8000/banners', headers=headers)

    print banners.json()