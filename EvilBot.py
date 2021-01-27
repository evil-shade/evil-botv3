from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import sys
from random import randint
import time
import schedule
import itertools
import website_links

profile = webdriver.FirefoxProfile()
options = Options()
options.headless = False
options.add_argument('--incognito')
options.add_argument('Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--ref')
options.add_argument('--disable-blink-features')

profile.set_preference('excludeSwitches', 'enable-automation')
profile.set_preference("dom.webserver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)
profile.set_preference("network.proxy.socks_version", 5)

profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path='C:\Program Files (x86)\geckodriver.exe')

action_chains = ActionChains(driver)
action_chains.send_keys(Keys.ARROW_DOWN)

completed_views = 0


def scroll_down():
    i = 0
    sys.stdout.write("\rScrolling")
    while i < 150:
        action_chains.perform()
        time.sleep(0.04)
        i = i + 1


def ran_time():
    sec = randint(7, 15)
    sys.stdout.write('\r ')
    for remaining in range(sec, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("wait {:2d} seconds.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete! ")


def loop():
    global completed_views
    i = randint(300, 1000)
    try:
        while i > 0:
            url = website_links.link
            sys.stdout.write('\rOpening Link : ' + url)
            driver.get(url)
            scroll_down()
            ran_time()
            i -= 1
            completed_views += 1
            sys.stdout.write('\r ')
            a = str(completed_views)
            sys.stdout.write(a)
            time.sleep(1)

    except Exception as e:
        print(e)
        print("you got", completed_views, "visitors")

    print("you got", completed_views, "visitors")


if __name__ == '__main__':
    print("##################################################################################")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                             Generate free traffic                              #")
    print("#                             v 3.1                                              #")
    print("#  From: Evil_Shade                                                              #")
    print("##################################################################################")
    print("Change your  SOCKES to 127.0.0.1:9050")
    # loop()
    schedule.every(3).seconds.do(loop)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("24:00").do(loop)
    # schedule.every(5).to(10).minutes.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    # schedule.every().minute.at(":17").do(job)

    while True:
        for c in itertools.cycle(['.', '..', '...']):
            sys.stdout.write('\r ')
            schedule.run_pending()
            sys.stdout.write('\rWaiting' + c)
            sys.stdout.flush()
            time.sleep(1)
