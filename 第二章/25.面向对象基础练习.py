"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车
"""
class Shopping:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"

    def update_shop(self, price=None, num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num
class ShoppingCar:
    def __init__(self):
        self.shopping_list = []

    def add_shopping(self):
        name = input("请输入商品名称: ")
        for s in self.shopping_list:
            if s.name == name:
                print("商品已存在")
                return
        price = float(input("请输入商品价格: "))
        num = int(input("请输入商品数量: "))
        i = Shopping(name, price, num)
        self.shopping_list.append(i)
        print("添加成功")
    def update_shopping(self):
        name = input("请输入要修改的商品名称: ")
        for s in self.shopping_list:
            if s.name == name:
                price = float(input("请输入商品价格: "))
                num = int(input("请输入商品数量: "))
                s.update_shop(price, num)
                print("修改成功")
                return
        print("商品不存在")
    def delete_shopping(self):
        name = input("请输入要删除的商品名称: ")
        for s in self.shopping_list:
            if s.name == name:
                self.shopping_list.remove(s)
                print("删除成功")
                return
        print("商品不存在")
    def showing_shopping(self):
        for s in self.shopping_list:
            print(s)

    def run(self):
        print(f"欢迎使用购物车管理系统")

        while True:
            print()
            print("# " * 35)
            print("#       1.添加商品  2.修改商品  3.删除商品  4.查询购物车  5.退出系统        #")
            print("# " * 35)
            print()

            choice = input("请选择要执行的操作，输入1-5: ")
            match choice:
                case "1":
                    self.add_shopping()
                case "2":
                    self.update_shopping()
                case "3":
                    self.delete_shopping()
                case "4":
                    self.showing_shopping()
                case "5":
                    print("退出系统")
                    break
                case _:
                    print("无效的选择，请重新输入")

if __name__ == "__main__":
    shopping_car = ShoppingCar()
    shopping_car.run()
