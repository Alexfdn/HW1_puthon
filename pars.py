import requests
import pandas as pd


def obj_pars():
    offset_ = 1
    limit_ = 100
    resss = []
    for i in range (30):
        url = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/kn/object?offset={offset_ * i * limit_}&limit={limit_}&sortField=devId.devShortCleanNm&sortType=asc&objStatus=0'
        res = requests.get(url)
        objects_data = res.json()
        objects_data.get('data').get('list')[0]
        objects_list = objects_data.get('data').get('list')
        objids = [x.get('objId') for x in objects_list]
        url_idd = url_form(objids)
        ress = append_json(url_idd)
        print(i)
        for n in range (len(ress)):
            resss.append(ress[n].json())
    save_dataframe(resss)
    



def url_form(objids):
    url_idd = []
    for i in range (len(objids)):
        idd = objids[i]
        url_idd.append(f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/object/{idd}')
    return url_idd


def append_json (url_idd):
    ress = []
    for i in url_idd:
        res = requests.get(i)
        ress.append(res)
    return ress



def save_dataframe(resss):
    a = pd.json_normalize(resss, max_level=3)
    print(a)
    df = pd.DataFrame(a)
    df.to_excel("panda.xlsx", index=True, header=True)


obj_pars()
