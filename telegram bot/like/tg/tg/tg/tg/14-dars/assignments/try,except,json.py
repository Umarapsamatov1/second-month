# user_input = input("qiymatni kiriitng")
# try:
#     number=int(user_input)
#     print(f"siz kiritgan son: {number}")
# except ValueError:
#         print(f"faqat son kiritng")


#2-topshiriq

# try:
#      a=float(input("a= "))
#      b=float(input("b= "))
#
#      natija =a/b
#      print(f"natija= {natija}")
#
# except ZeroDivisionError:
#      print('xatolik: nolga bolish mumkin emas')
# except ValueError:
#     print("xatolik: faqat son kiriting")

#3-ttopshiriq
# fruits = ["apple", "banana", "orange", "kiwi"]
# try:
#    son=int(input("index : "))
#    print(f"natija: {fruits[son]}")
# except IndexError:
#    print("bunday indeksli element mavjud emas")
# except ValueError:
#     print("xatolik: indeks uchun faqat butun son kiriting")

#4-topshiriq
# def check_age(age):
#     try:
#         age = int(age)
#         if 7< age <=100:
#             return True
#         else:
#             return False
#     except ValueError,TypeError:
#         return False
#
#
# print(check_age("20"))
# print(check_age("salom"))

#5-topshiriq

# try:
#     with open("message.txt", "r", encoding="utf-8") as file:
#         message = file.read()
#         print(message)
# except FileNotFoundError:
#         print("fayl topilmadi")

#6-topshiriq

# student = {
# "name": "Ali",
# "age": 20,
# "course": "Python"
# }
#
# key=input("kalit:")
# try:
#     print(student[key])
# except KeyError:
#     print("bunday malumot mavjud emas")

#7-topshiriq






# import json
#
# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 25},
#     {"name": "Keyboard", "price": 70}
# ]
#
#
# with open("products.json", "w", encoding="utf-8") as file:
#     json.dump(products, file, indent=4)
#
#
# with open("products.json", "r", encoding="utf-8") as file:
#     loaded_products = json.load(file)
#
#
# for product in loaded_products:
#     print(product["name"])