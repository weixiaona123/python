import time
from adhoc.test.common.page import Page
from adhoc.test.common.browser import Browser


class H5Editor(Page):

    def test_click(self):
        click_test = self.driver.find_element_by_id('js-test-editor').text
        print(click_test)
        self.save_screen_shot("screen_shot")
        # 点击
        self.driver.find_element_by_id("js-test-editor").click()
        #获得alert
        alert = self.driver.switch_to.alert
        # 添加等待时间
        time.sleep(2)
        '''获取警告对话框的内容'''
        print(alert.text)  # 打印警告对话框内容
        print("开始打印啊")
        # time.sleep(4)
        alert.accept()  # alert对话框属于警告对话框，我们这里只能接受弹窗
        '''添加等待时间'''
        # time.sleep(2)
