# /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

import re
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )

class WhiteListTime(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '69DDU16519013381'
        desired_caps['appPackage'] = 'com.yulore.framework'
        desired_caps['appActivity'] = 'superyellowpage.yulore.com.frameworktest.FrameworkTestActivity'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_whiteList(self):
        testDataList = []
        testDataList = self.get_telNum()

        self.driver.find_element_by_id("identify_single").click()
        sleep(1)

        for num in range(len(testDataList)):

            number_text = self.driver.find_element_by_id("input_number")
            number_text.click()
            self.driver.keyevent(123)
            for i in range(0, len(number_text.text)):
                self.driver.keyevent(67)
            sleep(1)
            tel = re.search(r'.+?\s(.+)', testDataList[num]).group(1)
            number_text.send_keys(tel.strip())
            sleep(3)
            self.driver.find_element_by_id("query").click()
            # sleep(1)
            # query_content = self.driver.find_element_by_id('query_content').text.encode('utf-8')
            # sleep(1)
            # patten = re.compile(r'名称：(.+)位置', re.DOTALL)
            # company_name = patten.search(query_content).group(1).strip().decode('utf-8')
            # print company_name
            #assert name is correct
            # real_company_name = re.search(r'(.+?)\s\w+', testDataList[num]).group(1)
            # self.assertEqual(company_name, real_company_name)
            # sleep(1)

    def get_telNum(self):
        # telNumList = []
        # lineNum = 0
        # with open('whitelist-100w.txt', 'rw+') as wlist:
        #     for line in range(0, len(wlist.readlines())):
        #         lineNum += 1
        #         if (lineNum % 10000 == 0):
        #             wlist.seek(lineNum, 1)
        #             whiteList = wlist.readline()
        #             telNumList.append(whiteList.decode('utf-8'))
        # print telNumList
        # return telNumList
        telNumList = []
        lineNum = 0
        with open('whitelist-100w.txt', 'rw+') as wlist:
            content = wlist.readlines()
            while lineNum < len(content):
                if (lineNum % 10000 == 0):
                    whiteList = content[lineNum]
                    # print "%s the content is: %s" % (lineNum, whiteList)
                    telNumList.append(whiteList.decode('utf-8'))
                lineNum += 1
        return telNumList


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WhiteListTime)
    unittest.TextTestRunner(verbosity=2).run(suite)