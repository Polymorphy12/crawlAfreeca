import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#아프리카 모바일 웹에서 표시하는 방송 썸네일 이미지들을 다운로드 하는 크롤러다.
#드라이버는 크롬 드라이버를 사용하기로 한다.
#참고 : http://www.fun-coding.org/crawl_advance3.html
#       http://jjssoolee.tistory.com/1
#       아래의 URL은 python3 환경에서 지원되는 라이브러리로
#       이미지 다운로드하는 방법을 설명해주고 있다.
#       http://moogii.tistory.com/entry/Python3-URL%EB%A1%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C

options = webdriver.ChromeOptions()
##options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36")


driver = webdriver.Chrome('C:/Users/Sumin/Desktop/study/chromedriver', chrome_options=options)
##driver = webdriver.Chrome('C:/Users/Sumin/Desktop/study/chromedriver')
#웹 자원 로드를 위해 3초까지 기다려준다.
driver.implicitly_wait(1)


#웹드라이버로 아프리카 TV URL을 실행한다.
driver.get('http://m.afreecatv.com/#/home')

time.sleep(1)

#홈페이지에서 "게임" 목록에 해당하는 탭을 클릭한다.
#클릭 하나 하기 참 힘들었다. 나중에도 다시 삽질 할 수 있으니 공부해야할 링크를 남긴다.
#https://trello.com/b/Jkson2mm/untitled-board
#여기에서 "크롤링 -> Selenium에서 요소 찾아 내는 법"을 참고하길 바란다.
child = driver.find_element_by_class_name('inner_scroll')
parent = child.find_element_by_xpath("//a[contains(text(), '게임')]")
parent = parent.find_element_by_xpath('..')
parent.click()

#원하는 요소를 잘 가져왔는지 확인용 출력함수
##print(child.text)
##print(parent.text)


#i 번 스크롤을 맨 아래로 내려서 다음 페이지를 불러온다.
#
# 주석 처리된 코드를 사용하니 미처 업로드 되지 않은 썸네일 사진들이 있어서 용량이 아주 작은 기본 사진이 다운로드 되는 경우가 많았다.
# 따라서 주석처리한 코드처럼 한번에 맨 끝까지 스크롤 하지 않고 조금씩 스크롤하는 방법을 선택하기로 했다.
##i = 0
##while i < 8:
##    i = i+1
##    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
##    time.sleep(1)

elem = driver.find_element_by_tag_name("body")
 
no_of_pagedowns = 30
 
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1



#전체 페이지를 BeautifulSoup으로 파싱한다.
bs = BeautifulSoup(driver.page_source, 'html.parser')


#썸네일 사진을 담고 있는 URL들을 찾는다.
thumbnail_spans = bs.find_all("span",{"class":"thumb"})

i = 0
for span in thumbnail_spans:
    thumb = span.find("img")
    urllib.request.urlretrieve(thumb["src"],"C://Users/Sumin/Desktop/study/crawling/thumbnails/afreeca3/"+ str(i)+".jpg")
    i += 1
    print(thumb["src"])





#urllib.request.urlretrieve("http://iflv14.afreecatv.com/save/afreeca/station/2018/0618/14/thumb/1529299944745183_L_7.jpg","C://Users/Sumin/Desktop/study/crawling/thumbnails/afreeca/thumbnail.jpg")
