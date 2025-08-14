from idlelib.mainmenu import menudefs

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
    print("func2")

def main():
    func2()

if __name__ == '__main__':
    main()