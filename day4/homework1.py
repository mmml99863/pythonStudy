def func1(data):
    if data:
        print("十进制->二进制：{0}->{1:#b}".format(data, data))
        print("十进制->八进制:{0}->{1:#o}".format(data, data))
        print("十进制->十六进制:{0}->{1:#x}".format(data, data))

"""最大返回值"""
def func2():
    print(max('I love FishC.com'))#v

"""淘气"""
def func3():
    name = input("请输入待查找的用户名：")
    score = [['迷途', 85],
             ['黑夜', 80],
             ['小布丁', 65],
             ['福禄娃娃', 95],
             ['怡静', 90]
            ]
    IsFind = False

    for each in score:
        if name in each:
            print(name + "的得分是:",each[1])
            IsFind = True
            break

    if IsFind == False:
        print("没有找到该用户")

"""忽略字符串求和"""
def func4(data):
    Asum = 0

    for item in data:
        if type(item) == int or type(item) == float:
            Asum += item
        else:
            continue
    return Asum



if __name__ == '__main__':
    # num = int(input("请输入一个十进制数:"))
    # func1(num)
    # func2()
    # func3()
    a = ['he', 1, 'hello', 3, 4, 3.5, 66]
    print(func4(a))
