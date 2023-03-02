''''
使用property升级getter和setter
'''


class Goods(object):
    def __init__(self):
        self._money = 10

    # 使用property装饰器获取私有属性,会自动添加一个叫money的属性，当获取money的值时，会自动调用装饰的方法
    @property
    def money(self):
        return self._money

    # 使用property设置私有属性
    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self._money = value
        else:
            print("error, 不是整型数字")

# 实例化对象
good = Goods()
# 获取私有属性， @property
print(good.money)
# 设置私有属性， @property.setter
good.money = 100
print(good.money)