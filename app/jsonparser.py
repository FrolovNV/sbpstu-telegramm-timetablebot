import requests
import json

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
    , 'accept': 'text/plain', 'content-type': 'application/json'}

def get_json(user_id):
    response = requests.get("https://soprachev.com/api/timetableBot/get", json={'apiKey':'test', 'userID': str(user_id)})
    if response.status_code != 200:
        print("Problem with API")
        return False
    data = json.loads(response.text)
    print(data)
    return data['url']


def post_json(user_id, url):
    jsons_str = {"apiKey": "test", "userID": str(user_id), "url": url}
    print(json.dumps(jsons_str))
    response = requests.post("https://soprachev.com/api/timetableBot/update", data=json.dumps(jsons_str), headers=HEADERS)
    if response.status_code != 200:
        print("Problem with my mind")
        print(response.text)
        return
    print(response.text)
    return True
    