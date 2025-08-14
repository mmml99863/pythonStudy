"""写一个程序，判断给定年份是否为闰年。"""
import  random as rd

'''闰年判断'''
def leap_year():
    year = input("please input your dream year:")
    year = int(year)
    if year%4==0 and year%100!=0 or year%400==0:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

'''猜数游戏'''
def rand_number():
    ans = rd.randint(1, 10)
    print(ans)
    return ans

def input_guess():
    guess = int(input("please input your guess between 1 and 10:"))
    return guess

def guess_number3(number, ans):
    times = 1 # 第一次猜测
    flag = False

    while times <= 3:
        if number == ans:  # 猜对
            flag = True
            break
        else:  # 猜错
            if number > ans:
                print("your guess is too high")
            else:
                print("your guess is too low")
            if times < 3:  # 还有机会才让用户输入
                number = input_guess()
        times += 1

    if flag:
        print("you guessed correctly!")
    else:
        print("you guessed incorrectly and your times are over 3!")

def func_set():
    leap_year()
    ans = rand_number()
    temp = input_guess()
    guess_number3(temp, ans)

'''从1输出到指定数值'''
def func1():
    temp = input("please input your number:")
    temp = int(temp)
    i = 1
    while temp:
        print(i)
        i += 1
        temp -= 1

def func2():
    temp = input("please input your number:")
    num = int(temp)
    while num:
        i = num - 1
        while i:
            print('', end='')
            i -= 1
        j = num
        while j:
            print('*', end=' ')
            j -= 1
        print()
        num -= 1

def main():
    func1()
    func2()
    func_set()

if __name__ == "__main__":
    main()