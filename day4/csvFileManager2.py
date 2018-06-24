import csv

class csvFileManager2:
    @classmethod
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\testdata.csv'
        file = open(path,'r')
        #通过csv代码库，读取打开的CSV文件，获取到文件中所有的数据
        date_able =csv.reader(file)
         #for 循环 item每一行 in在数据集中 data_table表示数据集
            #data_able有几行数据我们就会执行几次
        for item in date_able:
             print(item)

#如果想在测试一下这个方法
if __name__ == '__main__':
    #csvr = csvFileManager2()
   # csvr.read()

#如果在方法上面加一个classmethod,表示这个方法可以直接用类调用
#如果在方法上写一个classmethod，就不需要先实例化对象了
    csvFileManager2.read()