from flask import Flask, json, request, Response
import hmac, hashlib, sys, requests, time, datetime


api = Flask(__name__)
api_secret = b'sY7r9XnXte31'

def verify(request):
    print('--- verify ---')
    messageId = request.headers.get('Twitch-Eventsub-Message-Id')
    timestamp = request.headers.get('Twitch-Eventsub-Message-Timestamp')
    hmac_message = messageId + timestamp + request.data.__str__()
    signature = hmac.new(api_secret, msg=hmac_message.encode('utf8'), digestmod=hashlib.sha256)
    hex_digest = signature.hexdigest()
    expected_signature = 'sha256=' + hex_digest
    actual_signature = request.headers.get('Twitch-Eventsub-Message-Signature')
    if actual_signature != expected_signature:
        return False
    else:
        return True

@api.route('/callback', methods=['POST'])
def callback():
    try:
        print('--- callback ---')
        if 'Twitch-Eventsub-Message-Type' in request.headers:
            match = verify(request)
            if request.headers.get('Twitch-Eventsub-Message-Type') == 'webhook_callback_verification':
                challenge = request.json["challenge"]
                return challenge

            elif request.headers.get('Twitch-Eventsub-Message-Type') == 'notification':
                return handle_notification(request)
            else:
                print(request)
                return Response(status=200)

        else:
            print(request.data.__str__())
            return Response(status=200)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return Response(status=500)

def handle_follow(request):
    try:
        print('--- handle follow ---')
        inc_user = {'id': request.json['event']['user_id'], 'username': request.json['event']['user_login'], 'display_name': request.json['event']['user_name']}
        print(users)
        print(inc_user['id'])
        for user in users:
            if(inc_user['id'] == user['id']):
                return Response(status=200)
        add_user(inc_user)
        flash_lights()
        return Response(status=200)
    except:
        print('error')
        return Response(status=200)
    

def handle_notification(request):
    try:
        print('--- handle notification ---')
        if request.json['subscription']['type'] == 'channel.follow':
            return handle_follow(request)
        else:
            print(request)
            return Response(status=200)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return Response(status=500)

def flash_lights():
    for light_id in lights:
        state = {'on': True, 'transitiontime': '1', 'bri': 255, 'hue': 9767}
        set_state(light_id, state)
    for light_id in lights:
        state = {'on': False, 'transitiontime': '1', 'bri': 255, 'hue': 9767}
        set_state(light_id, state)
    for light_id in lights:
        state = {'on': True, 'transitiontime': '1', 'bri': 255, 'hue': 9767}
        set_state(light_id, state)
    for light_id in lights:
        state = {'on': False, 'transitiontime': '1', 'bri': 255, 'hue': 9767}
        set_state(light_id, state)

def set_state(id, state):
    return json.loads(requests.put(f'https://192.168.1.203/api/62CjCwojQ2sykUNM56SFgH3zpszbolpci-VFNZKq/lights/{id}/state', data=json.dumps(state), verify=False).content.decode(encoding='utf8'))


def add_user(user):
    users.append(user)
    with open('users.json', "w") as outfile:  
        json.dump(users, outfile, indent=4) 

if __name__ == '__main__':
    with open('users.json', "r") as data:  
        users = json.load(data) 
    lights = json.loads(requests.get('https://192.168.1.203/api/62CjCwojQ2sykUNM56SFgH3zpszbolpci-VFNZKq/lights', data=json.dumps({"devicetype": "hueapi#autom"}), verify=False).content.decode(encoding='utf8'))
    api.run()