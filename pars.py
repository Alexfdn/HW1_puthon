import requests
import pandas as pd

offset_ = 1
limit_ = 12
url = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/kn/object?offset={offset_}&limit={limit_}&sortField=devId.devShortCleanNm&sortType=asc&objStatus=0'
res = requests.get(url)
objects_data = res.json()
objects_data.get('data').get('list')[0]

objects_list = objects_data.get('data').get('list')
objids = [x.get('objId') for x in objects_list]

url = []
for i in range (len(objids)):
    idd = objids[i]
    url.append(f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/object/{idd}')

ress = []
resss = []
for i in url:
    res = requests.get(i)
    ress.append(res)
for i in range (len(ress)):
    resss.append(ress[i].json())
a = pd.json_normalize(resss, max_level=3)
print(a)

df = pd.DataFrame(a)
df.to_excel("panda.xlsx", index=True, header=True)
