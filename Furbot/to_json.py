import json

ar = []

with open('ban_word.txt',encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != "":
            ar.append(n)
with open('ban_word.json', 'w',encoding='utf-8') as e:
    json.dump(ar,e)
