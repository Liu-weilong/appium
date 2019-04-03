#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/1 15:43
#@Author: liuweilong
#@File  : appium-basis.py



#app自动化测试知识点
#自动化的流程与分类
#流程：需求分析 方案选择 环境准备 系统设计 编码
#分类：分层测试
#安卓：是基于Linux的自由和开放代码的操作系统
#app三种类型与区别
#原生应用程序  混合应用程序  web版app
#安卓sdk  UIautomator是一个做app的UI自动化测试框架


#adb命令  是一种通用命令行工具
#工作原理：启动一个adb客户端时此客户端首先检查是否有已运行的adb服务进程 没有的话启动服务进程 启动时与本地tcp端口5037
#绑定 并侦听从adb客户端发送的命令   所有的adb客户端都使用端口5037与adb服务器通信
#adb常用命令
#adb version 查看版本号
#adb connect 127.0.0.1:62001 链接模拟器   62025
#adb devices 查看链接设备
#adb shell 查看系统中的目录
#adb install 文件名  安装程序
#adb uninstall 文件名  卸载程序
#adb shell pm list package 查看设备上安装的应用包名
#adb start-server 开启adb服务
#adb kill-server 关闭adb服务
#adb reboot 重启android设备
#adb pull <设备中的文件路径> <本地路径>:从模拟器或设备中复制文件到本地。
#adb push <本地文件路径> <设备中的路径>:将本地文件或目录复制到模拟器或设备。
#adb logcat 查看日志

#package包  是APP中唯一的对什么程序做自动化  就得知道他的包名
#activity  是程序的根本 所有程序流程都运行在activity之中 是安卓最基本的模块

#monkey简介
# 进入monkey
# adb shell
# cd /system/bin
# monkey

#monkey常用命令
# 强制关闭monkey
# adb shell ps 查看全部在运行的进程
# 找出com.android.commands.monkey 进程pid
# adb shell kill pid  杀掉monkey进程

#monkey事件
#触摸事件
#手势事件
#二指缩放事件
#轨迹事件
#屏幕旋转事件
#基本导航事件
#主要导航事件
#系统按键事件
#启动activity事件
#键盘事件
#其他类型事件

#monkey参数
#adb shell monkey -h 帮助信息
#adb shell monkey -v 200 打印执行200个日志信息
#adb shell monkey -f 脚本名称  执行指定脚本
#adb shell monkey -s 随机执行

#adb shell monkey --pct-touch 100 200 触摸事件百分比
#adb shell monkey --pct-motion 手势事件百分比
#adb shell monkey --pct-trackball 轨迹球事件百分比
#adb shell mnonkey --pct-nav 基本导航事件百分比
#adb shell monkey --pct-majornav 主要导航事件百分比
#adb shell monkey --pct-syskeys 系统按键事件百分比
#adb shell monekey --pct-appswitch 应用启动事件百分比
#adb shell  monkey --pct-rotation 横竖屏切换事件百分比

#约束类参数
#包约束
#-p 后面接一个包名
#例子：adb shell monkey -p  包名（可以多个）  200 （在这个包内点击200次随机事件）
#activity约束
#例子：adb shell monkey -c
#adb shell monkey -p com.tal.kaoyan --pct-touch 40  --pct-motion 25 --pct-appswitch 10 --pct-rotation 5 -s 1666 --throttle 400 --ignore-crashes --ignore-timeouts -v -v 200

#monkey自定义脚本稳定式测试
#LaunchActivity(pkg_name,cl_name) 启动应用的activity  参数：包名和启动的avtivity
#Tap（x,y,tapDuration）模拟手机一次手指单机事件 参数：x，y为控件坐标  tapDuration:点击的持续时间
#UserWait（sleeptime）休眠一段时间
#DispatchPress(keyName)按键  参数：
#DispatchString(input)输入字符串
#DispatchFlip(true/false)打开或关闭软件盘
#PressAndHold(x,y,pressduration)模拟长按事件
#Drag(xStart,yStrat,xend,yend,stepcount)用于模拟一个拖拽操作
#PinchZoom(x1start,y1start,x1end,y1end,x2start,y2start,x2end,y2end,stepcount)模拟缩放手势
#LongPress()长按2秒
#DeviceWakeUp()唤醒屏幕
#

#monkey 自定义脚本
# type = raw events
# count = 1
# speed = 1.0
#
# start data >>
# LaunchActivity(com.spread,com.spread.MainActivity)
# UserWait(2000)
#
# Tap(114,556,1000)
# DispatchString(15256750385)
# UserWait(2000)
#
# Tap(99,641,1000)
# DispatchString(123456)
# UserWait(2000)
#
# Tap(339,809)
# UserWait(2000)
#adb push C:\Users\蜻蜓队长\Desktop\xlx.txt /sdcard  把脚本放在这个文件中
#adb shell monkey -f /sdcard/xlx.txt -v 1  执行这个脚本一次

#adb shell monkey -v 100 >d:/monkey.log  把日志存储在指定位置
#adb shell monkey -v -v 100 1>d:/stand.log 2>d:/error.log  把日志分为错误流和标准流放在指定文件中


#monkeyrunner知识点
#monkeyrunner  路径：Androidsdk/tools
#功能：
#多设备控制：api可以跨多个设备，一次启动全部模拟器来实现测试套件
#功能测试：为应用自动执行一次功能测试，然后观察输出结果的截屏
#可扩展自动化：因为monkeyrunner是一个API工具包 可以开发基于python模块的真个系统来控制Android设备

#monkeyrunner和monkey区别
#本身没有什么直接联系，monkey是在设备上直接运行adb shell命令生成随机事件来进行访问 monkeyrunner是通过API发送
#特定的命令和事件来控制设备

#monkeyrunner环境搭建
#安装并配置jdk环境
#安装Androidsdk
#安装python
#monkeyrenner环境变量配置：{path}\android_sdk\tools
#检查安装 控制台输入 monkeyrunner
#退出monkeyrunner命令行使用快捷键  ctrl+D


#monkeyrunner api
#主要有三个类
#MonkeyRunner
#MonkeyDevice
#MonkeyImage

#MonkeyRunner类
#提供了链接真机和模拟器 输入 暂停 警告框等方法
#alert()警告框
#choice()选项列表框
#help()api帮助文档
#input()输入
#sleep()暂停
#waitForConnection()等待设备连接
#常用方法waitForConnect(float timeout,string deviced)

#MonkeyDevice类
#提供了安装和卸载程序包 开启activity 并发送按键和点击事件 运行测试包等方法
#broadcastIntent()发送广播
#drag()拖动
#getProperty()获取当前设备属性
#getSystemProperty()获取当前设备属性
#installPackage()安装应用
#instrument()执行测试用例
#press()按键
#reboot()重启
#removePackage()删除指定安装包
#shell()执行命令
#startActivity()启动应用
#touch()点击
#常用方法
#installPackage(string path路径)
#removePackage(string package路径)
#startActivity(包名，Activity)
#touch(x integer,y integer type)type:DOWN按下 UP弹起 DOWN_AND_UP按下弹起

#MonkeyImage类
#convertToBytes()转换图像格式
#getRawPixel()获取当前坐标像素元祖
#getRawPixelInt()获取当前坐标像素值
#sameAs()图像对比
#writeToFile()保存图像文件
#getSublmage()截取子图像
#常用方法
#takeSnapshot()进行屏幕截图
#writeToFile()保存图像文件指定的文件路径


#Appium基础知识点
#Appium：是一个开源测试自动化框架 可用于原生 混合 移动web应用程序测试，它使用webDirver协议驱动ios android和windows应用程序
#优势：可以跨平台同时支持Android iOS   支持多语言python java PHP等  不用为复杂环境发愁 有selenium直接上手
#appium组件
#appium server就是appium的服务器一个web接口服务 使用node.js实现
#appium desktop是一款适用于mac windows和linux的开源应用程序
#appium Gui 是appium desktop的前身 这个也是把appium server封装成一个图形界面
#appium clients是一个客户端 （appium是一个c/s结构 ）它会给服务端appium server发送请求会话来执行自动化任务（就像浏览器访问网页）

#appium环境搭建
#环境一来 node.js  appium  appium-desktop appium-doctor appium-python-clients python  jdk android sdk
#安装流程在文本文档

#capability
#是配置appium会话 告诉appium服务器你想要的自动化的平台和应用程序
#desired capability 是一组设置的键值对的集合 其中键对应设置的名称 而值对应设置的值 如{'platformname':'android'}
#session appium的客户端和服务端之间进行通信都必须在一个session的上下文中进行 客户端在发起通信的时候首先会发送一个desried capability
#的json对象给服务器 服务器收到该数据后 会创建一个session并将session的id返回客户端 之后客户端可以用该session的id发送后续的命令
#这是官方文档 ：http://appium.io/docs/cn/writing-running-appium/caps/#android

#capability 启动app演示
#new session window 会话创建
#automatic server 本地appiumserver服务
#custom server：例如如果针对运行在网络中另一台计算机上的appium服务器启动inspector会话 这很有用
#sauce labs:如果你无法访问机器上的iOS模拟器 则可以利用sauce labs账户在云中启动appium会话
#testobject:可以利用testobject的真实设备云来进行真机测试
#headspin:使用远程设备来创建会话
#desired capability参数josin
# {
#     "platformName":"Android"
#     "platfromVersion":"5.1.1"
#     "deviceName":"127.0.0.1:62026"
#     "appPackage":"com.spread"
#     "appActivity":"com.spread.MainActivity"
#     "noReset":true
# }

#appium元素定位
#id
#name
#class
#list定位
#相对定位
#Xpath定位
#H5页面元素定位
#Uiautomator定位

#选中图片方法
# images = driver.find_elements_by_id('元素id')
# images[7].click()
#在点击保存按钮

#UIautomator元素定位
#id
#text
#calss name
#用 new UiSelector().resourceId()  id定位
#用 new Uiselector().className()   clasname定位
#用 new Uiselector().text('请输入姓名') text定位


#appium元素等待
#强制等待 使用sleep（）
#隐士等待 是针对全部元素设置的时间  driver.implicitly.wait()
#显式等待用到的库为：from selenium.webdriver.support.ui import WebDriverWait
#显式等待 是针对某个元素设置的时间  webDriverWait


#Toast元素识别  就是app错误提示
#配置参数desired_caps['automatorionName'] = 'uiautomator2'
#安装appium-uiautomator2-driver
#安装命令 cnpm install appium-uiautomator2-driver
#安装selenium  pip install selenium     web自动化已安装

#保存图片指定路径
#driver.get_screenshot_as_file('./images/long.png')


#Appium H5页面的定位知识点
#context:当前对象在程序中所处的一个环境，比如前面提到的app一个界面是属于activity类型也就是Android界面环境但是当访问
#内嵌的网页是属于另一个环境，两者处于不同的一个环境，所以UIautomator定位不到元素
#可以使用WebView
#WebView是Android系统提供能显示网页的系统控件 他是一个特殊的View同事他也是一个ViewGroup可以有很多的子View
#
#H5元素定位环境搭建
#下载谷歌浏览器手机版和电脑版  查看版本信息  下载chromdrive要相对应
#chromDriver版本与chrom版本对照表 npm.taobao.org/mirrors/chromedriver/(https://npm.taobao.org/mirrors/chromedriver/2.37/notes.txt)
#路径：C:\Users\蜻蜓队长\AppData\Roaming\npm\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win
#安装逍遥模拟器 比较稳定
#app Webview开启debug模式
#在电脑端chrome浏览器输入chrome://inspect/#devices 进入调试模式

#appium 滑动
#这是滑动操作
# def get_size():
#     x = driver.get_window_size()['width']
#     y = driver.get_window_size()['height']
#     return x,y
# l = get_size()
# print(l)
#
# def swipelft():
#     l = get_size()
#     x1 = int(l[0]*0.9)
#     y1 = int(l[1]*0.5)
#     x2 = int(l[0]*0.1)
#     driver.swipe(x1,y1,x2,y1,1000)
#
# for i in range(2):
#     swipelft()
#     driver.implicitly_wait(2)
#
# driver.find_element_by_id('点击立即体验')


#appium进阶
#appium常用参数
#参数   默认值    含义
#-u    null      链接物理设备的唯一设备标识符
#-a    0.0.0.0   监听的ip地址
#-p    4723      监听的端口
#-bp   4724       链接Android设备的端口号
#-g    null      将日志输出到指定文件
#--no-reset   false  session之间不可重置应用状态
#--session-override  FALSE  允许session被覆盖
#--app-activity  null  打开Android应用时 启动activity的名字
#--app  null  本地绝对路径或远程http URL所指向的一个安装包
#更多参数命令   appium -h













'''

Appium 自动化

'''
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

print('connect')
device = mr.waitForConnection()

print('install')
#device.installPackage(r'D:/360Downloads/kaoyanbang_3.3.6.242.apk')
package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
runCont = package + '/' + activity
print('launch')
device.startActivity(component = runCont)
mr.sleep(2)

print('Click on the')
device.touch(925,125,'DOWN_AND_UP')
mr.sleep(1)

print('login')
device.touch(984,1981,'DOWN_AND_UP')
mr.sleep(1)

print('login in')
device.touch(567,500,'DOWN_AND_UP')
mr.sleep(1)

print('input')
device.touch(214,724,'DOWN_AND_UP')
device.type('123456789')
mr.sleep(3)

print('long success')
device.touch(566,920,'DOWN_AND_UP')
mr.sleep(2)

print('click canale')
device.touch(174,1901,'DOWN_AND_UP')
mr.sleep(2)

print('The calendar')
device.touch(103,1957,'DOWN_AND_UP')
mr.sleep(2)

print('Colleges and universities')
device.touch(321,1973,'DOWN_AND_UP')
mr.sleep(2)

print('community')
device.touch(549,1974,'DOWN_AND_UP')
mr.sleep(2)

print('course')
device.touch(778,1975,'DOWN_AND_UP')
mr.sleep(2)

print('me')
device.touch(968,1987,'DOWN_AND_UP')
mr.sleep(2)

print('image')
device.touch(545,309,'DOWN_AND_UP')
mr.sleep(2)

print('back')
device.touch(77,175,'DOWN_AND_UP')
mr.sleep(1)

# print('members')
# device.touch(270,771,'DOWN_AND_UP')
# mr.sleep(3)
#
# print('back')
# device.touch(55,162,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('integral')
# device.touch(819,774,'DOWN_AND_UP')
# mr.sleep(1)
#
#
# print('back')
# device.touch(77,154,'DOWN_AND_UP')
# mr.sleep(1)

print('My post')
device.touch(310,925,'DOWN_AND_UP')
mr.sleep(1)


print('back')
device.touch(59,148,'DOWN_AND_UP')
mr.sleep(1)

print('Reply to remind')
device.touch(302,1061,'DOWN_AND_UP')
mr.sleep(1)

print('back')
device.touch(48,140,'DOWN_AND_UP')
mr.sleep(1)

print('My order')
device.touch(304,817,'DOWN_AND_UP')
mr.sleep(1)

print('back')
device.touch(48,140,'DOWN_AND_UP')
mr.sleep(1)

print('coupons')
device.touch(252,800,'DOWN_AND_UP')
mr.sleep(1)

print('back')
device.touch(85,160,'DOWN_AND_UP')
mr.sleep(1)

# print('I of course')
# device.touch(327,963,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('back')
# device.touch(43,141,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('My screen')
# device.touch(302,1091,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('back')
# device.touch(58,137,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('My profile')
# device.touch(265,1231,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('back')
# device.touch(50,137,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('Course cache')
# device.touch(297,1376,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('back')
# device.touch(40,150,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('My collection')
# device.touch(267,1524,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('back')
# device.touch(45,140,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('Message history')
# device.touch(265,1657,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('back')
# device.touch(31,132,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('help')
# device.touch(258,1812,'DOWN_AND_UP')
# mr.sleep(1)
#
# print('back')
# device.touch(50,146,'DOWN_AND_UP')
# mr.sleep(1)

print('Set up the')
device.touch(955,180,'DOWN_AND_UP')
mr.sleep(1)

print('logout')
device.touch(568,1655,'DOWN_AND_UP')
mr.sleep(1)

device.touch(317,1156,'DOWN_AND_UP')