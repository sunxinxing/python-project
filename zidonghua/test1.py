from selenium import webdriver


'''
#位置传参
def Hello(name, age):
    print("名字是：", name)
    print("年龄是：", age)

hello("wawa", 19)
hello(19,"wawa")


#关键字传参（指定传参）
def Hello(name, age):
    print("名字是：", name)
    print("年龄是：", age)

hello(age = 19, name = "wawa")
hello("haha", age = 90)




#缺省传参（默认传参）

def Hello(name, age = 20):
    print("名字是：", name)
    print("年龄是：", age)

hello("wawa", 19)
hello("nini")



#位置不定长传参，结果封装为元组
def Hello(name, *other):
    print(name)
    print(other)

hello("koko", 18, "女")
hello("coco", 12, "男", "本科")
hello("ppopo")



#关键字不定长传参，结果封装为字典
def Hello(name, **other):
    print(name)
    print(other)

hello("koko", age = 18, sex = "女")
hello("coco", age = 12, sex = "男", bachelor = "本科")
hello("ppopo")

'''

#return

class compare():
    def get_ele(self):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com/")


        eles = driver.find_elements_by_xpath('//*[@id="s-top-left"]/a')
        eles_list = []
        for i in eles:
            eles_list.append(i.text)

        # print(eles_list)
        # return eles_list
    
ele = compare()
ele.get_ele()


# /html/body/div[1]/div[1]/div[3]/a[2]
# /html/body/div[1]/div[1]/div[3]/a
# //*[@id="s-top-left"]/a[1]
