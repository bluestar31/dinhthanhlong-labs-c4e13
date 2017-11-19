from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
html_content = website.read().decode('utf-8')
website.close()

soup = BeautifulSoup(html_content, 'html.parser')
table_data = soup.find('table', id = 'tableContent')
tr_data_list = table_data.find_all('tr')

for tr in tr_data_list:
    td_data_list = tr.find_all('td')
    for td in td_data_list:
        content = td.string
        if content == None:
            continue
        print('\t',content, sep = '\t')
        print('\t','- ' * 30)
