# def is_chet_numb(number: int) -> bool:
#     return not number % 2
#
#
# print(is_chet_numb(9))

# f = lambda number: not number % 2
# print(f(10))


# numb_1, numb_2 = map(int, input().split())
# print(numb_1, numb_2)

# variant 1
# for ind in range(len(lst)):
#     lst[ind] **= 2
#
# print(lst)

# variant 2

# print([elem**2 for elem in lst])

# variant 3
# def sqr_numb(numb):
#     return numb ** 2

# lst = list(map(lambda numb: numb**2 if not numb % 2 else 0, lst))
# print(lst)

# lst = list(filter(lambda elem: not elem % 2, lst))
# print(lst)
# lst = [6, 21, -16, 22, 81, -88, 91]
#
# # lst.sort(key=lambda elem: not elem % 2)
# lst.sort(key=lambda elem: abs(elem) % 10)
# print(lst)
# x = 1
# y = 2
# f = lambda x, y: x + y
# print(f(x,y))

# recursion

# def factorial(number: int) -> int:
#     summa = 1
#     for numb in range(1, number + 1):
#         summa *= numb
#     return summa
#
#
# #
# #
# print(factorial(1000))


# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4! = 5 * 4 * 3 !
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1
# 1! = 1

# def factorial(number):
#     if number == 1:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
# print(factorial(1000))

# def show_symb_in_str(some_str: str):
#     if not some_str:
#         return 0
#     else:
#         # print(some_str[0],end= " ")
#         return 1 + show_symb_in_str(some_str[1:])
#
# print(show_symb_in_str("Denis"))
# closure
# def function(x):
#     def inner(x: int) -> None:
#         print(f"x:{x}")
#     inner(x)
#
#
# function(7)
# function(8)
# function(9)


# def get_name_for_greeting(name: str) -> callable:
#     def inner_greeting():
#         print(f"Hi, {name}")
#
#     return inner_greeting


# fun = get_name_for_greeting("Tom")
# fun()
# fun()
#
# def counter(number: int) -> callable:
#     def inner_count(x: int) -> int:
#         nonlocal number
#         number += 1
#         print(f"number = {number}")
#         return x + number
#
#     return inner_count
#
#
# f = counter(0)
#
# print(f(2))
# print(f(2))


# from datetime import datetime
#
#
# def modify_wake_up(fun: callable) -> callable:
#     def inner(name: str) -> str:
#         some_text = fun(name)
#         new_text = some_text + " " + str(datetime.utcnow())
#         return new_text
#     return inner
#
#
# def some_decorator(fun: callable) -> callable:
#     def inner(name: str):
#         print("start decorating")
#         some_text = fun(name)
#         print(some_text)
#         print("end decorating")
#     return inner
#
# @some_decorator
# @modify_wake_up
# def wake_up(name: str) -> str:
#     return f"Hey, {name} wake up!"


# # wake_up = some_decorator(modify_wake_up(wake_up))
# wake_up("Tom")

# print(wake_up("Tom"))



