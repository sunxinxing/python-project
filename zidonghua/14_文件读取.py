
import xlrd
from xlrd import sheet
import yaml
from yaml import loader

#with open()自动打开及关闭文件

'''
#txt文件
with open("D:\datum\环境搭建.txt") as f:
    for i in f.readlines():
        i = i.strip("\n")
        data = i.split()
        print(data)


#excel

class ExcelData():

    data_path = "D:\datum\常用服务参数、指令配置说明.xlsx"

    #打开文件
    excel = xlrd.open_workbook(data_path)

    #找到指定sheet
    sheet = excel.sheet_by_index(0)

    rows, cols = sheet.nrows, sheet.ncols

    print(rows, cols)

    def read_excel(self):

        first_row = self.sheet.row_values(0)
        print(first_row)   


        #定义空列表存放数据
        self.result = []
        for i in range(1, self.rows):
            #定义空字典存放字典数据
            data = {}
            for j in range(0, self.cols):
                data[first_row[j]] = self.sheet.row_values(i)[j]

            self.result.append(data)
            print(self.result)

                

'''

#yaml文件

path = "D:\\datum\\python\\python project\\python project\\zidonghua\\test.yaml"

#获取对象进行操作
result = open(path, encoding="utf8").read()


file_dict = yaml.load(result, Loader=yaml.FullLoader)

print(file_dict)




# e = ExcelData()
# e.read_excel()