import sys
import requests
from lxml import html
import os
import datetime

path = sys.argv[1]
url = 'https://www.anekdot.ru/release/anekdot/day'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

response = requests.get(url, headers=headers)

root = html.fromstring(response.text)

anekdot_list = []
for anekdot_xtext in root.xpath('//div[@class="topicbox"]/div[@class="text"]'):
    anekdot_list.append('\n'.join(anekdot_xtext.xpath('./text()')))

if not os.path.exists(path):
    os.makedirs(path)

with open('{0}/{1}.txt'.format(path, datetime.date.today()), 'w') as f:
    f.writelines('\n------------\n'.join(anekdot_list))
