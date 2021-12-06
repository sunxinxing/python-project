
'''
class Test():

    name = "aa"
    __age = 20

    def run(self):
        print("run")
        print(Test.__age)

test = Test()
# print(test.name)
test.run()
# print(test.__age)

'''

class Phone():

    def __init__(self):
        self.model = "N78"
        self.__color = "白色"

    # def test1(self):
    #     print("调用公有属性：", self.model)

    def test2(self):
        print("调用私有属性：", phone.__color)

phone = Phone()
# phone.test1()
phone.test2()

# print(phone.model)


