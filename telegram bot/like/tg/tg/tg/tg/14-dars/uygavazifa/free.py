# rfhireivgh=int(input("raqam kirit"))
#
# print(f"keyingi {rfhireivgh+1}")
# print(f"keyingi {rfhireivgh-1}")



#
# oquvchi=50
# olma_soni=6
#
# oladi=oquvchi//olma_soni
# qoldi=oquvchi%olma_soni
# print(oladi)
# print(qoldi)

# def taqsimot(oquvchi,olmalar):
#     if olmalar<0:
#         print("0 dan katt son bolsin 1")
#     elif olmalar>0:
#         olinadigan_son=oquvchi//olmalar
#         qoladigani_son=oquvchi%olmalar
#         return olinadigan_son,qoladigani_son
#
# olma=6
# oquvchi=50
#
# lake,student=taqsimot(oquvchi,olma)
#
#
# print(f"oquvchi soni: {oquvchi}"
#       f"oquvchi oladigan soni:{lake}")


# # ==========================================
# # 1-MASALA: Olmalarni taqsimlash (def va if bilan)
# # ==========================================
# def olmalarni_taqsimla(oquvchilar_soni, olmalar_soni):
#     # Shart operatori yordamida tekshirish (if)
#     if oquvchilar_soni <= 0:
#         return "Xato: O'quvchilar soni noldan ko'p bo'lishi kerak!"
#
#     har_biriga = olmalar_soni // oquvchilar_soni
#     savatda_qoldi = olmalar_soni % oquvchilar_soni
#     return har_biriga, savatda_qoldi
#
#
# # Sinovdan o'tkazish
# o_soni = 6
# olma_soni = 50
#
# natija = olmalarni_taqsimla(o_soni, olma_soni)
#
# print("--- 1-MASALA NATIJASI ---")
# if type(natija) == str:
#     print(natija)
# else:
#     har_biriga, savatda_qoldi = natija
#     print(f"{o_soni} ta o'quvchi {olma_soni} ta olmani taqsimlasa:")
#     print(f"• Har bir o'quvchi oladi: {har_biriga} ta")
#     print(f"• Savatda qoladi: {savatda_qoldi} ta\n")
#
#
# # ==========================================
# # 2-MASALA: Sonlar yig'indisi (def va if bilan)
# # ==========================================
# def sonlar_yigindisini_hisobla(n):
#     # Shart operatori yordamida musbat son ekanligini tekshirish (if)
#     if n < 1:
#         return "Xato: Faqat musbat son (1 dan katta yoki teng) kiritilishi kerak!"
#
#     # 1 dan n gacha bo'lgan sonlar yig'indisi formulasi
#     summa = (n * (n + 1)) // 2
#     return summa
#
#
# print("--- 2-MASALA NATIJASI ---")
# try:
#     kiritilgan_n = int(input("Musbat sonni kiriting (n): "))
#
#     # Yana bir bor if orqali shartni tekshiramiz
#     if kiritilgan_n > 0:
#         javob = sonlar_yigindisini_hisobla(kiritilgan_n)
#         print(f"1 dan {kiritilgan_n} gacha bo'lgan sonlar yig'indisi: {javob}")
#     else:
#         print("Iltimos, 1 yoki undan katta musbat son kiriting!")
#
# except ValueError:
#     print("Xato! Faqat butun son kiritishingiz kerak.")

# while True:
#  s1=int(input("kirit: "))
#  s2=int(input("kirit: "))
#
#  if s1*s2 >= 1000:
#      print(s1+s2)
#
#  else:
#      print(s2*s1)
#      break

# son=int(input("sonni kiriting"))
# if son%5==0:
#     print("salom")
# else:
#     print("xayr")

# kabisa_kirit=int(input("yil kirit: "))
#
# if kabisa_kirit%4==0 and (kabisa_kirit%100!=0 or kabisa_kirit%400==0):
#     print("kabisa yili")
# else:
#     print("kabisa yilimas bu")
while True:
 it_yoshi=int(input("it yoshini kirit"))
 if it_yoshi<=0:
     print("xato yoshda musbat korinishida bolishi shart!")
 elif it_yoshi<=2:
     inson_yoshi=it_yoshi*10.5
     print(f"{it_yoshi} yil it yoshi odam yoshiga  nisbatan {inson_yoshi} ga togri keladi")
 else:
     inson_yoshi=2*10.5 + (it_yoshi -2) * 4
     print(f"{it_yoshi} itning yoshi insonikiga xisoblaganda {inson_yoshi} ga togri keladi")