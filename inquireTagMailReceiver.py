import requests
import json

def Get(url, params):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.get(url, params=params, headers=headers)
    print(request.json())

def InquireTagMailReceiver(APP_KEY, apiFunction, requestId):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + requestId
    params = {}
    Get(url, params)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    inquireTagMailApi = 'tagMails'
    requestId = '2018121917070788070014'

    InquireTagMailReceiver(APP_KEY, inquireTagMailApi, requestId)