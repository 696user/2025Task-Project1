# 条件语句
a = 95

if a >= 90:  # 如果
    print("A")
else:
    if a >= 80:  # else if 否则如果
        print("B")
    else:
        if a >= 70:
            print("C")
        else:  # 否则
            print("D")

# 常见关系运算
# < > <= >= == !=

# 常见逻辑运算
# 与或非
# and or not
# *   +  负号
# ∩   ∪ 补集

# for 循环
# range 范围
for i in range(10):  # 等价于 range(0, 10) 左闭右开
    if i % 3 == 0:
        print(i)

# 字符串迭代
for s in "Hello":
    print(s)

# 字符串迭代等价于：
li = ["H", "e", "l", "l", "o"]
for s in li:
    print(s)

# 列表迭代
li = [1, 2, 3, 4, 5]
for x in li:
    print(x)

# 列表元素修改
li[0] = 6

print(li)

# 元组（不可修改）
tu = (1, 2, 3)  # Tuple, Mutable Sequence

# 元组转化为列表
li = list(tu)  # Convert Tuple to List

print(li)
