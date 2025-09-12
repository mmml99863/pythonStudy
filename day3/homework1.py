
def ques1():
    a = "{{1}}".format("不打印", "打印") #{1}
    print(a)

def quest2():
    c = "Pi={:1.2f}".format(3.1415)
    print(c)#Pi=3.14

"""进制转换程序"""
def quest3(flag):
    while flag:
        x = int(input("Please input your number:"))
        print("十进制->二进制:{0} -> {1:#b}".format(x, x))
        print("十进制->八进制:{0} -> {1:#o}".format(x, x))
        print("十进制->八进制:{0} -> {1:#x}".format(x, x))
    print("Thank you!")



if __name__ == '__main__':
    ques1()
    quest2()
    quest3(True)