# 1. float() -- 将数据转换成浮点型
num1 = 1
str1 = '10'

num2 = float(num1)
print(type(num2))
print(num2)

print(float(num1))
print(float(str1))

# 2. str() -- 将数据转换成字符串型
print(type(str(num1)))


# 3. tuple() -- 将一个序列转换成元祖
list1 = [10,20,30]
print(tuple(list1))

# 4. list() -- 将一个序列转换成列表
t1 = (100,200,300)
print(list(t1))

# 5. eval() -- 计算在字符串串中的有效Python表达式，并返回一个对象（将数据转换成原有类型）
str2 = '1'
str3 = '1.1'
str4 = '(10,20,30)'
str5 = '[100,200,300]'

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
