from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__=="__main__":
    while 1:
        driver = webdriver.Chrome(r'C:/pythonTools/Tools/chromedriver.exe')
        # 设置浏览器窗口的位置和大小
        driver.set_window_position(20,40)
        driver.set_window_size(1100,700)
        path = "http://192.168.11.67/eportal/index.jsp?wlanuserip=38ede9139ec247e2f452c388d9189a02&wlanacname=2a9ead5bc601264ff44e7c7032f4e16dd57e63ddf1a91b00&ssid=&nasip=b3767e8ff469cefac1a5e44ffd87e53a&mac=3253653712e6a49e8c46d1d335582ff2&t=wireless-v2&url=ed45cb0bbc0c5769479a20ae02dc85564053a7962e772c02"
        # C:/python/loginSschoolNetwork/hello.html
        path1 = "http://192.168.11.67"
        driver.get(path1)
        driver.implicitly_wait(10)
        
        d = driver.find_element_by_id("username")
        driver.execute_script('arguments[0].removeAttribute(\"readonly\")',d);
        driver.implicitly_wait(10)
        driver.find_element_by_id("username").clear()
        driver.implicitly_wait(10)
        driver.find_element_by_id("username").click()
        driver.implicitly_wait(10)
        driver.find_element_by_id("username").send_keys("1834241002")
        driver.implicitly_wait(20)
        driver.find_element_by_id("username").send_keys(Keys.TAB)
        driver.implicitly_wait(10)
        driver.find_element_by_id("pwd").clear()
        driver.implicitly_wait(10)
        driver.find_element_by_id("pwd").click()
        driver.implicitly_wait(10)
        driver.find_element_by_id("pwd").send_keys("WZRwuzhaorui32.")
        driver.implicitly_wait(10)
        driver.find_element_by_id("loginLink_div").click()
        driver.implicitly_wait(20)
        time.sleep(3600)
        driver.quit()
