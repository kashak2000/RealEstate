import requests
import bs4
import pandas as pd
import urllib
from time import sleep


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



def parsing():
    columns_name = [
    'Дата',
    'Тип квартиры',
    'Район', 
    'Адрес', 
    'Этаж',
    'Площадь о',
    'Площадь ж',
    'Площадь к',
    'Примечание',
    'Цена',
    'ПТелефон',
    'Агенство',
    'Email'
    ]
    
    data = []

    url = 'http://citystar.ru/detal.htm?d=43&nm=%CE%E1%FA%FF%E2%EB%E5%ED%E8%FF+%2D+%CF%F0%EE%E4%E0%EC+%EA%E2%E0%F0%F2%E8%F0%F3+%E2+%E3%2E+%CC%E0%E3%ED%E8%F2%EE%E3%EE%F0%F1%EA%E5&pN={}'
    
    for i in range(1,100):
        # 
        page = requests.get(url.format(i), headers=headers, proxies=urllib.request.getproxies())
        if page.status_code == 200:
            print('url: ', url.format(i))
            sleep(1)
            # Конвертация страницы в bs4
            page_soup = bs4.BeautifulSoup(page.content, "lxml")
            rows = page_soup.find_all('tr', attrs={'class': 'tbb'}) # Все строки таблицы
            for row in rows:
                columns = row.find_all('td')
                if len(columns) == 14:
                    # Запись конента строки
                    row_content = []
                    for col in columns[1:]:  
                        row_content.append(col.text.strip())
                else:
                    print('Не 14')
                
                data.append(row_content)
            
            pd.DataFrame(data=data, columns=columns_name).to_csv('./data/real_estate.csv')
        else:
            break

parsing()