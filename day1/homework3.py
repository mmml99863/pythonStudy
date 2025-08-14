"""班级成绩判定"""
from ctypes.wintypes import PSMALL_RECT
from selectors import SelectSelector


def func1():
    score = int(input("please input your score: "))
    if 90 <= score <= 100:
        print('A')
    elif 80 <= score < 90:
        print('B')
    elif 70 <= score <80:
        print('C')
    elif 60 <= score < 70:
        print('D')
    elif 0 <= score < 60:
        print('F')
    else:
        print('your number is out of range')

"""三目运算符"""
def func2():
    a = 60
    b = 70
    c = 80
    small = a  if (a < b and a < c) else\
            b  if (b < a and b < c) else\
            c
    return small

"""循环打印次数"""
def func3():
    for i in range(0, 10, 2):
        print(i, end=' ') # 0 2 4 6 8
    print()

"""打印结果:2 3"""
def func4():
    while True:
        while True:
            break
            print(1)
        print(2, end=" ")
        break
    print(3)

"""水仙花数"""
def flower():
    for i in range(100, 1000):
        if i == pow( i%10, 3) + pow( int(i/10)%10, 3) + pow( int(i/100), 3):
            print(i, end=' ')
    print()

"""三色球:n*n"""
def colorful_ball():
    red = 3
    yellow = 3
    while red >= 0:
        while yellow >= 0:
            green = 8 - red - yellow
            while yellow >=0 and 0 <= green <= 6:
                print(f"red: {red}, yellow: {yellow}, green: {green}")
                yellow -= 1
                green += 1
        yellow = 3
        red -= 1

"""密码验证"""
def passwd_acc(ans):
    passwd = input("请输入您的密码:")
    counter  = 3

    while counter > 0:

        while "*" in passwd:
            passwd = input("密码中不能包含 *，请重新输入:")


        if passwd == ans:
            print("登录成功")
            return
        else:
            counter -= 1
            if counter > 0:
                passwd = input(f"密码错误,您还有{counter}次机会,请重新输入:")
            else:
                print("登录失败，密码输入次数超过3次")


"""三色球低效率:n*n*n"""
def re_colorful_ball():
    for red in range(0,4):
        for yellow in range(0,4):
            for green in range(0,7):
                if red  + yellow + green == 8:
                    print(f"red: {red}, yellow: {yellow}, green: {green}")

"""水仙花数2"""
def re_flower():
    for i in range(100,1000):
        asum = 0
        temp = i
        while temp:
            left = temp % 10
            temp = temp // 10
            asum += pow(left, 3)
        if asum == i:
            print(asum, end=' ')
    print()

def main():
    re_flower()
    """
    re_flower()
    re_colorful_ball()
    passwd_acc("hj9988")
    func1()
    print(func2())
    func3()
    func4()
    flower()
    colorful_ball()   
    """

if __name__ == '__main__':
    main()