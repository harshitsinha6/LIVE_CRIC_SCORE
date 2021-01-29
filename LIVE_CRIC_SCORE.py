
import json

'''
data = json.loads("https://www.espncricinfo.com/static/json/manifest.json")
print(data)
'''

import requests
url = "https://hs-consumer-api.espncricinfo.com/v1/pages/matches/live?"

'''
https://hs-consumer-api.espncricinfo.com/v1/pages/matches/live?
'''

response = requests.get(url)

# print(response.text)

data = json.loads(response.text)

# print(data)

for ele in data:
    # print(data[ele])
    # print(type(data[ele]))
    for k, v in data[ele].items():
        for e in v:
            # print(type(e))
            # print(e['status'] == 'Live', e['status'])
            if e['status'] == 'Live':
                # for k1, v1 in e.items():
                #    print('key: ', k1, '\t\t\t\t value: ', v1)
                
                print('MATCH DETAILS: ')
                print(e['slug'])
                print(e['format'])
                print(e['status'], '\t\t\t\t\t', e['statusText'])
                
                
            
                print("\n\n\n\n")
