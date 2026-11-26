"""
Структуры данных Python: list, tuple, set, dict.
Порядок разделов повторяет учебник на docs.python.org/3/tutorial/datastructures.html
"""
import timeit
from collections import deque

# =====================================================================
# 5.1 Подробнее о списках (list): все методы
# =====================================================================
print("=== 5.1 Методы list ===")
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print("Исходный:", fruits)
print("count('apple'):", fruits.count("apple"))
print("index('banana'):", fruits.index("banana"))
print("index('banana', 4):", fruits.index("banana", 4))   # поиск с позиции 4
fruits.reverse()
print("reverse():", fruits)
fruits.append("grape")
print("append('grape'):", fruits)
fruits.sort()
print("sort():", fruits)
print("pop():", fruits.pop(), "->", fruits)
fruits.insert(0, "mango")
print("insert(0, 'mango'):", fruits)
fruits.remove("apple")
print("remove('apple'):", fruits)
fruits.extend(["fig", "lime"])
print("extend([...]):", fruits)
copy_of_fruits = fruits.copy()
fruits.clear()
print("clear():", fruits, "| copy():", copy_of_fruits)

# 5.1.1 Список как стек (LIFO)
print("\n--- Список как стек ---")
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print("Стек:", stack, "pop ->", stack.pop(), "->", stack)

# 5.1.2 Очередь (FIFO): через deque, а не list (pop(0) у списка медленный)
print("\n--- Очередь через deque ---")
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print("popleft ->", queue.popleft(), "->", list(queue))

# 5.1.3 List comprehensions
print("\n--- List comprehensions ---")
nums = list(range(1, 11))                           # ЗАДАНИЕ 1
evens = [n for n in nums if n % 2 == 0]
print("Числа:", nums)
print("Чётные:", evens)
squares = [x ** 2 for x in range(10)]
print("Квадраты:", squares)
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("Пары (два цикла и условие):", pairs)

# 5.1.4 Вложенные comprehensions: транспонирование матрицы
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed = [[row[i] for row in matrix] for i in range(4)]
print("Транспонированная матрица:", transposed)

# =====================================================================
# 5.2 Оператор del
# =====================================================================
print("\n=== 5.2 del ===")
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print("del a[0]:", a)
del a[2:4]
print("del a[2:4]:", a)
del a[:]
print("del a[:]:", a)

# =====================================================================
# 5.3 Кортежи (tuple) и последовательности
# =====================================================================
print("\n=== 5.3 tuple ===")
point = (10, 20)                                    # ЗАДАНИЕ 4
print("Точка:", point)
try:
    point[0] = 99
except TypeError as error:
    print("TypeError:", error)

packed = 12345, 54321, "hello!"                     # упаковка
x, y, z = packed                                    # распаковка
print("Упаковка:", packed, "| распаковка:", x, y, z)
single = ("one",)                                   # кортеж из одного элемента
print("Из одного элемента:", single, "| пустой:", ())
# в кортеже можно держать изменяемый объект
mixed = ([1, 2], "text")
mixed[0].append(3)
print("Список внутри кортежа меняется:", mixed)

# =====================================================================
# 5.4 Множества (set)
# =====================================================================
print("\n=== 5.4 set ===")
tags_list = ["python", "flask", "python", "oop", "flask", "oop", "dict"]   # ЗАДАНИЕ 3
tags = set(tags_list)
print("Список с дублями:", tags_list)
print("Множество:", tags)
print("'flask' in tags:", "flask" in tags)
print("'django' in tags:", "django" in tags)

s1, s2 = set("abracadabra"), set("alacazam")
print("Буквы 1:", sorted(s1), "| буквы 2:", sorted(s2))
print("Разность  s1 - s2:", sorted(s1 - s2))
print("Объединение s1 | s2:", sorted(s1 | s2))
print("Пересечение s1 & s2:", sorted(s1 & s2))
print("Симм. разность s1 ^ s2:", sorted(s1 ^ s2))
print("Set comprehension:", sorted({c for c in "abracadabra" if c not in "abc"}))
empty_set = set()                                   # {} создаёт dict, а не set
print("Пустое множество:", empty_set, "| тип {}:", type({}).__name__)

# =====================================================================
# 5.5 Словари (dict)
# =====================================================================
print("\n=== 5.5 dict ===")
prices = {"хлеб": 50, "молоко": 90, "сыр": 400}     # ЗАДАНИЕ 2
prices["молоко"] = 95
for product, price in prices.items():
    print(f"{product}: {price}")
print("Ключи:", list(prices.keys()))
print("Значения:", list(prices.values()))
print("get('чай'):", prices.get("чай"), "| get с умолчанием:", prices.get("чай", 0))
print("'хлеб' in prices:", "хлеб" in prices)
del prices["хлеб"]
print("После del:", prices)
print("dict(пары):", dict([("sape", 4139), ("guido", 4127), ("jack", 4098)]))
print("dict comprehension:", {n: n ** 2 for n in (2, 4, 6)})
print("dict(kwargs):", dict(sape=4139, guido=4127))

# =====================================================================
# 5.6 Приёмы работы с циклами
# =====================================================================
print("\n=== 5.6 Циклы ===")
for i, v in enumerate(["tic", "tac", "toe"]):
    print("enumerate:", i, v)
questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, ans in zip(questions, answers):
    print(f"zip: What is your {q}? It is {ans}.")
print("reversed:", list(reversed(range(1, 4))))
print("sorted(set):", sorted({"pear", "apple", "pear", "orange"}))

# =====================================================================
# 5.8 Сравнение последовательностей
# =====================================================================
print("\n=== 5.8 Сравнение ===")
print("(1, 2, 3) < (1, 2, 4):", (1, 2, 3) < (1, 2, 4))
print("[1, 2, 3] < [1, 2, 4]:", [1, 2, 3] < [1, 2, 4])
print("'ABC' < 'C' < 'Pascal' < 'Python':", "ABC" < "C" < "Pascal" < "Python")

# =====================================================================
# ЗАДАНИЕ 5: цикл for против comprehension
# =====================================================================
print("\n=== for и comprehension ===")
numbers = range(1000)


def squares_for():
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result


def squares_comprehension():
    return [n ** 2 for n in numbers]


assert squares_for() == squares_comprehension()
print(f"for:           {timeit.timeit(squares_for, number=2000):.4f} c")
print(f"comprehension: {timeit.timeit(squares_comprehension, number=2000):.4f} c")

# =====================================================================
# Проверка для сдачи
# =====================================================================
user = {"хлеб": 50, "молоко": 95, "сыр": 400}
assert isinstance(nums, list)
assert isinstance(user, dict)
assert isinstance(tags, set)
assert isinstance(point, tuple)
print("\nOK")
