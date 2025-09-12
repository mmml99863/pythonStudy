"""摩斯密码"""
def func1(data):
    charSet = {
        'A':'.-',
        'B':'-..',
        'C':'-.-.',
        'D':'-..',
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-',
        'V':'...-',
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..'
    }
    numSet={
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----'
    }

    for item in data:
        if item.isalpha():
            if item in charSet:
                print(charSet[item],end=' ')
        elif item.isnumeric():
            if item in numSet:
                print(numSet[item],end=' ')
        else:
            print(item, end='')
def func2():
    x = {"hero1":"吕布", "hero2":"关羽", "hero3":"张三"}
    print(type(x))#<class 'dict'>
    print(x["hero1"])#吕布
    x["hero4"] = "刘备"
    print(x)#{'hero1': '吕布', 'hero2': '关羽', 'hero3': '张三', 'hero4': '刘备'}
    a = [1, 2, 3]
    b = [4, 5, 6, 7]
    c = dict(zip(a, b))
    print(c)#{1: 4, 2: 5, 3: 6}
    d = dict(张三 = "张三", 李四= "李四")
    print(d)#{'张三': '张三', '李四': '李四'}
    e = dict([("hero1","吕布"), ("hero2", "关羽")])
    print(e)#{'hero1': '吕布', 'hero2': '关羽'}
    print(list(zip(a, b)))#[(1, 4), (2, 5), (3, 6)]

"""字典的增"""
def func3():
    """fromkeys(iterable[, value]),使用iterable创建字典，并将值初始化为value指定的值"""
    a = dict.fromkeys("hello",33)
    print(a)
    a['e'] = 250#修改值
    print(a)

"""字典的删"""
def func4():
    a = dict.fromkeys("hello",33)
    print(a)#{'h': 33, 'e': 33, 'l': 33, 'o': 33}
    a.pop('e')
    print(a)#{'h': 33, 'l': 33, 'o': 33}
    print(a.pop('z','没有'))#当没有该元素时输出默认值
    print(a.pop("h","没有h"))#33
    print(a.popitem())#('o', 33)
    print( a)#{'h': 33}
    del a['l']
    print(a)#{}
    a = dict.fromkeys("hello", 33)
    a.clear()
    print(a)#{}

"""改"""
def func5():
    a = dict.fromkeys("hello", 233)
    a['h'] = 155
    print(a)#{'h': 155, 'e': 233, 'l': 233, 'o': 233}
    a.update({"h": 333, 'e': 77})
    print( a)#{'h': 333, 'e': 77, 'l': 233, 'o': 233}

"""查"""
def func6():
    a = dict.fromkeys("hello", 33)
    b = a.get('A', "这里没有a")#这里没有a
    print(b)#这里没有a
    c = a.get('H',"这里没有H")#这里没有H
    print(c)
    c = a.get('h',"这里没有h")#33
    print(c)
    """查找一个字典值如果在，则返回它的值，如不在则设置并加入字典中"""
    print(a.setdefault('H','这是一个新值'))#这是一个新值
    print(a)#{'h': 33, 'e': 33, 'l': 33, 'o': 33, 'H': '这是一个新值'}
    print(a.setdefault('e','这是一个新值'))#33
    """items(), keys(), values()获取字典的键值对，键，值"""
    """视图对象：字典的动态视图，当字典的内容发生改变时，视图对象的内容也会发生相应的改变"""
    keys = a.keys()#键的视图对象
    values = a.values()#值的视图对象
    items = a.items()#键值对的视图对象
    print(items)#dict_items([('h', 33), ('e', 33), ('l', 33), ('o', 33), ('H', '这是一个新值')])
    a.pop('h')
    print(items)#dict_items([('e', 33), ('l', 33), ('o', 33), ('H', '这是一个新值')])
    b = a.copy()
    print(b)#浅拷贝{'e': 33, 'l': 33, 'o': 33, 'H': '这是一个新值'}
    print(len(b))#4
    print('e' in b)#True判断键是否在字典中
    print(list(b.keys()))#['e', 'l', 'o', 'H']
    print(list(b.values()))#[33, 33, 33, '这是一个新值']
    print(list(b.items()))#[('e', 33), ('l', 33), ('o', 33), ('H', '这是一个新值')]
    a = iter(b.keys())
    for item in a:
        print(item)
    c = list(reversed(b.keys()))
    print(c)#['H', 'o', 'l', 'e']
    subjects=["语文", "数学", "英语"]
    score_gy = [60, 70, 80]
    score_zf = [99, 100, 100]
    dic_gy = dict(zip(subjects, score_gy))
    dic_zf = dict(zip(subjects, score_zf))
    students = {"关羽": dic_gy, "张飞": dic_zf}
    print(students.get("关羽").get('数学'))#70
    scores = dict({"关羽": score_gy, "张飞": score_zf})
    print(scores)#{'关羽': [60, 70, 80], '张飞': [99, 100, 100]}
    print(scores.get("关羽")[1])#70
    """字典推导式"""
    a = [1, 2, 3, 4, 5]
    b = ['a', 'b', 'c', 'd', 'e']
    c = dict(zip(a, b))
    print(c)#{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    e = {v:k for k,v in c.items()}
    print(e)#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    f = {k:v for k,v in c.items() if k>3}
    print(f)#{4: 'd', 5: 'e'}
    a = {x:y for x in [1, 3, 5] for y in [2, 4, 6]}
    print(a)#{1: 6, 3: 6, 5: 6}键值覆盖到最新的






if __name__ == '__main__':
    #code = input("请输入要转换的英文：")
    #func1(code)
    #func2()
    #func3()
    #func4()
    #func5()
    func6()