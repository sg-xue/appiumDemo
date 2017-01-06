# /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from PIL import Image
import re

class getCodeFromSMSTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '79c1e852'
        # desired_caps['app'] = PATH(
        #     '../../../sample-code/apps/ContactManager/ContactManager.apk'
        # )
        # desired_caps['appPackage'] = 'com.android.contacts'
        # desired_caps['appActivity'] = '.DialtactsContactsEntryActivity'
        desired_caps['appPackage'] = 'com.android.mms'
        desired_caps['appActivity'] = '.ui.ConversationList'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_identifyingCode(self):

        sleep(1)
        self.driver.find_element_by_id("com.android.mms:id/from").click()
        sleep(1)
        # self.driver.find_elements_by_id("com.android.mms:id/conversation_list_item")[0].click()
        # sleep(3)
        sms_conten = self.driver.find_element_by_id("com.android.mms:id/text_view").get_attribute("text")
        print sms_conten

        verification_code = re.search(r'(\d+)', sms_conten).group(0)
        print verification_code
        return verification_code


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(getCodeFromSMSTest)
    unittest.TextTestRunner(verbosity=2).run(suite)