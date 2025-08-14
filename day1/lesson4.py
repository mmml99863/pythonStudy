"""分支和循环"""
from turtledemo.penrose import makeshapes

"""分支案例：根据用户输入的成绩划分等级"""
def func1():
    score = int(input("please input your score: "))
    if score == 100:
        print("score is 100")
    elif score >= 90:
        print("you score is greater than 90")
    elif score >= 80:
        print("you score is greater than 80")
    elif score >= 70:
        print("you score is greater than 70")
    elif score >= 60:
        print("you score is greater than 60")
    else:
        print("you score is smaller than 60")

"""分支案例：条件成立时执行的语句 if condition else 条件不成立时执行的语句 """
def func2():
    return  "hello" if 2 < 3 else "hello"   # hello

"""分支案例：赋值"""
def func3():
    a = 3
    b = 5
    small =  a if a<b else b
    return small

"""分支案例：func1()改写"""
def re_func1():
    score = int(input("please input your score: "))
    return 'A' if score >= 90 else\
            'B' if score >= 80 else\
            'C' if score >= 70 else \
            'D' if score >= 60 else 'F'

"""分支案例：分支结构嵌套"""
def func4(age, isMale):
    sex = 'male'
    limit = 18
    flag = False
    if age >= limit:
        if isMale == sex:
            flag = True
    if flag:
        print("you are allowed")
    else:
        print("you are not allowed")

"""循环结构案例：恋爱暗恋"""
def func5():
    is_love = "yes"
    while is_love == "yes":
        is_love = input("Do you love me today? ")
    print("you don't not love me today!")

"""循环案例：求和"""
def func6():
    i = 1
    asum = 0
    while  i < 100:
        asum += i
        i = i + 1
    print(asum)

"""循环案例：奇数跳过"""
def func7():
    i = 1
    while i < 20:
        if i % 2 == 0:
            print(f"{i} is even") # 输出偶数
        """
        else:
            continue    # continue语句会使得直接跳到while的条件判断进而死循环，break语句是当前的所属整个循环跳出
        """
        i += 1

"""循环案例：while和else"""
def func8():
    i = 1
    while i < 5:
        print("循环内", i)
        i+=1
    else:
        print("循环外")

"""循环案例：当循环案例不再为真时，else才会被执行"""
def func9():
    i = 1
    while i <= 7:   # 当连续输入7个“yes时，while循环跳出，执行else语句，否则不执行”
        ans = input("Did you study hard today?")
        if ans == "yes":
            print("good job!")
        else:
            print("bad guy!")
            break
        i += 1
    else:
        print("have a good rest!")

"""循环嵌套案例：乘法口诀表"""
def func10():
    i = 1
    while i <= 9:
        j = 9
        while j >= i:
            print(f"{i} * {j} = {i * j}", end=" ") #同行输出
            j -= 1
        print()# 换行输出
        i += 1
"""循环语句：for"""
def func11():
    for i in range(1, 10):
        print(i, end=" ")

def func12():
    i = 0
    str = "huang ji"
    while i < len(str):
        print(str[i], end="")
        i += 1

"""
range(stop)
range(start, stop)
range(start, stop, step)
"""
def re_func12():
    str = "huang ji"
    for i in range(0, len(str), 1):
        print(str[i], end="")

"""range()函数案例"""
def range_func():
    for i in range(10):
        print(i, end=" ")   #0 1 2 3 4 5 6 7 8 9
    print()
    for i in range(-1, 10):
        print(i, end=" ")   #-1 2 3 4 5 6 7 8 9
    print()
    for i in range(1, 10, 2):
        print(i, end=" ") # 1 3 5 7 9
    print()
    for i in range(10, 0, -2):  #10 8 6 4 2
        print(i, end=" ")
    print()

"""for循环案例：1-100求和"""
def re_func6():
    ans = 0
    for i in range(1, 101):
        ans += i
    print(ans)

"""for循环案例：找出10以内的素数"""
def func13():
    for i in range(2, 10):
        if i == 2:
            print(i, end=" ")
            continue
        flag = True
        for j in range(2, i):
            if i%j != 0:
                continue
            else:
                flag = False
                break
        if flag:
            print(i, end=" ")

def main():
    func13()
    func1()
    print(func2())
    print(func3())
    print(re_func1())
    func4(18, "male")
    func5()
    func6()
    func7()
    func8()
    func9()
    func10()
    func11()
    func12()
    re_func12()
    range_func()
    re_func6()

if __name__ == "__main__":
    main()