''''
类有两种，一种是经典类，一种是新式类
新式类继承Object，有三种property装饰器
property, method.setter, method.deleter
经典类只有一种property装饰器
'''

# -------经典类--------

class test:
    @property
    def price(self):
        return 100


# a = test()
# print(a.price)
# ------------end---------

# --------新式类---------

class test2(object):

    @property
    def price(self):
        print("@property")

    @price.setter
    def price(self, value):
        print("@price.setter")

    @price.deleter
    def price(self):
        print("@price.deleter")

# 实例化一个对象
a = test2()
print(a.price)
# 设置值
a.price = 123
print(a.price)
del a.price



