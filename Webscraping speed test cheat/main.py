import time

import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "C:/Users/kuba/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome()
url = "https://10fastfingers.com/typing-test/english"
driver.get(url)
time.sleep(4)

# Correct the XPath for cookies button
cookies = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
cookies.click()

input_tag = driver.find_element(By.XPATH, '//*[@id="inputfield"]')
input_tag.click()

index = 1


def main():
    text_list = []
    global index
    while driver.find_element(By.XPATH, f'//*[@id="row1"]/span[{index}]').text != "":
        word = driver.find_element(By.XPATH, f'//*[@id="row1"]/span[{index}]').text
        for i in word:
            keyboard.press(i)
            keyboard.release(i)
        keyboard.press('space')
        keyboard.release('space')
        index += 1
        print(word)
            # actions.send_keys(word + " ")
            # actions.perform()
            # text_list.append(word)
            # index+=1
        # else:
        #     break

    # print(text_list)

    # actions = ActionChains(driver)
    # for word in text_list:
    #     actions.send_keys(word + " ")
    #
    # actions.perform()


main()
