# import math
#
# age_tom = 0
# name = ""
# #          0      1
# names = [""]
# print(math.radians(180))


# строки не изменяемы!!! unmutable

# print(id(name))
# surname = "Redle"
# name = name + " " + surname
#
# name[0] = "R"
#
# full_name = "Tom Reddle"

# print(full_name[-4])
# # срезы/slice
# # [start:stop:step]
# print(full_name[:4])
# print(full_name[4:])
# print(full_name[:])
# print(full_name[::-2])
#
# print(id(full_name))
#         -4    -3      -2     -1
#          0     1       2      3
# names = ["Tom","Peter","Max","Alice"]
# # ages = list()
# # print(names[::-2])
# # print(ages)
# names.append("Petya")
# names.append("Petya")
#
# names.insert(0,"Grisha")
# print(names)
# names.remove("Petya")
# names.pop(3)
#
# names.sort(reverse=True)
# print(names)
# print(names)
# print(names.count("Toma"))
# names.reverse()
# print(names)
#
# names.extend(["Anna","Kate"])
# print(names)
# print(names.index("Anna"))
#
# data = [5,2,6,[4,1,2,[5,2,6]]]
# data[3].extend([52,12,2])
# print(data)
# print(names.__sizeof__())
# print(names)
# names[0] =  "Anna"
# print(names*3)
# lst_1 = []
# lst_2 = [1,2]
# print(lst_1 is None)

# friends_numbers = {"Tom": "378211241", "Mary": "748217412", "Pit": "4271848125"}
# friends_numbers.update({"Kate":"72481412","Peter":"5125124112"})
# dct = dict(**friends_numbers)
# print(dct)
#
#
# product = {
#     "banana":{
#         "price":4.21,
#         "vendors": [
#             {"country":"Ecvador","price":4.21},
#             "SAR"]
#     },
#     "apple":{
#         "price":2.21,
#         "vendor": ["Belarus","Poland"]
#     }
# }
# print(product["banana"])
# friends_numbers["Tom"] = "47218412"
# friends_numbers["Kate"] = "41251252"
# # friends_numbers.pop("Tom")
# # del friends_numbers["Tom"]
#
# print(friends_numbers["Tom"])
# print(friends_numbers)

# friends = ("Tom", "Kate", "Peter", "Tom",)
# friends_2 = ("Mary",)
# print(type(friends_2))
# friends.add("Mary")
# friends.add(5)
# friends.add(-5)
#
# # friends.remove("Max")
# friends.clear()
# # name = friends.pop()
# print(friends)

# school = {"9a": 23, "9b": 25}
# print(sum(school.values()))

# some_str = "sdafasdasfasdsafasd"
# first_ind_f = some_str.find("f")
# print(some_str.find("f", first_ind_f + 1))

# from math import ceil
#
# height = 10
# up = 3
# down = 2
# print(ceil((height-up)/(up-down)) + 1)
# print()

# #      0    1      2     3       4          5
# tup = (4, "524", 6.21, True, (4, 1, 6), [6, 2, 6])
# tup[5].pop()
# tup2 = 9,9
# print(tup2)
# lst = list(tup2)
# print(lst)
# fr_set = set(lst)
# print(fr_set)

# int float str set dict list tuple frozenset
# numb1 = [1]
# numb2 = [1]
# print(numb1 is numb2)"
# some_str = "hello world"
# sub_str = "hell"
# lst = [5,2,6,2,1]
# print(7 not in lst)

# print(sub_str in some_str)

# age = 25
#
# print(not age <= 24)

# number = 330
#
# #  True/False
# if number > 0:
#     print("positive")
#     if number >= 10 and not (number < 100 or exp):
#         print("двузначное")
#     if number >= 100 and number < 1000:
#         print("трёхзначное")
# elif number == 0:

#     print("zero")
# else:
#     print("negative")

# number = 5
#
# lst = []
# if lst:
#     print("number not equal 0")
# тернарный оператор
# number = 2
# print("positive" if number > 0 else "not positive")
# range(start,end,step)
# range(start,end) step = 1
# range(end) start = 0 step = 1
# for var in range(5,10,-1):#итерируемый объект
#     print(var)
#           01
# some_str = "hello world"
# some_lst = [4,2,6,1,7]
# for ind in range(len(some_lst)):
#     if some_lst[ind] % 2 == 0:
#         print(ind,some_lst[ind])

# n = 1412
# while n:
#     print(n % 10)
#     n //= 10
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
# school = {"9a": 45, "9b": 21, "9c": 27,"9d": 30}

# for key in school:
#     print(key,school[key])

# for key, value in school.items():
#     if value > 20:
#         print(key,value)
#     else:
#         break
# else:
#     print("some text")
# print("ds",5,sep="\n",end="/")
# print(5)

# val,val2,val3 = int(input("enter val:")),int(input("enter val2:")),int(input("enter val3:"))
# l = set(map(int,input("enter values").split()))
# print(l)
# print(l)

# number = int(input("введите число:"))
#
# for numb in range(2, number // 2 + 1):
#     if not number % numb:
#         print("составное")
#         break
# else:
#     print("простое")
#
# 17.	Дан текст. Слова в тексте разделены одним или несколькими пробелами.
# Написать программу выводящую все различные слова текста.
#
# text = "h6h ihah pyd 5eh    po   op  hah hehe" + " "
# buf = ""
# some_set = set()
# for ind in range(len(text)):
#     if text[ind] != " ":
#         buf += text[ind]
#     # elif not buf:
#     #     continue
#     else:
#         if buf and buf not in some_set:
#             if buf[0] not in "aeuioy"  and buf.isalpha():
#                 print(buf)
#             some_set.add(buf)
#         buf = ""


# lst = text.split()
# print(set(lst))
#
# 8.	Задан список из k чисел. Определить количество инверсий в списке
# (т. е. таких пар элементов, в которых большее число находится слева от меньшего).

# lst = [5, 2, 7, 9, 8, 19, 5]
# counter = 0
# for ind in range(len(lst) - 1):
#     if lst[ind] > lst[ind + 1]:
#         counter += 1
# print(counter)

# str_new = "".join(some_str)

# some_str = input("enter str:")
# buf = ""
# for symb in some_str:
#     if symb not in buf:
#         buf += symb
#
# print(buf)
#
# some_str = input("enter str:")
#
# for ind in range(len(some_str)):
#     if some_str[ind] not in some_str[:ind]:
#         print(some_str[ind],end="")

# # import random
# from random import randint as rndt
#
# print(rndt(1,18))
# def hello():
#     return "hello"
#
#
# # import math
# from math import (
#     sin,cos,
#     tan,factorial
# )
#
#
# print(sin(60))
# print(cos(50))
