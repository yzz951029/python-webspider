from bs4 import BeautifulSoup
import urllib.request

print ('Hello world')

header='http://www.w3school.com.cn'
follower='/sql/index.asp'
url=header+follower
end='http://www.w3school.com.cn/sql/sql_summary.asp'
title='教程'

print(url)
response = urllib.request.urlopen(url)
html=response.read()
soup=BeautifulSoup(html,'lxml')
#print(soup.prettify())
'''for link in soup.find_all('div'):
    if link.get('id') =='maincontent':
        print (link.prettify())
        str=link.prettify('gbk')
        fileHandle=open((title+'.html'),'wb')
        fileHandle.write(str)
        fileHandle.close()
'''
for link in soup.find_all('a'):
    follower = link.get('href')
    if follower.startswith('/sql'):
        print(follower)
        title=link.get('title')
        url=header+follower
        response = urllib.request.urlopen(url)
        html=response.read()
        tempSoup=BeautifulSoup(html,'lxml')
        for tempLink in tempSoup.find_all('div'):
            if tempLink.get('id')== 'maincontent':
                str=tempLink.prettify('gbk')#坑在这里
                fileHandle=open((title+'.html'),'wb')
                fileHandle.write(str)
                fileHandle.close()