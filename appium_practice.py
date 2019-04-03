#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/1 15:44
#@Author: liuweilong
#@File  : appium_practice.py


'''
这段代码是monkeyrunner安装程序启动起来

from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
print('connect')
device = mr.waitForConnection()
print('install ...')
device.installPackage(r'D:\360Downloads\zhifubao_138.apk')
print('launcha ...')
package = 'com.eg.android.AlipayGphone'
activity = 'com.eg.android.AlipayGphone.AlipayLogin'
compont = package + '/' + 'activity'
device.startActivity(component = compont )

'''


'''
这是根据monkeyrunner代码从程序的安装 输入 登录 截图保存的一段综合代码

from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from time import sleep
print('connect……')
device = mr.waitForConnection()
print('install....')
device.installPackage(r'D:\360Downloads\app-release(17).apk')
print('lunch...')
package = 'com.spread'
activity = 'com.spread.MainActivity'
compent = package  + '/' + activity
device.startActivity(component = compent)
sleep(2)
print('input username and password')
sleep(5)
device.touch(107,542,'DOWN_AND_UP')
sleep(2)
device.type('15256750385')
sleep(2)
device.touch(109,652,'DOWN_AND_UP')
sleep(2)
device.type('123456')
sleep(2)
device.touch(362,814,'DOWN_AND_UP')
sleep(5)
scrp = device.takeSnapshot()
scrp.writeToFile(r'D:\360Downloads\test.png','png')
'''


'''

from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from time import sleep
print('connect....')
device = mr.waitForConnection()
print('install....')
device.installPackage(r'D:\360Downloads\kaoyanbang_3.3.6.242.apk')
print('pinjie....')
package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
pont = package + '/' +  activity
device.startActivity(component = pont)
sleep(5)
print('success....')
device.touch(493,36,'DOWN_AND_UP')
print('registered....')
sleep(5)
device.touch(69,393,'DOWN_AND_UP')
sleep(5)
device.touch(92,238,'DOWN_AND_UP')
sleep(5)
device.type('测试数据')
sleep(5)
device.touch(91,283,'DOWN_AND_UP')
sleep(5)
device.type('123456789')
sleep(5)
device.touch(91,334,'DOWN_AND_UP')
sleep(5)
device.type('1711365301@qq.com')
sleep(5)
device.type(252,408,'DOWN_AND_UP')
print('registered success...')
'''




'''


'''
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['platforVersion'] = '7.1.2'

#这是真机
# desired_caps['deviceName'] = 'HUAWEI'
# desired_caps['platforVersion'] = '9'
# desired_caps['udid'] = 'LKX0217C03001636'

desired_caps['app'] = r'D:\360Downloads\kaoyanbang_3.3.6.242.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
desired_caps['noReset'] = 'True'
#中文配置
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)
def check_btn():
    print('check...')
    try:
        cont = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no cont')
    else:
        cont.click()
check_btn()







