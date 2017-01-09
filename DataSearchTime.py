# /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webelement import WebElement


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = '69DDU16519013381'
desired_caps['appPackage'] = 'com.yulore.framework'
desired_caps['appActivity'] = 'superyellowpage.yulore.com.frameworktest.FrameworkTestActivity'

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

testDataList = []
lineNum = 0
with open('whitelist-70w-6.txt', 'rw+') as wlist:
    content = wlist.readlines()
    while lineNum < len(content):
        if lineNum % 7000 == 0:
            whiteList = re.search(r'.+?\s(.+)', content[lineNum]).group(1)
            # print "%s the content is: %s" % (lineNum, whiteList)
            testDataList.append(whiteList.decode('utf-8'))
        lineNum += 1

driver.find_element_by_id("identify_single").click()
sleep(1)
number_text = driver.find_element_by_id("input_number")
numOfTel = len(testDataList)
action = TouchAction(driver)

for num in range(0, numOfTel):
    # tel = re.search(r'.+?\s(.+)', testDataList[num]).group(1)
    number_text.send_keys(testDataList[num].strip())
    sleep(1)
    driver.find_element_by_id("query").click()
    # number_text.click()
    action.long_press(number_text).wait(2000).perform()
    driver.keyevent(67)

driver.quit()
