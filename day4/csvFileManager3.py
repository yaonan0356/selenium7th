import csv
#每个测试用例对应着不同的csv文件
#每条测试用例都会打开一个CSV文件，所以每次也应该关闭该文件

class csvFileManager3:
    @classmethod
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\testdata.csv'
        file = open(path,'r')
        try:
        #通过csv代码库，读取打开的CSV文件，获取到文件中所有的数据
            date_able = csv.reader(file)
            a = [2,3,4,5,6]
            a[6]
         #for 循环 item每一行 in在数据集中 data_table表示数据集
            #data_able有几行数据我们就会执行几次
        #如果保证，不论程序执行过程中是否报错，都能正常关闭打开的文件
        for item in date_able:
                print(item)
        #方法最后应该添加close方法

        finally:
            print("file.close()method is executed")
            file.close()
#如果想在测试一下这个方法
if __name__ == '__main__':
    #csvr = csvFileManager2()
   # csvr.read()

#如果在方法上面加一个classmethod,表示这个方法可以直接用类调用
#如果在方法上写一个classmethod，就不需要先实例化对象了
    csvFileManager3.read()