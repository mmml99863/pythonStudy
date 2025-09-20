"""参数传递:收集参数 *name"""
def func1(*args, a, b):
    print(a, b)
    print("以下是收集参数", end=" ")
    for item in args:
        print(item, end=" ")
    print()

"""关键字参数   **name"""
def func2(d, *args, **kwargs):
    print(d)#1
    print(args, f"The type of args is {type(args)}")#(1, 2, 3) The type of args is <class 'tuple'>
    print(kwargs, f"The type of kwargs is {type(kwargs)}")#{'a': 1, 'b': 2, 'c': 3, 'd': 4} The type of kwargs is <class 'dict'>

"""收集参数打包"""
#def func3(*k, *val): 注意一个方法中不能有多个收集参数和打包参数
def func4(*k):
    val = (1, 2, 3)
    dic_zip = dict(zip(k, val))#{4: 1, 5: 2, 6: 3}
    print(dic_zip)

"""参数的解包"""
def func5(a, b, c, d):
    print(a," " ,b," ", c," ", d)#1   2   3   4

def func6(**a):
    print(a)#{'1': 1, '2': 2, '3': 3, '4': 4}

"""作用域：变量可以被访问的范围"""
# 局部作用域
def func7():
    x = "520"
    y = "1314"
    print(x, " ",y)

all_val = 'hello'
#全局作用域与局部作用域冲突，优先使用局部作用域覆盖
def func9():
    all_val = "world！"#此时值域有覆盖
    print(id(all_val))

#全局作用域
def func8():
    print(all_val)#覆盖的值仅是局部作用域内生效

"""global语句"""
def func10():
    global all_val
    print(all_val, f"The id of all_val in func10 is {id(all_val)}")#The id of all_val is  2575695462928

"""嵌套函数"""
def func_a():
    x = 520
    def func_b():
        x = 1314
        print(x, f"The id of x in funcB is {id(x)}")
    #嵌套函数只能在内部去调用
    print(x, f"The id of x in funcA is {id(x)}")#520 The id of x in funcA is 1605031270896
    func_b()#1314 The id of x in funcB is 1605033393968

"""nonlocal语句"""
def func11():
    x = 520
    def func_b():
        nonlocal x
        x = 1314
        print(x, f"The id of x in funcB is {id(x)}")
    """
    520 The id of x in funcA is 1964140108272
    1314 The id of x in funcB is 1964142231344
    1314 The id of x in funcA is 1964142231344
    """
    print(x, f"The id of x in funcA is {id(x)}")
    func_b()
    print(x, f"The id of x in funcA is {id(x)}")

"""
LEGB[local enclosed global build-i n]规则:python变量的解析机制
查找顺序【优先级】：local（局部） -> enclosed（闭包） -> global（全局） -> build-in（内置）
local（局部）：指在函数或方法内部定义的局部变量。python优先在局部作用域内找变量
enclosed（闭包）：指嵌套函数中外层函数的变量。如果局部作用域中未找到，则查找外层函数的变量
global（全局）：指在模块级别定义的变量。如果在局部和闭包作用域中都未找到，python会查找全局作用域中的变量
build-in（内置）：指python内置的名称，如str(),int(),print()等。如果在LEG中未找到则找内置名称
"""
def func12():
    pass

"""
复习函数：*号【关键字参数】
    *前不需要关键字，*号后需要关键字参数
"""
def func13(a, b,*, c, d):
    print('a={0}， b={1}, c={2}, d={3}'.format(a, b, c, d))

"""
复习函数：/【位置参数】
    /之前的参数只能用位置传递，/之后的参数可以使用位置或关键字传递
"""
def func14(a, b, /, c, d):
    print('a={0}， b={1}, c={2}, d={3}'.format(a, b, c, d))


if __name__ == '__main__':
    func1(1, 2, 3, 4,a=['hello', 'world'], b='!')
    func2(1, 1, 2, 3,a=1, b=2, c=3)
    func4(4, 5, 6)
    agrs = (1, 2, 3, 4)
    str_agrs=[]
    for agr in agrs:
        str_agrs.extend(str(agr))#尾部添加
    func5(*agrs)
    kwargs = dict(zip(str_agrs, agrs))#keywords must be strings
    func6(**kwargs)
    func7()
    print(id(all_val))#id = 2575695462928
    func9()#world！id = 1452258408880
    func8()#hello
    print("The id of all_val is ", id(all_val))#The id of all_val is  2575695462928
    func10()
    func_a()
    func11()
    func13(1, 2, c = 3, d = 4)
    func14(1, 2, 3, 4)#a=a， b=c, c=c, d=d
    func14('a', 'c','c', d='d')#a=a， b=c, c=c, d=d



