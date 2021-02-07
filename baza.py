import mechanicalsoup as ms 
import sqlite3
bog=sqlite3.connect('malumot.db')
c=bog.cursor()
c.execute('CREATE TABLE malumotlar(ismlar text,manosi text)')
browser=ms.Browser()
url='http://ismlar.com/letter/boy/F'
page=browser.get(url)
soup=page.soup
ul=soup.select("ul")[2]
for i in [0,59]:
    li=ul.select("li")[i]
    a=li.select("a")
    urlm=f'https://ismlar.com/name/{a}'
    meta=browser.get(urlm)
    meta=meta.soup
    meta=meta.select("meta")[i]["content"]
    c.execute(f"INSERT INTO malumotlar VALUES ({a},{meta})")
bog.commit()
bog.close()
print('Yakunlandi:))')