import requests

url = 'http://127.0.0.1:5000/belka/api/v1.0/getpred'

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}


params =[{'square': 43.7, 'n_floor': 5, 
        'district_len': 1, 'district_len_left': 0, 
        'district_ordg': 0, 'district_ordg_left': 0, 
        'district_right': 0},
        {'square': 43.9, 'n_floor': 5, 
        'district_len': 1, 'district_len_left': 0, 
        'district_ordg': 0, 'district_ordg_left': 0, 
        'district_right': 0},
        {'square': 65.0, 'n_floor': 9,  
        'district_len': 0, 'district_len_left': 0, 
        'district_ordg': 1, 'district_ordg_left': 0, 
        'district_right': 0}]
        
for p in params:
    response = requests.get(url, params=p, headers=headers)
    print(response.url)
    print(response.json())

#array([2534.38852785, 2261.95295137, 3327.13341683])