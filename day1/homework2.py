
"""打印1-100以内的奇数"""
def func1():
    for i in range(1, 101):
        if i%2 != 0:
            print(i, end=' ')

"""爱因斯坦步数"""
def func2():
    flag = True
    i = 7
    while flag:
        if (i%2 == 1) and (i%3 == 2) and (i % 5 == 4) and (i % 6 == 5) and (i % 7 == 0):
            print("the answer is :", i)
            flag = False
            break
        i+=7

