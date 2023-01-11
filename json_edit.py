import json
with open('data/Jan2022dataBad.json') as f:
    data = json.load(f)

for i in range(len(data['values'])):
    if data['values'][i] > 1: #meaningless number
        data['values'][i] = -1

with open('data/Jan2022data.json', 'w') as f:
    json.dump(data, f)