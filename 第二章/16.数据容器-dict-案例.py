"""
    案例:
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
    具体功能如下：
        1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
        5. 退出购物车

    结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""
shopping_cart = {}
menu = """
########### 购物车系统 ##########
#         1. 添加购物车         #
#         2. 修改购物车         #
#         3. 删除购物车         #
#         4. 查询购物车         #
#         5. 退出购物车         #
###############################
"""
print("欢迎来到购物车管理系统")

while True:
    # 1,制作菜单
    print(menu)

    # 2.选择
    choice = input("请选择要执行的操作(1-5): ")
    match choice:
        case "1":
            goods_name = input("请输入商品的名称:")
            goods_price = float(input("请输入商品的价格:"))
            goods_num = int(input("请输入商品的数量:"))
            if goods_name not in shopping_cart:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("添加商品成功!")
            else:
                print("该商品已存在,请重新选择操作!")
        case "2":
            goods_name = input("请输入需要修改商品的名称:")
            goods_price = float(input("请输入需要修改商品的价格:"))
            goods_num = int(input("请输入需要修改商品的数量:"))
            if goods_name in shopping_cart:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("修改商品成功!")
            else:
                print("该商品不存在,请重新选择操作!")
        case "3":
            goods_name = input("请输入需要删除商品的名称:")
            if goods_name in shopping_cart:
                del shopping_cart[goods_name]
            else:
                print("该商品不存在,请重新选择操作!")
        case "4":
            for goods_name in shopping_cart.keys():
                goods_num = shopping_cart[goods_name]
                print("商品名称:", goods_name, "商品价格:", goods_num["price"], "商品数量:", goods_num["num"])
        case "5":
            print("再见----")
            break
        case _:
            print("输入操作有误,请重新选择操作")



