import requests
import csv

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
Y = '\033[33m' # yellow

proxylist = []
proxylist_fn = './proxy_list/proxy_list.csv'

with open(proxylist_fn, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0].strip())

for proxy in proxylist:
    try:
        r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=1)
        print(G + 'Succeeded ' + str(r.status_code) + ' ' + proxy + W)
    except Exception as e:
        print(R + 'Failed with ' + str(proxy) + W)

    if r.status_code == 200:
        print(r.json())
    else: pass
    print()
