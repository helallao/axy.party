import requests
from multiprocessing.dummy import Pool
import warnings
import random

warnings.filterwarnings('ignore')



#
#
#      download
#      urllib 1.23
#
#      pip install urllib==1.23
#


s = requests.Session()
s.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101'})


hata_ekran = s.get('https://axy.party/22', verify=False).text



def get(kelime, proxy, timeout):
    try:
        return [s.get(f'https://axy.party/{kelime}', proxies={'http': 'http://' + proxy, 'https': 'https://' + proxy}, timeout=timeout, verify=False), kelime]
    
    except:
        return [None, kelime]




kelimeler = [x for x in open('wordlist.txt', 'r').read().split('\n') if x]
proxies = s.get(f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=all&simplified=true').text.split('\r\n')[:-1]


pool = Pool(len(proxies))

threads = len(proxies)

found = []
denenen_sayisi = 0


while True:
    print(f'denendi {denenen_sayisi}')
    print('bulunanlar', found)
    print('son kelime', kelimeler[0])
    random.shuffle(proxies)
    processes = []
    
    for _index_ in range(threads):
        if len(kelimeler) < threads:
            for _index_ in range(len(kelimeler)):
                processes.append(pool.apply_async(get, [kelimeler[_index_], proxies[_index_], 10]))
        
        else:
            processes.append(pool.apply_async(get, [kelimeler[_index_], proxies[_index_], 10]))
    
    
    
    responses = []
    for process in processes:
        responses.append(process.get())
    
    
    for resp in responses:
        if resp[0] and resp[0].text != '<3' and resp[0].text != hata_ekran:
            found.append(resp[1])
            
            if resp[1] in kelimeler:
                kelimeler.remove(resp[1])
            
            denenen_sayisi += 1
            
        
        elif resp[0]:
            if resp[1] in kelimeler:
                kelimeler.remove(resp[1])
            
            denenen_sayisi += 1
    
    
    if len(kelimeler) == 0:
        break