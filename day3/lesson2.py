import math
import os

"""截取字符串"""
def func1():
    """去除指定空白"""
    x = "     左侧有空白        "
    print(x.lstrip())#"左侧有空白        "
    print(x.rstrip())#"     左侧有空白"
    #左右都不留白
    print(x.strip())#"左侧有空白"
    x = "12345"
    y =x.center(15," ")
    print(y)#~~~~~12345~~~~~
    """
    去除指定字符串
    lstrip()：从左侧开始做参数内的模式串，从匹配串开始删除原字符串的最大匹配串
    rstrip()：从右侧开始做参数内的模式串，从匹配串开始删除原字符串的最大匹配串
    strip()：从左/右开始做参数内的模式串，从匹配串开始分别删除左/右的最大连续匹配字符串
    """
    z = "abcdefg1234"
    print(z.lstrip("b134"))#abcdefg1234
    print(z.rstrip("b134"))#abcdefg12
    print(z.strip("a134"))#bcdefg12
    print(z.removeprefix("abce"))#abcdefg1234
    print(z.removeprefix("abcd"))#efg1234
    print(z.removesuffix("1234"))#abcdefg

"""拆分"""
def func2():
    """partition()是从左到右实现的分割,rpartition()是从右到左找到第一个分隔符时间分割"""
    x = "This is s sentence!"
    print(x.partition(" "))#('This', ' ', 'is s sentence!')
    print(x.rpartition(" "))#('This is s', ' ', 'sentence!')
    """
    split(str, maxSplit)从左到右分割maxSplit个数字的数组
    rsplit(str, maxSplit)从右到左分割maxSplit个数字的数组
    默认均是-1
    """
    print(x.split(" "))#['This', 'is', 's', 'sentence!']
    print(x.rsplit(" ", 2))#['This is', 's', 'sentence!']
    print(x.split(" ", 2))#['This', 'is', 's sentence!']
    y = "This\nis\na\nsentence!"
    print(y.split())#['This', 'is', 'a', 'sentence!']
    print(y.splitlines())#['This', 'is', 'a', 'sentence!']
    print(y.splitlines(True))#['This\n', 'is\n', 'a\n', 'sentence!']
    """
    字符串拼接
    """
    a = "."
    b = "world"
    print(a.join(b))#w.o.r.l.d
    c = ['ab', 'cd', 'ef']
    print(a.join(c))#ab.cd.ef
    print("".join(c))#abcdef

'''格式化字符串'''
def func3():
    year = 2025
    s1 = f"this is {year} year!"
    print(s1)
    s2 = "this is {} year!".format(year)
    print(s2)
    s3 = "1+2={}, square(2) is {}, square(3) is {}".format(1+2,math.floor(math.pow(2, 2)),math.floor(math.pow(3, 2)))
    print(s3)#1+2=3, square(2) is 4, square(3) is 9
    print("{0},{3},{1},{2}".format("张三","李四","王五","赵六"))#张三,赵六,李四,王五
    print("My name is {name}, I love {0}".format( "python", name="张三")) #注意，实义参数的数值要在位置后，My name is 张三, I love python
    """输出格式化{位置索引:(符号:)对齐方向:显示宽度}"""
    print("{1:>10}{0:<10}".format(250,520))#"       520250       "
    print("{:010}".format(250))#0000000250，只能对数字生效
    print("{0:010}".format(-250))#-000000250
    print("{:~>10}{:!<10}".format(250,520))#~~~~~~~250520!!!!!!!

"""符号使用format()"""
def func4():
    print("{:+} {:-}".format(10, -20))#+10 -20
    print("{:+} {:-}".format(10, 20))#+10 20注意，要正确识别正负号的作用
    """千分数符，不满3位则不可行"""
    print("{:,}".format(123456789))#123,456,789
    print("{:-,}".format(-123456))#-123,456
    """数位显示与截取"""
    print("{:.2f}".format(3.256))#3.26四舍五入
    print("{:-.2f}".format(-3.256))#-3.26四舍五入小数点后2位，不包含符号位
    print("{:.2g}".format(3.256))#3.3四舍五入2位
    print("{:-.2g}".format(-3.256))#-3.3四舍五入2位，不包含符号位
    print("{:.6}".format("This is a sentence"))#This i,此方法不能用于数字，只能用于字符串
    print("{:b}".format(80))#二进制：1010000
    print("{:c}".format(80))#Unicode:P
    print("{:d}".format(80))#十进制80
    print("{:o}".format(80))#八进制120
    print("{:x}".format(80))#十六进制50
    print("{:X}".format(80))#十六进制50
    print("{:#b}".format(80))#二进制0b1010000
    print("{:#o}".format(80))#十进制0o120
    print("{:#d}".format(80))#十进制80
    print("{:#x}".format(80))#十六进制0x50
    """科学计数法"""
    print("{:e}".format(3.1415))#默认精度6位3.141500e+00
    print("{:E}".format(3.1415))#3.141500E+00
    print("{:g}".format(123456789))#1.23457e+08大数则科学计数法，有损精确度
    print("{:g}".format(1234.56789))#1234.57小数则以定点小数输出
    print("{:%}".format(0.98))#默认精度6位98.000000%
    print("{:.2%}".format(0.98))#2位精度98.00%
    print("{:.{prec}%}".format(0.98, prec=2))#98.00%
    """综合使用"""
    print("{:{fill}{align}{width}.{prec}{ty}}".format(3.1415, fill="+", align="^", width=10, prec=3, ty="f"))#++3.142+++

    """f字符串"""
def func5():
    name = "python"
    a = f"我喜欢{name}"
    print(a)#我喜欢python
    """格式化字符串"""
    b = f"{-520:010}"#-000000520
    print(b)
    c = f"{123.456:~>10.2f}"
    print(c)#~~~~123.46
    #如果参数里有以斜杠 / 开头的绝对路径，那么它会丢弃前面的所有路径，从这个绝对路径重新拼接。
    pt = os.path.join("hello", "world","python","test.txt")#hello\world\python\test.txt
    print(pt)
    pt = os.path.join("/hello/", "world/","python/","test.txt")#/hello/world/python/test.txt
    print(pt)


if __name__ == '__main__':
    #func1()
    #func2()
    #func3()
    #func4()
    func5()