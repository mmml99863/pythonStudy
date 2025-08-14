import random

"""字符串"""
print('I love \'python\'')  # 反译符号\

name = input("please input your name: ")
print("hello "+ name)

# 随机数游戏
a = random.randint(1,100) # 随机获取1-10的整数
temp = int(input("please input a number between 1 and 100: "))

while a != temp:
    if a > temp: # 如果随机生成的数大于输入的数
        print(f"the random number is greater than {temp}.")
        temp = int(input(f"please input a number between {temp} and 100 agin: "))
    else : # 如果随机生成的数小于输入的数
        print(f"the random number is smaller than {temp}.")
        temp = int(input(f"please input a number between 1 and {temp}: "))

print("you are right! see you next time!")
