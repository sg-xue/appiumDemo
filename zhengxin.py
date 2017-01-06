# /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from PIL import Image

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )

class InfoInputTest(unittest.TestCase):
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
        desired_caps['appPackage'] = 'com.vivo.browser'
        desired_caps['appActivity'] = '.MainActivity'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_open_webpage(self):

        #打开浏览器输入网址
        search_box_init = self.driver.find_element_by_id("com.vivo.browser:id/search_text").click()
        sleep(2)
        search_box = self.driver.find_element_by_id("com.vivo.browser:id/edit")
        search_box.send_keys("crs-ui.dianhua.dev")
        self.driver.find_element_by_id("com.vivo.browser:id/go").click()
        sleep(3)

        #输入号码和服务密码
        num_text = self.driver.find_elements_by_class_name("android.widget.EditText")[0]
        num_text.send_keys("18823834164")
        num_text = self.driver.find_elements_by_class_name("android.widget.EditText")[1]
        sleep(20)
        num_text.send_keys("157350")
        self.driver.find_element_by_class_name("android.widget.CheckBox").click()
        self.driver.find_element_by_class_name("android.widget.Button").click()
        sleep(8)

    # def add_contacts(self):

    #
    #     textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
    #     textfields[0].send_keys("appium user")
    #     print textfields[0].get_attribute("name")
    #     self.assertEqual('appium user', textfields[0].get_attribute("name"))
    #
    #     # self.driver.find_element_by_name("Save").click()
    #     #
    #     # # for some reason "save" breaks things
    #     # alert = self.driver.switch_to_alert()
    #     #
    #     # # no way to handle alerts in Android
    #     # self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()
    #
    #     # self.driver.keyevent(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InfoInputTest)
    unittest.TextTestRunner(verbosity=2).run(suite)