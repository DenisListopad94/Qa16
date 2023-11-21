# import random
#
#
# n = int(input("enter n:"))
# rand_numb = random.randint(1,n)
# numbers = set()
# for i in range(1,n+1):
#     numbers.add(i)
#
#
# while True:
#     print(numbers)
#     numb = set(map(int,input().split()))
#     if rand_numb in numb:
#         print("YES")
#         numbers = numb.copy()
#         if len(numbers) == 1:
#             print(f"your number {rand_numb}")
#             break
#     else:
#         print("NO")
#         numbers -= numb
#
# phones = {}
#
# while True:
#
#     phone = input()
#     name_phone = phone.split()
#
#     if phone == ".":
#         break
#
#     if len(name_phone) == 2:
#         phones[name_phone[0]] = name_phone[1]
#     else:
#         if name_phone[0] in phones:
#             print(phones[name_phone[0]])
#         else:
#             print(f"{name_phone[0]} not found")
# from random import randint
#
# lst2 = [4, 11, 6, 3, 6, 2]
# lst = []
# for i in range(10):
#     numb = randint(1, 100)
#     if numb % 2 == 0:
#         lst.append(numb)
# print(lst)
# list/set comprehension
# [объект for объекта in итерируемый объект]
# [объект for объекта in итерируемый объект if exp == True]
# [объект if exp == True else объект for объекта in итерируемый объект]
# print([randint(1,10) for elem in range(1, 11)])
# print([elem for elem in lst2])
# print([elem**2 for elem in lst2 if elem % 2 == 0])
# print([elem ** 2 if elem % 2 == 0 else elem ** 3 for elem in lst2])
# print([int(input("enter number:")) for _ in range(4)])
# print(int(input("enter number:")) for _ in range(4))
# dict comprehension
# {key:value for объекта in итерируемый объект}
# {key:value for объекта in итерируемый объект if exp == True}
# {key:value if exp == True else key:value for объекта in итерируемый объект}

# print({elem:randint(1,10) for elem in range(1,11)})


# age = 18


# функции
# процедуры - функции, которые ничего не возвращают
# def greeting(name: str):
#     print(f"Hi {name}")
#
#
#
# greeting("Denis")
# greeting("Kate")

# def info_person(name: str, age: int, friends: list) -> str:
#     info = f"name: {name} age: {age} friends: {friends}"
#     return info
#
#
# person_info = info_person("Max", 20, ["Anna", "Peter", "Oleg"])
# print(person_info)
#
#
# def sum_value(val_1: int = 9, val_2: int = 10) -> tuple:
#     """
#     return sum of two values
#     :param val_1 type int:
#     :param val_2 type int:
#     :return type tuple:
#     """
#     print(val_1,val_2)
#     summa = val_1 + val_2
#     return (summa, val_1, val_2)
#
#
# print(sum_value(val_1=5))
# print(sum_value(val_2=51))
# print(sum_value(val_2=8, val_1=7))
# print(sum_value())

# scope
# builtin
# global
# enclosing
# local

# val = 5
#
#
# def some_fun():
#     global val
#     val += 7
#     print(val)
#
#
# some_fun()
# print(val)

# fiends = ["Peter","Kate"]
#
# def add_friend():
#     friend = "Kolya"
#     fiends.append(friend)
#     print(fiends)
#
# add_friend()
# print(fiends)
# some_global_var = 5
# # some_inner_var = 3
# def out_func():
#     some_out_func_var = 1
#     # some_inner_var = 2
#     def inner():
#         nonlocal some_out_func_var
#         # some_inner_var = 1
#         some_out_func_var += 4
#         # print("some_out_func_var",some_out_func_var)
#         # print("some_global_var:",some_global_var)
#         # print("some_inner_var:", some_inner_var)
#     # inner()
#
# print(out_func)

def some_fun(*numbers , **keys):
    print(numbers)
    print(keys)

def some_fun(number: int = 9):
    print(number)


tup = (5, 1, 6, 1, 3)
some_fun(5)
