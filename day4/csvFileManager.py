#1.要想读取CSV，首先要导入CSV代码库
#这个CSV也不用下载，是Python内置的代码库
#如果要读取Excel需要下载相应的代码库:xlrd
#怎么下载：1.通过命令下载：在DOS窗口中，输入pip -install -U xlrd
#之前发了一个selenium的离线包，也可以通过命令行在线安装：
#pip -install -U xlrd或者pip3 install selenium
#-U是升级到最新版的意思
#pip是Python语言最常用的项目管理工具，和Java中的maven类似
#如果你又安装了Python2，同是安装Python3，那么可能把pip改成pip3
#2.点击File-》点击setting->project-》project下面的interpreter->+
#搜索需要的代码库，并可直接安装


import csv

#指定要读取文件的路径

#path = 'C:\\Users\\51Testing\\PycharmProjects\\selenium7th\\data\\testdata.csv'
path = 'C:/Users/51Testing/PycharmProjects/selenium7th/data/testdata.csv'

#因为字符串中包含发斜线\t等，那么怎么办？
#1.每个反斜线前面加一个反斜线
#2.把每一个反斜线都改成正斜线
#相比，第二种方法更好一点，因为Java和Python都是跨平台语言
#在字符串中两个反斜线会自动根据转义字符转成一个反斜线
#在Windows操作系统中，用反斜线表示目录结构
#但是在Linux操作系统中，只有正斜线/才能表示目录
#如果用双反斜线，那么代码就失去了跨平台的能力，因为Linux用不了\
#如果用正斜线，代码可以同时在Linux和Windows中执行
#3.在字符串外面加一个字母r,认为中间所有的代码都不存在转义字符

print(path)
#3.打开路径所对应的文件
file = open(path,"r")

#4.读取文件的内容，通过什么来读取？
#我们是不是导入了CSV代码库，还一直没有
#reader（）方法时专门用来读取文件的
data_table = csv.reader(file)

#5.打印data_table中的每一行数据
#for是循环关键字，item代表每一行，每循环一次，就代表item里的最新数据

for item in data_table:
    print(item)
#我们是不是这样，就成功从excel中读取出所有的数据了
#很多的测试用例可能都需要从Excel中读取数据，所以我们应该对这些代码做一个简单的封装
#建一个文件叫CSVFileManager2,把以上的代码封装到一个方法中
#并且再建一个文件来读取封装好的方法