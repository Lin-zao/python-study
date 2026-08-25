"""测试章节：基础断言示例。"""


def add(a, b):
    """返回两个数的和。"""
    return a + b


if __name__ == "__main__":
    assert add(1, 2) == 3
    print("测试通过")
