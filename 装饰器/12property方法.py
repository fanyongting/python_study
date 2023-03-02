'''
property 方法有四个参数
1. 方法名， 调用对象.属性时会自动触发执行方法
2. 方法名， 调用对象.属性 = xxx时自动触发执行方法
3. 方法名， 调用del 对象.属性 时自动触发执行方法
4. 字符串， 调用 对象.属性.__doc__ 此参数是该属性的描述信息
'''

class Goods(object):

    # 获取类属性
    def get_price(self):
        print("get_price")
        return 'a.....'
    # 设置类属性
    def set_price(self, value):
        print("setter", value)
        return "set value" + value
    # 修改类属性
    def del_price(self):
        print("deleter price")
        return "del_price"

    BAR = property(get_price, set_price, del_price, "description")

#
good = Goods()
# print(good.BAR)
# good.BAR = '110'
# print(Goods.BAR.__doc__)
# del good.BAR
#
print(type(good.BAR))
