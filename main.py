import requests
import json

f = open("datas_test_numeral.txt", "r")
for line in f:
    line = line.rstrip()
    num = int(line)
    template = 'http://numbersapi.com/{}/math?json=true'
    res = requests.get(template.format(num))
    data_json = res.text
    data_again = json.loads(data_json)
    if data_again["found"]:
        print("Interesting")
    else:
        print("Boring")
f.close()