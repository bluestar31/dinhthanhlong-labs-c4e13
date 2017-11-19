from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen('http://nhaczingmp3.com/bang-xep-hang/bai-hat-Viet-Nam/IWZ9Z08I.html')
html_content = website.read().decode('utf-8')
website.close()

soup = BeautifulSoup(html_content, 'html.parser')
div_title = soup.find('div', 'widget-title')
a_detail = div_title.a
a_title = a_detail['title']
print('\t\t\t',a_title)

ul_chart = soup.find('ul', 'box-song')
li_chart_list = ul_chart.find_all('li')
count = 1

for li in li_chart_list:
    a_detail = li.div.h3.a
    content = a_detail.string
    print('\t\t\t', count, content)
    print('\t\t\t','- '*30)
    count += 1
