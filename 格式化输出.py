"""

1.准备数据
2.格式化符号输出数据

"""

age = 27
name = 'hepan'
weight = 68.5
stu_id = 1

# 1.今年我的年龄是X岁
print('今年我的年龄是age岁')

# 2.我的名字是x
print('我的名字是%s' % name)

# 3.我的体重是x公斤
print('我的体重是%.1f公斤' % weight)

# 4.我的学号是x
print('我的学号是%d' %stu_id)

# 4.1我的学号是001
print('我的学号是%03d' %stu_id)

# 5.我的名字是x，今年x岁了
print('我的名字是%s,今年%d岁' % (name, age))

# 5.1我的名字是x，明年x岁了
print('我的名字是%s,明年%d岁' % (name, age+1))

# 6.我的名字是x，今年x岁了，体重是x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重是%.1f公斤，学号是%03d' %(name, age, weight, stu_id))
