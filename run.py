import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner


def allcase():
    test_dir = './adhoc/test/case'
    #test_dir = './adhoc/test/android-case'
    discover = unittest.defaultTestLoader.discover(start_dir='./adhoc/test/case', pattern="test*.py")
    #discover = unittest.defaultTestLoader.discover(start_dir='./adhoc/test/android-case', pattern="test*.py")
    testcase = unittest.TestSuite()
    #discover方法筛选出来的用例，循环添加到测试套件中
    #print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            print(test_case)
            testcase.addTest(test_case)
    return testcase



if __name__ == "__main__":
    report_dir = './report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="H5Editor兼容性测试结果")
        runner.run(allcase())
