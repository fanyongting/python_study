'''
新式类的属性有三种访问方法，
标准类的属性只有一种访问方法

'''
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.85
    # 第一种访问方法---获取
    @property
    def price(self):
        return self.original_price * self.discount

    # 第二种类属性的访问方法----修改
    @price.setter
    def price(self, value):
        self.original_price = value

    # 第三种类属性的访问方法---删除
    @price.deleter
    def price(self):
        del self.original_price

# 实例化一个对象
obj = Goods()
# 使用类属性的访问方法 --获取

print(obj.price)
# 使用类属性的访问方法 -- 修改
obj.price = 300
print(obj.price)
# 使用类属性的访问方法 -- 删除
del obj.price
# print(obj.price) 'Goods' object has no attribute 'original_price'
