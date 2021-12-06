


class People():

    nation = "china"
    __mimi = "秘密"

    def cook(self):
        print("炒饭")

    def __secret(self):
        print("隐私")

    def test(self):
        print("调用秘密：", nan.__mimi)

    
class Man(People):
    
    #重写父方法
    # def cook(self):
    #     print("会满汉全席")
    
    #扩展父方法
    def cook(self):
        People.cook(self)
        print("还可以煮面")

nan = Man()
# print(nan.nation)
nan.cook()
