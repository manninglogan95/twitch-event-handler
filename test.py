import requests, json, time, threading

def flash_lights():
    for light_id in lights:
        state = {'on': True, 'transitiontime': '1', 'bri': 255, 'hue': 9767}
        set_state(light_id, state)
    time.sleep(.1)
    for light_id in lights:
        state = {'on': False, 'transitiontime': '1', 'bri': 255, 'hue': 9767}
        set_state(light_id, state)
    time.sleep(.1)
    for light_id in lights:
        state = {'on': True, 'transitiontime': '1', 'bri': 255, 'hue': 9767}
        set_state(light_id, state)
    time.sleep(.1)
    for light_id in lights:
        state = {'on': False, 'transitiontime': '1', 'bri': 255, 'hue': 9767}
        set_state(light_id, state)


def set_state(id, state):
    return json.loads(requests.put(f'https://192.168.1.203/api/62CjCwojQ2sykUNM56SFgH3zpszbolpci-VFNZKq/lights/{id}/state', data=json.dumps(state), verify=False).content.decode(encoding='utf8'))


def add_user(user):
    users.append(user)
    with open('users.json', "w") as outfile:  
        json.dump(users, outfile, indent=4) 

lights = json.loads(requests.get('https://192.168.1.203/api/62CjCwojQ2sykUNM56SFgH3zpszbolpci-VFNZKq/lights', data=json.dumps({"devicetype": "hueapi#autom"}), verify=False).content.decode(encoding='utf8'))
    

with open('users.json', "r") as data:  
    users = json.load(data) 

inc_user = {"name": "joe", "id": 2}
for user in users:
    if(inc_user['id'] == user['id']):
        print('exists')
    else:
        print('dont exists')
        add_user({"name": "joe", "id": 2})

# state = {'on': True, 'bri': 255, 'hue': 7676}
# set_state(2, state)