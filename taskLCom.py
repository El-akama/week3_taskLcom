# task1
# nums = range(100)
# odd_nums = [num for num in nums if num % 2 == 0]
# print(odd_nums)

# task2
# nums = range(15)
# numss = [num * num for num in nums]
# print(list(nums))
# print(numss)

# task3
# nums = ['1', '2', '3', '4', '5', '6']
# num_int = [int(x) for x in nums]
# print (num_int)

# task4
# kv = {'a': 5, 'b': 3, 'c': 8, 'd': 14, 'e': 18, 'f': 25}
# values = {key: value for key, value in kv.items() if value % 3 == 0 or value % 5 == 0 for key, value in kv.items()}
# print(values)
# не смог заменить на Foo и Bar


# kv = {'a': 5, 'b': 3, 'c': 8, 'd': 14, 'e': 18, 'f': 25}
# foo = {key: value % 3 for key, value in kv.items()}
# bar = {key: value % 5 for key, value in kv.items()}
# print(foo)
# print(bar)
# не смог заменить на Foo и Bar

# ура почти сделал
# kv = {'a': 5, 'b': 3, 'c': 8, 'd': 14, 'e': 18, 'f': 25, 'g': 35}
# values = [print("Foo") if v % 3 == 0 else print("Bar") if v % 5 == 0 else None for k, v in kv.items()]


# этоо не надо трогать
# values = [print("Foo") if value % 3 == 0 else print("Bar") if value % 5 == 0 else None for value in kv.values()]
# key: value  if value % 3 == 0 or value % 5 == 0 for key, value in kv.items()

# {value: key for key, value in sodi.items()}

# kv = {'a': 5, 'b': 3, 'c': 8, 'd': 14, 'e': 18, 'f': 25}
# values = {print("Foo") if value % 3 == 0 else print("Bar") if value % 5 == 0 else key for key, value in kv.items()}
# print(values)

kv = {'a': 5, 'b': 3, 'c': 8, 'd': 14, 'e': 18, 'f': 25}

newkv = {key: 'Foo' if value % 3 == 0 else 'Bar' for key, value in kv.items() if value % 3  == 0 or value % 5 == 0}
print(newkv)