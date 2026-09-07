#1-topshiriq
# i=1
# while i<11:
#     print(i)
#     i=i+1
# #2-topshiriq
# i=10
# while i>=1:
#     print(i)
#     i-=1
#3-topshiriq
# i=2
# while i<102:
#     print(i)
#     i+=2
# 4-topshiriq
# n=int(input("son kiriting"))
# yigindi=0
# i=1   
# while i<=n:
#     yigindi+=i
#     i+=1
#     print(yigindi)
# 5-topshiriq
# n=int(input("son kiriting"))
# faktarial = 1
# i = 1
# while i <= n:
#     faktarial *= i
#     i+=1
#
# print(faktarial)
#6-topshiriq


# while True:
#     parol = input("parolni kirititng")
#     if parol == "python123":
#         print("parol to'gri")
#         break
#     else:
#         print("parol notogri")
#         continue
#7-topshiriq
# while True:
#     raqam =float(input("musbat raqam kiritng "))
#     if raqam >0:
#         print("musbat son to'gri ")
#         break
#     else:
#         print("bu manfiy son !")
#8-topshiriq
# while True:
#     print("\n---menyu---")
#     print("1-qo'shish\n2-ayirish\n3-ko'paytirish\n4-bo'lish\n0-chiqish")
#
#     son=input("sonni kiriitng 0-4")
#     if son=="0":
#         print("siz dasturdan chiqdingiz")
#         break
#
#     elif son in ["1", "2", "3", "4"]:
#         a=float(input("birinchi sonni kiriitng"))
#         b=float(input("ikkinchi sonni kiriitng"))
#
#         if son=="1":
#             print(f"natija:{a+b}")
#         elif son=="2":
#             print(f"natija:{a-b}")
#         elif son=="3":
#                 print(f"natija:{a*b}")
#         elif son=="4":
#                 print(f"natija:{a//b}")
#         else:
#             print("nolga bolish mumkin emas")
#     else:
#         print("noto'gri tanlov")
#9-topshiriq
# while True:
#     son=int(input("son kiritng"))
#     if son==27:
#         print("siz to'gri son kiritdingiz va yutdingiz !")
#         break
#     elif son<27:
#         print("kattaroq son kiriting")
#         continue
#     elif son>27:
#         print("kichikroq son kiriting")
#         continue
#     else:
#         pass
#10-topshiriq
# balans=50000
# print("\n---bankomat---")
# print("1 - Balansni ko'rish\n2 - Pul yechish\n3 - Pul qo'shish\n0 - Chiqish")
# n=input("menyu orqali buyruq tanlang")
# while True:
#     if n == "1":
#         print(f"Balans: {balans} so'm")
#         break
#
#     elif n == "2":
#         mablag = int(input("Yechmoqchi bo'lgan summani kiriting: "))
#
#         if mablag > balans:
#             print("Balansda buncha pul yo'q")
#         elif mablag <= 0:
#             print("Xato summa kiritildi")
#         else:
#             balans -= mablag
#             print(f"Muvaffaqiyatli yechildi. Qoldiq: {balans} so'm")
#     elif n == "3":
#             pul=int(input("qoshiladigan pulni kiriting: "))
#             if pul > 0:
#                   balans+=pul
#                   print(f" {pul}so'm Muvaffaqiyatli qo'shildi qoldiq {balans} so'm")
#             else:
#                 print("noto'gri summa")
#     elif n == "0":
#         print("dasturdan chiqdingiz")
#         break
#     else:
#         print("notogri buruq kiritildi")
#         break











