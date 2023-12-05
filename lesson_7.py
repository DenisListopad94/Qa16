# def get_student_info(*marks, name: str = "Oleg", age: int = None, **professors) -> str:
#     """
#     get info about student
#     name  -> student name
#     age -> age of student
#     """
#     info_student = f"name: {name} age: {age} marks: {marks} professors: {professors}"
#     return info_student
#
#
# print(get_student_info(5, 2, 6, 1, 2, name="Denis", age=25, math="Filipov", phys="Markov"))
# import time
#
#
# def decorator_function(func: callable) -> callable:
#     def wrapper(number: int):
#         start = time.time()
#         func(number)
#         end = time.time()
#         print('время выполнения {}, Функция протестирована: {}'.format(end - start, func.__name__))
#
#     return wrapper
#
#
# @decorator_function
# def appear_numbers(number: int) -> None:
#     for num in range(2, number + 1):
#         is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
#         if is_prime:
#             print(num, end=" ")
#     print()
#
#
# # appear_numbers = decorator_function(appear_numbers)
# appear_numbers(50)

# def some_fun(marks: tuple = ()):
#     marks = list(marks)
#     marks.append(3)
#     print(marks)
#
# some_fun()
# some_fun()
# some_fun()


# exceptions

# print(NameError.__bases__[0].__bases__[0].__bases__)
# print(type(5).__bases__)

# def division_function(numb_1: int, numb_2: int) -> float:
#     return numb_1 / numb_2
#
#
# try:
#     print(division_function(numb_1=5, numb_2=0))
# except NameError:
#     print("NameError:(")
# except ZeroDivisionError:
#     print("ZeroDivisionError:(")
# except Exception as e:
#     print("some exception:(")
#     print(type(e))
# else:
#     print("all good")
# finally:
#     print("always")


# def registration() -> None:
#     name = input("enter your name in upper case:")
#     password = input("enter difficult password, min 4 sign")
#     if not name.isupper():
#         raise ValueError(f"name: {name} in not in upper case")
#     if len(password) < 4:
#         raise ArithmeticError(f"password:{password}  must be min 4 sign")
#
#
# while True:
#     try:
#         registration()
#     except ValueError as e:
#         print(e)
#         print("put data:")
#         continue
#     except ArithmeticError as e:
#         print(e)
#         print("put data:")
#         continue
#     else:
#         print("hello user")
#         break

# file = None

# def file_work():
#     file = open(file="test.txt", mode="a",encoding="utf-8")
#     file.write("привет мир\n")
#     file.write(str(27))
#
# try:
#     file_work()
# except FileExistsError:
#     print("error")
# finally:
#     file.close()

# file = open(file="test.txt",encoding="utf-8")
# data = file.read().split("\n")
# data = [int(item) for item in data] #list(map(int,data))
# print(sum(data)/len(data))
# file.close()

# ages = []
# file = open(file="test.txt",encoding="utf-8")
# for line in file:
#     ages.append(int(line.rstrip()))
# # data = file.readline()
# # print(data)
# print(ages)
# file.close()

# ages = []
# def read_data():
#     with open(file="test.txt",encoding="utf-8") as file:
#         counter = 0
#         for line in file:
#             if counter == 3:
#                 raise ValueError
#             ages.append(int(line.rstrip()))
#             counter += 1
#
# try:
#     read_data()
# except Exception:
#     print("sorry ;(")
# finally:
#     print(ages)
# f = open("bin_file.bin", "wb")
# num = [5, 10, 15, 20, 25]
# arr = bytearray(num)
# f.write(arr)
# f.close()
#
# import pickle
# FILENAME = "user.dat"
# with open(FILENAME, "rb") as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
# print("Имя:", name, "\tВозраст:", age)

# import os
#
# os.remove("bin_file.bin")

# import json
#
# student_info = {
#     "name": "Oleg",
#     "age": 27
# }

# with open("student.json","w") as file:
#     json.dump(student_info,file)

# with open("student.json") as file:
#     data = json.load(file)
#
# import json
# from datetime import datetime
#
# current_date = datetime.now()
#
# with open("goods.json") as json_file:
#     goods = json.load(json_file)
#
# for info_good in goods["goods"]:
#
#     date_data = datetime(*list(map(int, info_good["date"].split("-"))))
#
#     if info_good["cost"] > 1000000:
#         print(info_good)
#
#     elif int(str(current_date - date_data).split()[0]) > 30:
#         print(info_good)
