'''
使用类属性方式创建property属性，
新式类与标准类无区别
'''
class Goods:

    def get_price(self):
        print("call get_price method")
        return 100

    price = property(get_price)


obj = Goods()
print(obj.price)

# 使用 property方法创建的类属性会自动调用 get_price 方法