import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 1340, "name": "Joe", "views": 10005400}
    , {"likes": 120, "name": "How to", "views": 10340000}
    , {"likes": 1430, "name": "Tim", "views": 100000}]

for i in range(len(data)):
    response = requests.get(BASE + "video/2")
    print(response.json())
    response = requests.put(BASE + "video/1" + str(i), data[i])
    print (response.json())


response = requests.get(BASE + "video/2")
print (response.json())