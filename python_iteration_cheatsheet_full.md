
# 🔁 Python 遍历语法总结（完整版）

Python 提供了多种灵活且强大的遍历（iteration）方式，适用于不同的数据结构，如列表、元组、字典、集合、字符串等。

---

## ✅ 基础 for 循环遍历列表

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

---

## ✅ 使用 enumerate 获取索引和元素

```python
for index, value in enumerate(fruits):
    print(index, value)
```

```python
# 从索引 1 开始
for index, value in enumerate(fruits, start=1):
    print(index, value)
```

---

## ✅ 遍历字典（dict）

```python
my_dict = {'a': 1, 'b': 2}

# 遍历键
for key in my_dict:
    print(key)

# 遍历键和值
for key, value in my_dict.items():
    print(key, value)

# 遍历值
for value in my_dict.values():
    print(value)
```

---

## ✅ 遍历字符串中的字符

```python
s = "hello"
for char in s:
    print(char)
```

---

## ✅ 遍历集合（set）

```python
my_set = {10, 20, 30}
for val in my_set:
    print(val)
```

> ⚠️ 集合是无序的，因此遍历结果顺序可能不同。

---

## ✅ 使用 range() 进行数值遍历

```python
# 从 0 到 4
for i in range(5):
    print(i)

# 从 1 到 5
for i in range(1, 6):
    print(i)

# 从 10 到 0，步长 -2
for i in range(10, 0, -2):
    print(i)
```

---

## ✅ 同时遍历多个列表（zip）

```python
names = ['Tom', 'Jerry']
ages = [10, 12]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
```

### ⚠️ 注意事项：

- `zip()` 会按**最短的列表长度截断**。
- 不等长列表不会报错，但可能会丢失数据。

```python
a = [1, 2, 3]
b = ['x', 'y']
for i, j in zip(a, b):
    print(i, j)  # 只输出两组
```

### ✅ 不想被截断？用 `itertools.zip_longest`

```python
from itertools import zip_longest
for a, b, c in zip_longest(list1, list2, list3, fillvalue="N/A"):
    print(a, b, c)
```

---

## ✅ 列表推导式遍历（简洁语法）

```python
# 平方
squares = [x**2 for x in range(5)]

# 条件过滤
evens = [x for x in range(10) if x % 2 == 0]

# 嵌套循环
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]

# 条件表达式（三元）
adjusted = [x if x > 0 else 0 for x in [-1, 2, -3]]
```

### ✅ 本质：生成新列表（不会修改原列表）

```python
nums = [1, 2, 3]
new = [x * 2 for x in nums]  # ✅ 新列表
```

> 如果需要原地修改，用普通 for 循环。

---

## 🧠 小结

| 结构     | 方法                                   |
|----------|----------------------------------------|
| 列表     | `for item in list`                    |
| 索引遍历 | `enumerate()`                          |
| 字典     | `for key, value in dict.items()`       |
| 多列表   | `zip()` / `zip_longest()`              |
| 范围遍历 | `range(start, stop, step)`             |
| 推导式   | `[expr for item in iterable]`          |

Python 的遍历语法强大且易读，掌握这些能大大提高代码的简洁性和表达力。
