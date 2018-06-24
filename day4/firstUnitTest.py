#第一个单元测试的demo
#1.要想用Unittest框架，首先要导包
#为什么selenium要安装或者解压，Unittest不需要？
#因为unittest比selenium更常用，几乎所有测试都要用unittest组织测试
#所以Python把unittest集成在Python SDK中了，不需要单独下载，只要安装Python就有，unittest是Python内置的代码库

import unittest

#2.创建一个类，用来编写自动化测试用例，这个类需要继承unittest框架中的TestCase类
#我们继承了testcase这个类，就说明我们这个类是一个测试用例类
#Python中的类名最好和文件名不一样，文件名首字母小写，类名首字母大写
#类名和文件名不强制要求，可以一样，可以不一样
#（）小括号表示继承，继承子类完全继承父类的所有方法和属性，并且有自己扩展的内容
#unittest.TestCase是父类（基类），FirstUnitTest是子类（派生类）

class FirstUnitTest(unittest.TestCase):

#3.重写父类的setup和tearDown方法

    def setUp(self):

#Setup（）是在测试用例执行之前要做的操作
#类似手工测试的预置条件
#setup和teardown方法在每个测试用例方法执行时，都会执行一次
         print(1)
    def tearDown(self):
#           tearDown()是在测试用例方法执行之后要做的操作
#           比如可能需要还原测试场景，清除脏数据（比如注册产生的数据）
        print(2)       #前面要有8个空格
    def test_login(self):
#       这个方法用来编写测试步骤
#       框架规定：测试用例方法必须以test开头
#       只有以test开头的方法才会被当做测试用例，直接执行
        print(3)
    def switch_window(self):
#       窗口切换方法只是希望被调用才能执行
        print(4)
    def test_zhuce(self):
#       在Python中，类里面的每个方法，都有一个默认参数，叫self
#       self类似中Java中的this关键字，代表类本身
#       如果你想使用类的属性和方法，那么必须在前面加self关键字
#       现在打印的数字应该是什么
#       根据光标所在的位置，决定执行什么测试用例
#       光标在哪个方法中，那么就会只运行哪个测试用例
#       光标在unittest main（）这行就会执行所有的测试用例
        self.switch_window()
    #也可以选择重启setupclass和teardownclass方法
#   @classmethod在Python中叫装饰器，在Java中叫注解
#一个类中，所有测试用例方法的执行顺序，是根据方法名的字母顺序决定的

    @classmethod
    def setUpClass(cls):
        print(5)
    @classmethod
    def tearDownClass(cls):
        print(6)
    #写完之后，在unittest.main()位置运行一下
    #检查setupclass和setup方法有什么不同
    #classmethod只在类中所有方法前或方法后执行一次

# if __name__ == '__main__':这是一个固定的写法
#在程序运行时，通过这句话，可以自动判断当前文件是不是程序入口
#如果当前文件是程序的入口，那么就会执行if语句中的内容
if __name__ == '__main__':
     #unittest.main()可以理解为当前文件的主函数，会自动调用类中的所有测试用例方法
     unittest.main()
