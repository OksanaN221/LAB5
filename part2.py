import requests
import json

def answ(response):
    response2 = requests.get(response)
    data2 = response2.json()

    people = []
    for i in data2['people']:
        people.append([i['name'], i['craft']])
    return people


def num(response):
    response2 = requests.get(response)
    data2 = response2.json()
    num = data2['number']
    return num


response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()

print(f"Timestamp:{data['timestamp']}")
print(f"Coordinates:{data['iss_position']['longitude']}, {data['iss_position']['latitude']}")

print("\n")

info = answ("http://api.open-notify.org/astros.json")

print('Number of people in space:', num("http://api.open-notify.org/astros.json"))
for k in info:
    print(' '.join(list(map(str, k))))

