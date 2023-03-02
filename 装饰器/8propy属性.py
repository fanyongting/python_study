class test:
    def Foo(self):
        print("call pbj")

    @property
    def prop(self):
        print("call property method")


# pbj = test()
# pbj.Foo()
# pbj.prop

class Goods:
    @property
    def money(self):
        return 100


# good = Goods()
# print(good.money)

class Pager:
# 实现分页的设计
# 返回分页数据，开始 start，结束 end

    def __init__(self, current_page):
        self.current_page = current_page # 默认的页数
        self.per_item = 10 # 默认每页的重量

    @property
    def start(self):
        val = (self.current_page-1) * self.per_item
        return val

    @property
    def end(self):
        val = self.current_page * self.per_item
        return val

# 实例化一个对象
p = Pager(2)
print(p.start)
print(p.end)

