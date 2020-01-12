import datetime
import requests


now_time = datetime.datetime.now()
ds = datetime.datetime.now().strftime('%Y%m%d')


def open_door():

    payload = {
    }
    headers = {
        "User-Agent": "RJSmartDoor/2.1.0 (Ruijia.RJSmartDoor; build:55; iOS 13.3.0) Alamofire/4.8.2"
    }

    resp = requests.post(url="", data=payload, headers=headers)
    resp_data = resp.json()
    if resp_data['status'] == 0:
        return True
    return False


if __name__ == '__main__':
    open_door()