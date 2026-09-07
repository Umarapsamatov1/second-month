#1-topshiriq
# def celsius_to_fahrenheit(celsius):
#       if not isinstance(celsius,(int,float)):
#           return "xatolik: xarorat son korinishida kiritilishi kerak"
#
#
#       fahrenheit = celsius * 9 / 5 + 32
#       return fahrenheit
#
# print(celsius_to_fahrenheit(25))
#2-topshiriq
# def harf_soni(matn,harf):
# #     if not isinstance(matn,str) or not isinstance(harf,str):
# #         return "xatolik: matn va xarf kiriitlishi kerak"
# #     matn=matn.lower()
# #     harf=harf.lower()
#                 return matn.count(harf)
# print(harf_soni("Dasturlash", "a"))
# 3-topshiriq
# def raqamlar_yigindisi(son):
#     if not isinstance(son, int) or son < 0:
#         return "xatolik: musbat son kiriting"
#     yigindi=0
#     for raqam in str(son):
#         yigindi+=int(raqam)
#
#     return yigindi
#
# print(raqamlar_yigindisi(582))
#4-topshiriq
# def parol_tekshir(parol):
#     if not isinstance(parol,str):
#         return "xatolik:parol matn korinishida bo'lishi kerak !"
#     uzunlik_yetarli=len(parol)>=8
#     raqam_bor = any(char.isdigit() for char in parol)
#     katta_harf=any(char.isupper() for char in parol)
#
#     if uzunlik_yetarli and raqam_bor and katta_harf:
#         return "kuchli parol"
#     else:
#         return "kuchsiz parol"
# print(parol_tekshir("Salom123"))
# print(parol_tekshir("Salom"))
#5-topshiriq
# def musbat_sonlar(son):
#     if not isinstance(son,list):
#         return "xatolik:list kirinting"
#
#     yangi_royhat=[]
#     for n in son:
#         if isinstance(n,(int,float))and  n>0:
#             yangi_royhat.append(n)
#     return yangi_royhat
#
# son = [-4, 10, 0, -2, 7, 8]
# print(musbat_sonlar(son))
#6-topshiriq
# def eng_uzun_soz(gap):
#     if not isinstance (gap, str):
#         return "xatolik:matn kiritilsin"
#
#     sozlar=gap.split()
#     if not sozlar:
#         return "gap bo'sh"
#
#     eng_uzun=sozlar[0]
#
#     for soz in sozlar:
#         if len(soz)>len(eng_uzun):
#             eng_uzun=soz
#
#     return eng_uzun
#
#
# print(eng_uzun_soz("Python dasturlash juda qiziqarli"))
#7-topshiriq
# def chegirma_hisobla(narx,chegirma):
#     if narx<0:
#         return "narx manfiy son bolishi mumkin emas"
#     if chegirma<=0 or chegirma>=100:
#         return "noto'gri chegirma"
#     yangi_narx = narx -(narx*chegirma/100)
#     return int(yangi_narx)
# print(chegirma_hisobla(200000, 15))