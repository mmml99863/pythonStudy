import  decimal


"""运算"""
i = 0
while i < 1:
    i += 0.1
    print(i)    # 浮点数存在存储误差

if 0.3==0.1+0.2:    # not equal
    print("equal")
else:
    print("not equal")

if 0.2+0.1==0.3:
    print("equal")
else:
    print("not equal")

a = decimal.Decimal('0.1') # 参数是字符串
b = decimal.Decimal('0.2')
c = decimal.Decimal('0.3') # 需要类型转换，否则出错

print(type(a))  # decimal.Decimal
print(a+b)
print(a+b == c) # True

# 科学计数法
print(0.00005)  # 5e-05

# 复数
print(1+2j) # (1+2j)
d = 1+2j
print(d.real) # 实部1.0
print(d.imag)  # 虚部2.0

# 地板除 即数轴向左取
e = 3
f = 2
print(e//f) # 结果是1，向下取整
e = -3
f = 2
print(e//f) # 结果是-2，向下取整
e = 9
f = 3
print(e//f) # 结果是3

# 取余
e = 3
f = 2
print(e%f) # 余数是1
# 内置函数(地板除，余数)
print(divmod(5,2)) #（2，1）
print(divmod(-5,2)) # (-3,1)

# 绝对值
print(abs(-5)) # 绝对值5
print(abs(-3.14)) # 绝对值-3.14
print(abs(3+2j)) # 复数的模:math.sqrt(3*3+2*2) = 3.605551275463989

# 向下截取取整 int()
print(int(3.14)) # 3
print(int(3.64)) # 3
## print(int('3.14')) 错误

# 浮点数
print((float('3'))) # 3.0
print(float('3.14')) # 3.14
print(float(3)) # 3.0

# 科学计数
print(1e+6) # 1000000.0
print(1e+06) # 1000000.0
print(isinstance(1e+6, float))  # true

# 复数
print(complex(1,2)) # (1+2j)
print(complex('3+4j')) # (3+4j)
a = str(3)
b = str(4)
c = a+'+'+b+'j'
print(c, type(c)) # 3+4j <class 'str'>
print(complex(c)) # (3+4j)

# 次方
print(pow(3, 2)) # 9
print(3 ** 2) # 9
print(3.3 ** 2) #10.889999999999999
print(4 ** -2)  # 1/16 = 0.0625
print(pow(4, 2, 3)) # (4^2) % 3 = 1