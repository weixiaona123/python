import unittest  # 单元测试模块
import time
from selenium import webdriver  # 引入浏览器驱动

from adhoc.test.page.h5editor_page import H5Editor
from utils.config import Config, DRIVER_PATH  # 引入配置
from adhoc.test.page.h5editor_page import H5Editor


class TestDLJ_firefox(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        print("开始测试")
        self.page = H5Editor(browser_type='firefox').get(self.URL, maximize_window=False)


    def tearDown(self):
        self.page.quit()

    def test_click_0(self):
        print("进入页面点击")
        H5Editor(self.page).test_click()  # 页面跳转到result page
        print("点击结束")

if __name__ == '__main__':
    unittest.main()

