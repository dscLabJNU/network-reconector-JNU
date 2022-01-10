import random
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import config
import os
import time

WEB_DRIVER_PATH="./driver/chromedriver.exe"
CAMPUS_NETWORK_URL = "http://192.168.11.67"
WEB_INITIALIZE_WAIT = 10
WEB_ACTION_WAIT = 1.5
WATCHDOG_PING_INTERVAL = 15
WATCHDOG_RETRY_INTERVAL = 5


def login() -> bool:
    account_list = list(config.ACCOUNT_POOL.keys())
    lucky_man = random.choice(account_list)
    username = config.ACCOUNT_POOL[lucky_man]['username']
    password = config.ACCOUNT_POOL[lucky_man]['passwd']
    print(f"The lucky man is {lucky_man}")

    driver: WebDriver = None
    try:
        driver = init_webdriver()
        driver.get(CAMPUS_NETWORK_URL)
        driver.implicitly_wait(WEB_INITIALIZE_WAIT)
        username_box = driver.find_element_by_id("username")
        driver.execute_script("arguments[0].style.display = 'block';", username_box)
        driver.implicitly_wait(WEB_ACTION_WAIT)
        username_box.click()
        driver.implicitly_wait(WEB_ACTION_WAIT)
        username_box.send_keys(username)
        driver.implicitly_wait(WEB_ACTION_WAIT)

        pwd_box = driver.find_element_by_id("pwd")
        driver.execute_script("arguments[0].style.display = 'block';", pwd_box)
        driver.implicitly_wait(WEB_ACTION_WAIT)
        pwd_box.click()
        driver.implicitly_wait(WEB_ACTION_WAIT)
        pwd_box.send_keys(password)
        driver.implicitly_wait(WEB_ACTION_WAIT)
        driver.find_element_by_id("loginLink").click()
        driver.implicitly_wait(WEB_ACTION_WAIT)
    except:
        return False
    finally:
        if driver is not None:
            driver.quit()
    return True


def init_webdriver() -> WebDriver:
    driver = webdriver.Chrome(WEB_DRIVER_PATH)
    driver.set_window_position(20, 40)
    driver.set_window_size(1100, 700)
    return driver


def ping(host: str) -> bool:
    response = os.system("ping -c 1 " + host)
    if response == 0:
        return True
    else:
        return False


def watchdog_loop() -> None:
    while True:
        if not ping("baidu.com"):
            print("Ping baidu.com failed, try to login...")
            while not login():
                print("Login failed, retry after {0} s".format(
                    WATCHDOG_RETRY_INTERVAL))
                time.sleep(WATCHDOG_RETRY_INTERVAL)
            print("Login successfuly, ping after {0} s".format(
                WATCHDOG_PING_INTERVAL))
        time.sleep(WATCHDOG_PING_INTERVAL)


def main():
    watchdog_loop()

if __name__ == "__main__":
    main()
