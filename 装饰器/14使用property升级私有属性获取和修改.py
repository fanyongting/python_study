'''
使用property升级私有属性的获取和修改
'''

class Goods(object):

    def __init__(self):
        self._money = 10

    # 获取私有属性
    def get_money(self):
        return self._money

    # 修改私有属性
    def set_money(self, value):
        # 防呆设计
        if isinstance(value, int):
            self._money = value
        else:
            print("error: 不是整形数字")

    money = property(get_money, set_money)

# 实例化一个对象
good = Goods()
# 获取私有属性， 会自动调用set_money
print(good.money)
# 设置私有属性，会自动调用get_money
good.money = 100
# 获取私有属性， 会自动调用set_money
print(good.money)