


class WeChat():
    def pay_method(self):
        print("微信支付")



class Ali():
    def pay_method(self):
        print("支付宝支付")


class Card():
    def pay_method(self):
        print("银行卡支付")


class Pay():
    def pay(self,method):
        method.pay_method()


wechat = WeChat()
ali = Ali()
card = Card()
pay = Pay()

pay.pay(ali)
