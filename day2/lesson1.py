import copy

"""
列表:可以存放任何类型的数据，不用所有数据类型相同
"""
def func1():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5, "上山打老虎"]
    print(a)
    print(b)

    c = [1, 2, 3, 4, 5, b, "测试"]
    print(c)
    print(c[0]) #1

    for item in c:
        print(item)

    length = len(c)
    for i in range(length): #注意！！！下标为[0, length-1]
        print(c[i])
    print()

    for i in range(0, length):#注意！！！
        print(c[i])
    print()

    print(c[-1])    # 倒数第一个
    print(c[-2])    # 倒数第二个

    """列表切片，注意右侧有数时表示开区间，否则闭区间"""
    print(c[0:3])#切片，表示前三个[0, 3)
    print(c[1:-1])#切片，表示[1, length)
    print()
    print(c[:-1])#切片，表示[-2, -1)
    print()
    print(c[:])#切片，表示全体
    print()
    print(c[2:])#切片，表示[2, length-1]
    print()
    print(c[0:-1:2])#切片，并表示[0:-1)，步距为2
    print()
    print(c[::2])#切片，并表示[0:-1]，步距为2
    print()
    print(c[::-1])#倒叙输出

"""列表的增"""
def list_add():
    heros=['钢铁侠', '绿巨人']
    heros.append('黑寡妇')#append每次只能添加一个到尾部
    print(heros)
    heros.extend(['灭霸', '雷神', '鹰眼'])#extemd里的参数必须是可迭代对象，且只能增加到尾部
    print(heros)
    d = [1, 2, 3, 4, 5]
    len_d = len(d)
    d[len_d:] = [6, 7, 8, 9]#可迭代后接可迭代
    print(d)
    d[:] = [10, 20, 30, 40, 50]
    print(d, ' ', len(d))    #整体替换[10, 20, 30, 40, 50]，长度为5
    #insert(位置， 数值)
    d.insert(2, 3) #将3插入d[2]，[10, 20, 3, 30, 40, 50]

"""列表的删"""
def list_del():
    heros = ['绿巨人', '钢铁侠', '黑寡妇', '蜘蛛侠']
    print(heros)
    heros.remove('绿巨人')#remove()删除指定元素的第一个，若元素不存在就会报错
    print(heros)
    """
    heros.remove('绿巨人')#若元素不存在就会报错
    print(heros)
    """
    heros.pop(len(heros) - 1)#pop()删除指定下表的元素
    print(heros)
    heros.clear()#列表整体清空
    print(heros)

"""列表的改，注意：列表可变，字符串不可以改变"""
def list_revise():
    heros = ['绿巨人', '钢铁侠', '黑寡妇', '蜘蛛侠', '灭霸']
    print(heros)
    heros[len(heros)-1] = '雷神'
    print(heros)
    heros[2:] = [1, 2, 3, 4, 5] # 将从2开始的都替换掉，结果是['绿巨人', '钢铁侠', 1, 2, 3, 4, 5] ，但可能替换报错
    print(heros)
    heros[:] = ['林冲', '李逵', '鲁智深']
    print(heros) # 整体替换
    nums = [1, 3, 6, 4, 5]
    nums.sort()
    print(nums) # 升序排序
    nums.reverse()
    print(nums)  # 翻转元素
    heros.reverse()
    print(heros)
    nums = [1, 3, 6, 4, 5]
    nums.sort(reverse=True)
    print(nums)
    print(nums.count(4))#查找4出现的次数1
    print(heros.index('李逵'))#查找李逵，并返回第一个索引值,未出现则报错
    #index(value, start, end) 查找[start, end)内的值
    print(nums.index(3, 0, 4))
    nums2 = nums.copy() # 整体浅拷贝
    print(nums2) #[6, 5, 4, 3, 1]
    nums3 = nums[1:3].copy() # [5, 4]
    print(nums3)

'''列表的加法和乘法'''
def list_add_and_mul():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8, 9, 10]
    print(nums1 + nums2)
    print(nums1 * 3) #列表中元素复制为原来的3倍，即[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
              [1,2,3,4,5,6,7,8,9],
              nums1]    #二维矩阵
    print(matrix)
    """
    1 2 3 
    4 5 6 
    7 8 9 
    1 2 3 4 5 6 7 8 9 
    1 2 3 4 5 
    """
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
    print(matrix[0][1]) # 0行1列 = 2
    a = [0]*3
    print(a)    # 1维
    for i in range(3):
        a[i] = [0]*3 #2维
    x = [[1, 2, 3]] * 3  # 三次引用[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print(a)

"""is同一运算符：判断是否指向内存中的同一存储位置，str是常量，可同时存储"""
def func_is():
    X = "huang ji"
    Y = "huang ji"
    print(X is Y)   #true
    X = [1, 2, 3]
    Y = [1, 2, 3]
    print(X is Y)   #False
    a = [[0]*3]*3       #引用，不是copy，一改全改
    b = [0]*3
    for i in range(3):
        b[i] = [0]*3
    print(a)
    print(b)
    print(a is b)   #False
    print(b[0] is b[1])     #False
    print(a[0] is a[1])      #True

"""变量引用数值"""
def func2():
    x = [1, 2, 3]
    y = x #引用
    print(x is y)   #true
    x[1] = 0
    print(y)    #[1, 0, 3]

"""拷贝"""
def func_copy():
    """浅copy"""
    x = [1, 2, 3]
    y = x.copy()    #浅copy，只copy对象
    print(x is y)   #False
    x[1] = 0
    print(y)    #[1, 2, 3]
    z = x[:]
    print(x is z)   #False
    x[1] = 4
    print(z)    #[1, 0, 3]

    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(x)
    y = x.copy()    #仅copy外层，内里任是引用，即相当于一个文件夹里全是快捷方式
    print("hello")
    print(x[1] is y[1])   #True，证明是引用
    x[1][1] = 0
    print(x)    #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    print(y)    #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    """深copy"""
    print()
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = copy.copy(x)    #浅copy
    print(x is y)   #False
    x[1][1] = 0
    print(x)    #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    print(y)    #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = copy.deepcopy(x)    #深度copy，将对象与其子对象...都copy
    print(x is y)   #False
    x[1][1] = 0
    print(x)    #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    print(y)    #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]

"""列表推导式:效率比循环效率高1倍"""
def func3():
    x = [1, 2, 3, 4, 5]
    for i in range(len(x)):
        x[i] = x[i]*2
    print(x)
    x = [1, 2, 3, 4, 5]
    """[表达式 for 表达式执行次数 in iterable]"""
    y = [x[i]*2 for i in range(len(x))]
    print(y)
    z = [i+1 for i in range(0, 10)]   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(z)
    m = []
    for i in range(0, 10):
        m.append(i+1)   #append无需列表的考虑长度问题
    print(m)
    n = [item*2 for item in 'hello world!'] #['hh', 'ee', 'll', 'll', 'oo', '  ', 'ww', 'oo', 'rr', 'll', 'dd', '!!']
    print(n)
    u = [ord(item) for item in 'hello world!'] #ord()单字符转码，[104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]
    print(u)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    col2 = [matrix[x][1] for x in range(len(matrix))]   #[2, 5, 8]
    print(col2)
    col3 = [row[1] for row in matrix]   #[2, 5, 8]
    print(col3)
    """输出正斜对角的"""
    col4 = [matrix[i][i] for i in range(len(matrix))]
    print(col4)
    """输出负斜对角"""
    length = len(matrix)
    col5 = [matrix[i][-i-1] for i in range(length)]   #[3, 5, 7]或matrix[i][length-i-1]
    print(col5)

"""列表推导式:[表达式 for target in iterable if 条件]"""
def func4():
     a = [[0]*3 for i in range(3)]  #表示[0]*3 执行三次，即[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
     print(a)
     a[1][1] = 1
     print(a)   #[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
     b = [i for i in range(10) if i%2==0]
     print(b)#[0, 2, 4, 6, 8]
     """筛选h开头的单词"""
     words = ['hello', 'world', 'python', 'java', 'c#']
     ans = [item for item in words if item[0]=='h']
     print(ans)

"""列表推导式:[表达式 for target1 in iterable1 for target2 in iterable2...]"""
def func5():
    """二维降为一维"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row = [i for item in matrix for i in item]
    print(row)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
    """['hw', 'ho', 'hr', 'hl', 'hd', 'ew', 'eo', 'er', 'el',
     'ed', 'lw', 'lo', 'lr', 'll', 'ld', 'lw', 'lo', 'lr', 'll', 'ld', 'ow', 'oo', 'or', 'ol', 'od']"""
    row2 = [x+y for x in 'hello' for y in 'world']
    print(row2)

"""列表推导式：[表达式 for target1 in iterable1 if condition1 for target2 in iterable2 if condition2...]"""
def func6():
    #[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3), (6, 1), (6, 3), (8, 1), (8, 3)]
    mul_ans = [(x, y) for x in range(10) if x%2==0
               for y in range(5) if y%2!=0]
    print(mul_ans)

def main():
    func6()
    #func5()
    #func4()
    #func3()
    #func_copy()
    #func2()
    #func_is()
    #list_add_and_mul()
    #list_revise()
    #list_del()
    #list_add()

if __name__ == '__main__':
    main()