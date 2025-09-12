import itertools

"""序列1"""
def func1():
    a = [1, 2, 3]
    b = [4, 5, 6, 7, 8]
    print(a+b)#[1, 2, 3, 4, 5, 6, 7, 8]
    c = (1, 2, 3)
    d = (4, 5, 6, 7, 8)
    print(c+d)#(1, 2, 3, 4, 5, 6, 7, 8)
    print(a * 2)#[1, 2, 3, 1, 2, 3]
    e = [[1, 2, 3],
         [4, 5, 6, 7, 8]]
    f = [num for hori in e for num in hori if num//2==3]
    print(f)#[6, 7]
    g = [1, 2, 3]
    #id是变量的唯一标识符
    print(id(g))#2862173106432
    g *= 3
    print(id(g))#2862173106432
    t = tuple([1, 2, 3])
    print(id(t))#2574244253696
    t *= 2
    print(id(t))#2574242900736
    """is 和 is not 是同一性运算符，判断二者的id值是否相等,判断是否为同一个对象"""
    x = "hello"
    y = "hello"
    print(x is y)#True
    x = [1, 2, 3]
    y = [1, 2, 3]
    print(x is y)#False
    x = tuple([1, 2, 3])
    y = tuple([1, 2, 3])
    print(x is y)#False
    """in 和 not in"""
    print("test" in "test web!")#True
    """del语句删除已定义的变量，删除一个或多个变量，删除后会释放空间"""
    h = [1, 2, 3, 4, 5]
    print(h)
    del h[1:4]
    print("the sizeOf h is {}".format(len(h)))    #h = [1, 5]  the sizeOf h is 2
    h = [1, 2, 3, 4, 5]
    h[1:4] = []#[1, 5]
    print(h)
    h = [1, 2, 3, 4, 5]
    del h[::2]
    print(h)#从头至尾，步距为2的依次删除，结果为[2, 4]
    #h[::2] =[]#ValueError: attempt to assign sequence of size 0 to extended slice of size 1

    #del h
    #print(h)#cannot access local variable 'h' where it is not associated with a value
    i = [1, 2, 3, 4, 5]
    i.clear()
    print(i)#[]
    i = list(range(5))
    del i[:]
    print(i)#[]

"""序列2"""
def func2():
    print(list("hello world"))#['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print(list((1, 2, 3, 4, 5)))#[1, 2, 3, 4, 5]
    print(list(range(5)))#[0, 1, 2, 3, 4]
    print(list(range(1, 6)))#[1, 2, 3, 4, 5]
    print(list(range(1, 6, 2)))#[1, 3, 5]
    print(tuple(range(1, 6)))#(1, 2, 3, 4, 5)
    """min(iterable)和max(iterable)函数对比传入的参数，返回最大最小值"""
    a = list(range(1, 6))
    min_value = min(a)
    print(min_value)#1
    b = "hello"
    min_value = min(b)
    print(min_value)#e，此时比较的是unicode编码
    print(ord(" "))#32
    print(chr(32))#" "
    c = []
    min_value = min(c, default="no value")
    print(min_value)#no value
    min_value = min(range(1, 6))#1
    print(min_value)
    """sum()"""
    print(sum(range(1, 6)))#15
    a = range(1, 6)
    print(sum(a, start=100))#115
    """sorted()"""
    a = [3, 5, 9, 2, 1]
    a.sort()
    print(a)#[1, 2, 3, 5, 9]
    a = [3, 5, 9, 2, 1]
    print(sorted(a))#[1, 2, 3, 5, 9]
    a.sort(reverse=True)
    print(a)#[9, 5, 3, 2, 1]
    a = [3, 5, 9, 2, 1]
    print(sorted(a, reverse=True))#[9, 5, 3, 2, 1]
    b = ["Book", "Banana", "Text", "Apple"]
    print(sorted(b))#['Apple', 'Banana', 'Book', 'Text']
    print(sorted(b, key=len))#['Book', 'Text', 'Apple', 'Banana']
    b.sort(key=len)
    print(b)#['Book', 'Text', 'Apple', 'Banana']
    print(sorted("Banana"))#['B', 'a', 'a', 'a', 'n', 'n']
    print(sorted((1, 0, 0, 8, 6)))#[0, 0, 1, 6, 8]
    b = sorted((1, 0, 0, 8, 6))
    print(f"type of b: {type(b)}")#type of b: <class 'list'>
    """reversed()"""
    reversed(b)
    print(list(reversed(b)))#[8, 6, 1, 0, 0]

"""序列3"""
def func3():
    """all()任意值均为True则为True与any()值中有一个为True则为True"""
    a = [1, 1, 2]
    b = [1, 1, 0]
    print(all(a))#True
    print(all(b))#False
    print(any(a))#True
    print(any(b))#True
    """enumerate()"""
    season = ["Spring", "Summer", "Autumn", "Winter"]
    print(list(enumerate(season)))#[(0, 'Spring'), (1, 'Summer'), (2, 'Autumn'), (3, 'Winter')]
    print(list(enumerate(season, start=10)))#[(10, 'Spring'), (11, 'Summer'), (12, 'Autumn'), (13, 'Winter')]
    """zip()创建一个聚合多个可迭代对象的迭代器，将作为参数传入的每个可迭代对象的每个元素依次组合成元组，即第i个元组包含来自每个参数的第i个元素"""
    c = list(range(1, 4))
    d = list(range(5, 8))
    e = zip(c, d)
    print(list(e))#[(1, 5), (2, 6), (3, 7)]
    f = list(range(3, 6))
    g = zip(c, d, f)
    print(list(g))#[(1, 5, 3), (2, 6, 4), (3, 7, 5)]
    a = list(range(1, 6))
    b = list(range(5, 8))
    c = zip(a, b)
    print(list(c))#以最短的为准[(1, 5), (2, 6), (3, 7)]
    c = list(range(1, 9))
    ans = itertools.zip_longest(a, b, c)
    print(list(ans))#[(1, 5, 1), (2, 6, 2), (3, 7, 3), (4, None, 4), (5, None, 5), (None, None, 6), (None, None, 7), (None, None, 8)]
    """map()根据提供的函数对提供的可迭代对象的每个元素进行运算，并将返回运算结果的迭代器"""
    mapped = map(ord, "hello world")#计算后面的可迭代对象的Unicode数值并返回可迭代对象
    print(list(mapped))#[104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
    #当传入的函数需要多个参数时
    mapped = map(pow,[2, 3, 10], [3]*3)#注意要数量对应
    print(list(mapped))#[8, 27, 1000]
    print(list(map(max, [1, 3, 2, 9, 7], [3, 4, 5], [3, 6, 11])))#[3, 6, 11]返回的数值是以列进行比较的
    """filter()函数会根据提供的函数对指定的可迭代对象的每个元素进行计算，并将运算结果为真的元素，以迭代器的形式返回"""
    res = filter(str.islower, "hello world")
    print(list(res))#['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    res = filter(lambda s: s.islower(), 'Hello world')
    print(list(res)) # ['e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

def func4():
    """
    迭代器与可迭代对象
    1.迭代器一定是一个可迭代对象
    2.可迭代对象可以重复使用
    3.迭代器是一次性的
    """
    mapped = map(ord, "hello world")
    for item in mapped:
        print(item)
    print(list(mapped))#[]
    x = [1, 2, 3, 4, 5]
    y = iter(x)#y是迭代器
    print(f"type of X is{type(x)}, type of Y is {type(y)}")#type of X is<class 'list'>, type of Y is <class 'list_iterator'>
    for item in y:
        print(item)
    print(list(y))# []
    y = iter(x)
    print(next(y, "列表"))#1
    print(next(y, "列表"))#2
    print(next(y, "列表"))#3
    print(next(y, "列表"))#4
    print(next(y, "列表"))#5
    print(next(y, "列表"))#列表



if __name__ == '__main__':
    #func1()
    #func2()
    #func3()
    func4()