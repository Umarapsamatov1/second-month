# 1-topshiriq

# def max_son():
# def max_son(a,b,c):
#     if a>b and a>c:
#         return a
#     if b>a and b>c:
#         return b
#     else:
#         return c
# print(max_son(300,40,30))
#2-topshiriq
# def yigindi(nums):
#     total = 0
#     for n in nums:
#         total += n
#     return total
#
# print(yigindi([1,2,3,4,5,6]))
#3-topshiriq
# def kopaytma(nums):
#     total = 1
#     for n in nums:
#         total *= n
#     return total
#
# print(kopaytma([8,2,3, -1, 7]))
#4-topshiriq
# def teskari(matn):
#     return matn[::-1]
#
# print(teskari("1234abcd"))
#5-topshiriq
# def harf_soni(matn):
#     katta = 0
#     kichik = 0
#     for char in matn:
#         if char.isupper():
#             katta += 1
#         elif char.islower():
#             kichik += 1
#     return f"katta harflar: {katta} ta, kichik harflar: {kichik} ta"
#
# print(harf_soni("The quick Brow Fox"))
#6-topshiriq
# def palindrom(soz):
#     soz=str(soz).lower()
#
#     if soz == soz[::-1]:
#         return "panidrom"
#     else:
#         return "palindrom emas "
#
# print(palindrom("kazak"))
# print(palindrom("salom"))
#7-topshiriq
# def bank(summa,yil):
#    for i in range(yil):
#        summa = summa *1.10
#    return summa
# print(bank(1000,2))
#8-topshiriq
# def bolinadi_15(nums):
#     result=[]
#     for n in nums:
#         if n % 15 == 0:
#               result.append(n)
#     return result
#
# nums = [45, 55, 60, 37, 100, 105, 220]
# print(bolinadi_15(nums))






