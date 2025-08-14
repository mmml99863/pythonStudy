import numpy as np
import copy as cp

"""插入insert(index, value)， 注意append只适合尾插法"""
def func1():
    member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
    addition=[88, 90, 85, 90, 88]
    length_m = len(member)
    length_a = len(addition)
    i = 1
    j = 0
    while j < length_a:
        member.insert(i, addition[j])
        j = j + 1
        i = i + 2
    print(member)

def func2():
    member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
    for item in member:
        print(item, end=' ')

def func3():
    test = [[1, 2, 3], [4, 5, 5]]
    rows, cols = np.shape(test)
    print(f"rows: {rows}, cols: {cols}")    #2行3列
    list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]   #3维，7z 3y 1x
    list1[1][2][0] = '小鱿鱼'
    print(list1)

    list2 = [1, 3, 5, 9, 6, 3]
    list3 = cp.copy(list2)
    list2.sort()
    print(list2)
    list3.sort(reverse=True)
    print(list3)
    list4 = list3.copy()
    print(list4)
    list3.reverse()
    print("list3:",list3)
    print("list4:",list4)
    list4.clear()
    print(list4)

def func4():
    old = [1, 2, 3, 4, 5]
    new = old
    old = [6]
    print(new)

def func5():
    list1 = [(x, y) for x  in range(10) for y in range(10) if x%2==0 if y%2!=0]
    list2 = []
    for x in range(10):
        for y in range(10):
            if x%2 == 0:
                if y%2 != 0:
                    list2.append((x, y))
    print(list1)
    print(list2)


def main():
    func5()

if __name__ == '__main__':
    main()