from selenium import webdriver
from selenium.webdriver.common.by import By

# 기본적으로 실행 시 driver 가 실행되고 자동화 테스트 소프트웨어를 통해 크롬이
# 제어되고 있다는 메세지를 확인 할 수 있다. 셀레니움이 제어하고 있다는 것이다.
# 프로그램이 종료되면 크롬 브라우저도 바로 닫힌다.
# 프로그램이 종료되어도 브라우저를 열어 두려면 웹 드라이버 설정을 변경해야 한다.

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

## ---------------------------------------------------------------------------

# Chrome / Firefox / Safari 사용가능 (꼭 대문자로 시작할 것.)
# 셀레니움 패키지에는 브라우저와 상호작용할 수 있는 코드가 담겨있다.
# 셀레니움 코드가 크롬 브라우저와 소통하도록 연결하는 다리가 필요하다.
# 그 다리가 크롬 드라이버이다. (사라피와 파이어폭스용 드라이버는 별도로 있다.)
driver = webdriver.Chrome(options=chrome_options)
# 드라이버를 사용해서 웹페이지 열기.

# driver.get("https://www.amazon.com/SLICE-RED-Android13-Smartphone-Fingerprint/dp/B0D5BN258W/ref=sr_1_9?crid=1D68JQ3R0E9G1&dib=eyJ2IjoiMSJ9.wLVCibRh4NX3wxMrXb_CgWEANsSVnxOC2FD_nw48Z0uy91gIZr_gVPgX_xmW3z990VQrXbgjg8omvWAXBmd8fsYvYLWw-df31Ji0WFK9DwF3SiXGl8mPrn7neT-62t5t0KOhJdEPzw8k5KgU6O4ndE1a8vnz6vaCH4dz8hq5wUfZhqZRVeVyVJIlRscfA4FA.cwZAWIpQ8TgPhVjMU6kS3r4oSrtyailTJfmL4iu-5kE&dib_tag=se&keywords=iphone&psr=EY17&qid=1722490843&s=todays-deals&sprefix=iphone%2Ctodays-deals%2C260&sr=1-9-catcorr&th=1")
driver.get("https://www.python.org/")

# value에는 Amazon 페이지의 가져올 데이터 span 클래스 이름을 넣으면 된다.
# price_doller = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# # 요소 안의 텍스트를 액세스하려면 텍스트 부분을 가져와야한다.
# # 요소 뒤에 .text 를 작성해주자.
# print(f"The price is {price_doller.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# # 클래스이름 말고도 ID로도 요소를 찾을 수 있다.
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# # a 태그에는 ID 나 CLASS 가 없는데 이럴 경우 상위 태그 중 div 에 있는 CLASS 이름으로 찾을 수 있다.
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Selenium 4.0 버전 이후 find_elements_by_css_selector() 메서드가 사라짐.
# driver.find_elements_by_css_selector(".event-widget time") 와 같은 결과.
event_times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events = {}
# 실제 텍스트라기보다는 셀레니움 객체가 될것이기 때문에 for문을 돌려서 무엇인지 확인하기.
# for time in event_times:
#     print(time.text)
# for name in event_names:
#     print(name.text)
for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(events)

## ---------------------------------------------------------------------------

# 브라우저를 닫으려는 메소드.
# close() -> 특정 페이지가 열려 있는 현재 활성 탭 하나를 닫는다.
# quit() -> 브라우저 전체를 종료한다. 동시에 여러 개의 탭이 열려 있을 때 전체 종료.
# driver.close()
driver.quit()

## ---------------------------------------------------------------------------