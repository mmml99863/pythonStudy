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
    heros.append('黑寡妇')#append每次只能添加一个
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


def main():
    list_revise()
    #list_del()
    #list_add()

if __name__ == '__main__':
    main()