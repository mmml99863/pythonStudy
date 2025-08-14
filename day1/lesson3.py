import fractions

"""
bool类型
"""

print(bool("假")) #True
print(bool("False")) #True
print(bool(False))  #False
print(bool(" ")) # True
print(bool(""))  # False

print(bool(1)) #True
print(bool(0)) #False

'''
值是False的情况
1.定义为False的对象：None和False
2.值为0的数字类型：0, 0.0, 0j, Decimal(0), Fraction(0, 1)即分子为0，分母为1的有理数
3.空的序列和集合："", (), [], set(), range(0)
'''

print(fractions.Fraction(1, 2)) #1/2
print(bool(fractions.Fraction(0, 2))) # False

if 250: # is true
    print('is true')
else:
    print('is false')

if bool(250): # is true
    print('is true')
else:
    print('is false')

"""
逻辑运算 or and not
or和and均遵从短路逻辑
"""
print(1==True) # True
print(0==False) #True
print(True + False)  # 1

print(not 250) # False，这里相当于 not 1
print(3 and 4) # 4 and逻辑表示一直向下，若遇到False，则输出当前为False的值，否则输出最后一个True的值
print(3 and 0 and 4) # 0
print(3 or 4) # 3 or逻辑表示输出遇到的第一个true
print(0 or 4 or 5) # 4

# 练习 False or 0 or 4 or 6 or 9
a = (not 1) or (0 and 1) or (3 and 4)  or (5 and 6) or (7 and 8 and 9)
print(a) # 4

"""
运算符优先级
lambda < if-else < or < and < not x < is, is not , <， <=, >=, !=, ==， ||
"""
# 练习s
"""
False or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
False or 0 or 4 or 6 or 9
4
"""
b = not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9  # 4
print(b)
print(not 1 < 2) # False  先1<2 再not
"""
0 or 1 and False
0 or False
"""
print(0 or 1 and not 2) # False
