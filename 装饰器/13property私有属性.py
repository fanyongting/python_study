class Goods(object):

    def __init__(self):
        self._money = 0

    # 获取私有属性
    def get_money(self):
        return self._money

    # 设置私有属性
    def set_money(self, value):
        # 防呆瓜
        if isinstance(value, int):
            self._money = value
        else:
            print("error, 设置的值不是整形数字")


# 实例化对象
good = Goods()
# 使用类方法获取私有属性
print(good.get_money())
# 使用类方法设置私有属性
good.set_money(100)
print(good.get_money())



