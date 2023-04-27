# web1.py
#크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지를 로딩(메서드 체인)
page = open("c:\\work\\test01.html","rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page,"html.parser")
#문서를 그대로 보여줌
#print(soup.prettify())

print("---<p>태그 전부 검색---")
print(soup.find_all("p"))
print("---<p>태그 하나를 검색하는 경우---")
print(soup.find("p"))
print("---<p class_=outer-text> 조건이 있는 경우---")
print(soup.find_all("p", class_="outer-text"))
print("---<p>태그에서 attrs 속성을 사용하는 경우(바로 위 결과와 동일)---")
print(soup.find_all("p", attrs={"class":"outer-text"}))
print("---태그 내부에 컨텐츠만 사용---")
for item in soup.find_all("p"):
    #태그를 버리고 컨텐츠만 사용
    title = item.text.strip()
    print(title)