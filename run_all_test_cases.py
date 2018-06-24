#这个文件是用来批量执行unittest的测试用例
#该文件是我们这个测试工具的唯一入口
#1.导入unitest
import smtplib
import  unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner

def send_mail(path):
    #1.通过path打开新生成的测试报告文件
    #html格式不是文本格式，需要指定以二进制的方式打开
    open(path,'rb')
    #2.读取文件的内容，作为邮件正文
    file = open(path,'rb')
    msg = file.read()
    #3.把读取出来的内容转换成MIMEText的格式
    #电子邮件类型一般分三种，分别是纯文本plain,html,富文本
    mime = MIMEText(msg, _subtype='html', _charset='utf-8')
    #4.除了正文以外，还需要设置主题，发件人，收件人
    mime['Subject']='姚楠测试报告'
    #发件人'bwftest126@126.com', 'abc123asd654'
    #因为发件人需要登录密码，这里的密码是登录端授权码
    #第三方登录不能直接用密码，必须用授权码
    mime['From']='bwftest126@126.com'
    mime['To']= 'yaonan9@126.com'

    #5.实现SMTP（）构造方法
    smtp = smtplib.SMTP()
    #
    smtp.connect("smtp.126.com")
    #登录邮箱和发邮件必须是同一个
    smtp.login("bwftest126@126.com",'abc123asd654')
    #

    smtp.send_message(mime, from_addr='bwftest126@126.com', to_addrs='yaonan9@126.com')
    #退出
    smtp.quit()
    #2.通过传输协议发送邮件

if __name__ == '__main__':
    #2.要想批量执行，首先要明确你要执行那些测试用例
    #只能执行继承了unitest.TestCase的类
    #比如执行这个项目中所有的unittest的测试用例
    #defaultTestLoader 是默认的测试用例的加载器，可以用来发现所有的测试用例
    #*表示统配符，可以代替任何字符
    #*Test.py表示以Test.py结尾的所有文件
    #.表示当前路径，即项目的根路径
    #suit随便起的变量名，suit本身是测试用例集的意思
    suit = unittest.defaultTestLoader.discover('./day5', pattern='*Test2.py')
    #当前项目下的所有测试用例
    #suit = unittest.defaultTestLoader.discover('.', pattern='*.py')

    #3.找到测试用例，执行这些测试用例
    #TextTestRunner()文本的测试用例的运行器
    #unittest.TextTestRunner().run(suit)
    #4.生成测试报告
    #HTMLTestRunner类似于TextTestRunner，都是批量执行测试用例的
    #区别在于，他们执行完测试用例的输出结果，
    # 一个是Text,另一个是HTML
    #Text会被打印到控制台中，HTML会单独生成一个文件
    #相比于Text，HTML结构更清晰
    #所以两者选其一，用HTMLTestRunner代替unittest原生的测试用例运行器TextTestRunner

   # HTMLTestRunner().run(suit)代替unittest.TextTestRunner().run(suit)
    #需要指定报告生成的路径
    #在项目根节点下创建一个文件夹，叫report
    # 5.定义测试报告的保存目录
    base_path = os.path.dirname(__file__)
    path = base_path +'/report/test_report.html'
    #创建测试文件
    file = open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description="测试环境：Server 2008;浏览器：’Chrome'").run(suit)
    #7.把测试报告做为邮件发送，好处是，可以起到及时提醒的作用
    #前提条件准备，准备两个邮箱，
    #版本控制的前提条件，申请一个git账号，并且用邮箱激活
    #把HTML格式的测试报告，作为邮件正文发送

    send_mail(path)
