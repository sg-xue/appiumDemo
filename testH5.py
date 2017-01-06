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

class H5Test(unittest.TestCase):
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
        # sleep(2)
        search_box = self.driver.find_element_by_id("com.vivo.browser:id/edit")
        search_box.send_keys("m.dianhua.cn/detail/97ece2b6170a6a203ceee2ed9c707e55")
        sleep(3)
        self.driver.find_element_by_id("com.vivo.browser:id/go").click()
        sleep(5)
        print self.driver.contexts #[u'NATIVE_APP', u'WEBVIEW_com.vivo.browser']
        self.driver.switch_to.context("WEBVIEW_com.vivo.browser")
        print self.driver.context
        sleep(5)
        self.driver.find_element_by_id('js_tel_more').click()
        sleep(3)
        self.driver.switch_to.context("NATIVE_APP")
        # search_box.send_keys("luna.58.com/m/bj/zufang.shtml?utm_source=link&spm=s-25339240070662-ms-f-dianhuabang.mzf_zufang&-15=20")
        # sleep(1)
        # self.driver.find_element_by_id("com.vivo.browser:id/go").click()
        # sleep(3)

        # self.driver.find_elements_by_class_name("android.view.View")[1].send_keys("hello")
        # self.driver.find_element_by_android_uiautomator('new UiSelector().description("土豪五居")').click()
        # sleep(3)
        # #输入号码和服务密码
        # num_text = self.driver.find_elements_by_class_name("android.widget.EditText")[0]
        # num_text.send_keys("18823834164")
        # num_text = self.driver.find_elements_by_class_name("android.widget.EditText")[1]
        # sleep(20)
        # num_text.send_keys("157350")
        # self.driver.find_element_by_class_name("android.widget.CheckBox").click()
        # self.driver.find_element_by_class_name("android.widget.Button").click()
        # sleep(8)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(H5Test)
    unittest.TextTestRunner(verbosity=2).run(suite)