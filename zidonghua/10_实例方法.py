
#self
class Test():

    #实例方法
    def hello(self):
        print("public")

    def __world(self):
        print("private")

    def test1(self):
        self.hello()

    def test2(self):
        self.__world()

test = Test()
test.test1()

test.hello()

test.test2()
