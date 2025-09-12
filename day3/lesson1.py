import keyword
from keyword import iskeyword

"""
字符串
"""
from operator import truediv
from selectors import SelectSelector
from sys import flags

"""回文数组判断"""
def func1(data):
    length = len(data)
    ans = "是回文" if data[:] == data[::-1] else "不是回文"
    print(ans)

"""大小写方法"""
def func2(data):
    print(data)
    print(data.capitalize())    #首字母大写，其余小写Hello world!huang ji
    print(data.casefold())  #所有字母小写hello world!huang ji
    print(data.title()) #每个单词的首字母大写，单词的其余字母都小写Hello World!Huang Ji
    print(data.swapcase())  #字符串中的所有单词大小写反转 HELLO WORLD!hUaNG jI
    print(data.upper()) #所有字母大写HELLO WORLD!HUANG JI
    print(data.lower()) #所有字母小写hello world!huang ji
    """casefold()和lower()的区别：lower()只能处理英文字母，casefold()可以处理更多语言"""

"""左中右对齐"""
def func3(data) :   #len(data) = 9
    print(data.center(15))  #左右用空格填充，源字符串用空格填充：   有内鬼，停止交易！
    print(data.ljust(15))   #左对齐：有内鬼，停止交易！
    print(data.rjust(15))   #右对齐：      有内鬼，停止交易！
    print(data.zfill(15))   #零填充：000000有内鬼，停止交易！
    print('-520'.zfill(5))  #算入符号,零填充：-0520
    print(data.ljust(15, '-'))  #有内鬼，停止交易！------
    print(data.rjust(15, '-'))  #------有内鬼，停止交易！
    print(data.center(15, '-')) #---有内鬼，停止交易！---
    print(data.center(10, '-'))  #默认左对齐，有内鬼，停止交易！-

"""查找"""
def func4(data) :
    """count(指定字符)，返回个数"""
    print(data.count('海'))  #2
    """count(sub[, start[, end]])"""
    print(data.count("海", 0, len(data)-2))    #1， 范围是[0, 7)
    """find()从左往右找第一个， rfind()从右往左找，二者都返回下标"""
    print('左：', data.find('海'), '右：', data.rfind('海'))  #左： 1 右: 7
    print('左：', data.find('你'), '右：', data.rfind('你'))  #未找到返回-1，左： -1 右： -1
    """index(),rindex()"""
    #print('左：', data.index('你'), '右：', data.rindex('你'))  #未找到抛出异常
    """替换,expandtabs(),使用空格替换制表符，并返回新的字符串"""
    temp = """这是一段对对话\t你能试着替换tab为空格吗？"""
    new = temp.expandtabs(7)
    print(temp) #这是一段对对话	你能试着替换tab为空格吗？
    print(new)  #这是一段对对话       你能试着替换tab为空格吗？
    """replace(old, new, count=-1),count指定替换的次数,默认-1即替换全部"""
    print(data.replace('海', 'sea', 1))  #上sea自来水来自海上
    print(data.replace('海', 'sea')) #上sea自来水来自sea上
    """translate(table),table用于指定一个转换规则的表格,str.maketrans()能实现指定规则表格"""
    table = str.maketrans('ABCDEFG', '1234567') #指定转换规则，左边的换成右边对应的
    a = 'I love HuAng'.translate(table)    #I love Hu1ng
    print(a)

    """str.maketrans()第三个参数"""
    table_new = str.maketrans('ABCDEFG', '1234567', 'love') #第三个参数是忽略掉
    b = 'I love HuAng'.translate(table_new)
    print(b)    #I  Hu1ng

"""判断"""
def func5():
    """startswith()，判断指定的子字符串是否出现在字符串的起始位置， 默认初始索引是1"""
    x = 'hello world'
    print(x.startswith('hello'))    #True
    print(x.startswith('h'))  #True
    print(x.startswith('e', 1)) #True
    print(x.startswith('h', 1)) #False
    """endswith(),判断指定字符串是否出现在字符串的结束位置， 默认初始索引是-1到  """
    print(x.endswith('world')) #True
    print(x.endswith('d', -1, -4))  #True
    print(x.endswith('l', -2))  #False
    print(x.endswith('h', -1))   #False

"""判断运用"""
def func6():
    x = "我爱python"
    if x.startswith('爱'):#起始位置判断
        print("hello world!")
    else:
        print("this is an another anchor!")
    if x.isdigit():#都是数字
        print("These words are all digit！")
    else:
        print("Not all digit!")
    x = "We are the champion!"
    if x.istitle():#句子单词的首字母是否大写
        print("They're the title!")
    else:
        print("Not title words")
    print(x.title().istitle())  #True
    print(x)#We are the champion! 注意需要赋值
    s = "   It'sthisthespace?"
    y = " "
    print(s.isspace())#如果字符串中只包含空格，则返回 True，否则返回 False.
    print(y.isspace())#True
    z = "this is a sentence\n"
    print(z.isprintable())#转义字符串不可打印，False
    z = r"this is a sentence\n"
    print(z.isprintable())#True

"""数字与进制判断"""
def func7():
    x = "12345"
    print(x.isdigit())#所有字符都是阿拉伯数字True
    print(x.isnumeric())#字符串是否只由数字组成，如果字符串中只包含数字则返回True，否则False
    print(x.isdecimal())#十进制True
    x = "一二三四五"
    print(x.isnumeric())#True
    print(x.isdigit())#False
    x = "ⅠⅡⅢ"
    print(x.isnumeric())#True
    print(x.isdigit())#False
    print(x.isalnum())#isdigit()||isnumeric()||isdecimal() == true时为true
    print(x.isidentifier())#是否是有效标识符（命名规则）
    """判断是否是python的关键字"""
    print(iskeyword('if'))#True




def main():
    """    data='hello world!HuAng Ji'
    func2(data)
    x = '有内鬼，停止交易！'
    func3(x)
    s = "上海自来水来自海上"
    func4(s)"""
    #func5()
    #func6()
    func7()

if __name__=='__main__':
    main()