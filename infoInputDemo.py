# /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class InfoInputTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.1'
        desired_caps['deviceName'] = '79c1e852'
        # desired_caps['app'] = PATH(
        #     '../../../sample-code/apps/ContactManager/ContactManager.apk'
        # )
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.TwelveKeyDialer'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        el = self.driver.find_elements_by_class_name("android.widget.LinearLayout")[3]
        el.click()
        sleep(3)


        for m in range(3):
            size = self.driver.get_window_size()
            starty = int(size["height"] * 0.80)
            endy = int(size["height"] * 0.20)
            startx = int(size["width"] / 2)
            # Swipe from bottom to top
            self.driver.swipe(startx, starty, startx, endy, 1000)
        sleep(1)

        self.driver.tap([(300,1850)])
        sleep(3)

        size = self.driver.get_window_size()
        starty = int(size["height"] * 0.90)
        endy = int(size["height"] * 0.10)
        startx = int(size["width"] / 2)
        # Swipe from bottom to top
        self.driver.swipe(startx, starty, startx, endy, 1000)
        sleep(2)

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("appium user")
        print textfields[0].get_attribute("name")
        self.assertEqual('appium user', textfields[0].get_attribute("name"))

        # self.driver.find_element_by_name("Save").click()
        #
        # # for some reason "save" breaks things
        # alert = self.driver.switch_to_alert()
        #
        # # no way to handle alerts in Android
        # self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        # self.driver.keyevent(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InfoInputTest)
    unittest.TextTestRunner(verbosity=2).run(suite)