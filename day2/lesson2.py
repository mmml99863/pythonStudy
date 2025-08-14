"""元组:元组内元素不可以改变，即不支持：增，删，改，支持列表的切片，列表推导式"""
def fun1():
    a = (1, 2, 3, 4, 5, "hello")
    print(a)
    b = 1, 2, 3, 4, 5, "hello"
    print(b)    #(1, 2, 3, 4, 5, 'hello')
    print(b[0]) #1
    print(b[-1]) #hello
    c = a[:3]
    print(c)    #(1, 2, 3)
    d = a[::2]
    print(d)    #(1, 3, 5)
    c = a[::-1]
    print(c)    #('hello', 5, 4, 3, 2, 1)

def fun2():
    a = (1, 2, 3, 4, 5, 3, 2, 3)
    print(a.count(3))   #3出现的次数为3
    print(a.index(3))   #3首次出现的下标为2
    b = (4, 5, 6)
    print(a+b)  #拼接(1, 2, 3, 4, 5, 3, 2, 3, 4, 5, 6)
    print(a*3)  #(1, 2, 3, 4, 5, 3, 2, 3, 1, 2, 3, 4, 5, 3, 2, 3, 1, 2, 3, 4, 5, 3, 2, 3)
    w = a, b
    print(w) #嵌套元组((1, 2, 3, 4, 5, 3, 2, 3), (4, 5, 6))
    for i in a:
        print(i, end=" ")#1 2 3 4 5 3 2 3
    print()
    """列表推导式"""
    c = [item for item in b]
    print(c)
    c = (520)   #<class 'int'>
    print(type(c))
    c = (520, ) #<class 'tuple'>
    print(type(c))

"""元组的打包和解包"""
def fun3():
    a = (1, 'hello', [1, 2, 3], 3.14)#打包
    print(a)
    x, y, z, e = a#解包
    print(x, y, z, e)   #1 hello [1, 2, 3] 3.14
    """列表的打包和解包"""
    b = [1, 'hello', 3.14]
    x, y, z = b
    print(x, y, z)  #1 hello 3.14
    """字符串的打包和解包"""
    a, b, c, d ,e = 'hello'
    print(a, b, c, d, e) #h e l l o
    a, b ,*c = 'hello'
    print(a, b, c)  #h e ['l', 'l', 'o']
    x, y = 10, 20   #先转换成元组打包，再解包
    print(x, y)

"""元组中的元素是指向可变列表时，则可变"""
def fun4():
    a = [ 1, 2, 3]
    b = [4, 5, 6]
    w = (a, b)
    print(w[0])#[1, 2, 3]
    w[0][1] = 8   #([1, 8, 3], [4, 5, 6])
    print(w)


fun4()