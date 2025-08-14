import  random

"""
编写程序：calc.py 要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”编写程序：calc.py 
要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”
"""
temp = input("please input a number between 1 and 100: ")
number = int(temp)

if 1 <= number <= 100:
    print("你妹好漂亮")
else:
    print("你大爷好丑")

"""如果非要在原始字符串结尾输入反斜杠，可以如何灵活处理？"""
print("This is a test sentence with \\")
c = r"this is a sentence with '\'"
d = r'C:\Program Files\FishC\Good''\\'
print(r"this is s sententce with '\'")
print(c)
print(d)

"""测试循环"""
#while 'c':
#    print("hello world") #一直
e = 10
while e:    # e>10跳出
    print(e)
    e-=1
print("you are out!")

