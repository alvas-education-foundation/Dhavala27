import​ requests
from​ bs4 ​import​ BeautifulSoup
r = requests.get(​"http://www.pythonhow.com/example.html"​)
c=r.content
c
soup=BeautifulSoup(c,​"html.parser"​)
print​(soup.prettify())
all​=soup.find_all(​"div"​,{​"class"​,​"cities"​})
all
all​[​0​].find_all(​"h2"​)[​0​].text
for​ item ​in​​all​:
    ​print​(item.find_all(​"p"​)[​0​].text)
