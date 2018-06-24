import csv

import os


class CsvFileManager4:

    def reader(self,filename):

        list = [] #声明一个空列表

       # path = r"C:\Users\51Testing\PycharmProjects\selenium7th\data\testdata.csv"


        #更好的方法是：
        #os.path.dirname(__file__)这是一个固定写法，用来获取当前文件的目录结构
        #os操作系统，path路径，dirname目录名，__file__是Python内置的变量，表示当前文件
        base_path = os.path.dirname(__file__)
        print(base_path)
        #用base_path的好处，不管项目方在任何路径下面，都可以找到文件的绝对路径
        path = base_path.replace('day5','data/'+ filename)
        print(path)

        #3.打开指定文件
        #file = open(path,'r')
        #每次打开文件，用完之后要记得关闭该文件，释放系统资源
        #我们上节课用的是try ...finally的方法
        #更常用的方式是with ...as的语法结构
        with open(path,'r')as file:
            date_table = csv.reader(file)
            for row in date_table:
                #循环遍历数据表中的每一行
                print(row)
#       打印出来不是我们的目的，我们的测试用例需要调用这些数据
#       所以，要给这个方法设一个返回值，把数据提取出来
#       5.声明一个二维列表，保存data_table中的所有数据
                list.append(row)
            #在read方法末尾，返回这个列表  # # return list
        return list
        print(list)






if __name__ == '__main__':
    list = CsvFileManager4().reader('testdata.csv')
    print(list[0][0])