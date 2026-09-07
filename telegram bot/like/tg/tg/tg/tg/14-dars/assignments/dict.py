#  1-topshiriq
# shaxarlar ={
#     "moskva": (550, 370),
#     "london": (510, 510),
#     "parij": (480, 480),
#
#
# }
# moskva = shaxarlar["moskva"]
# london = shaxarlar["london"]
# parij = shaxarlar["parij"]
#
# masofalar ={}
#
# masofalar["moskva-london"] = ((moskva[0]-london[0])**2 + (moskva[1]-london[1])**2)**0.5
#
# masofalar["moskva-parij"] = ((moskva[0]-parij[0])**2 + (moskva[1]-parij[1])**2)**0.5
#
# masofalar["london-parij"] = ((london[0]-parij[0])**2 + (london[1]-parij[1])**2)**0.5
#
# print(masofalar)
from mimetypes import init

#2-topshiriq

# mahsulotlar={"olma":5000, "banan":12000, "uzum":8000, "nok":15000}
#
# yigindi=sum(mahsulotlar.values())
#
# soni=len(mahsulotlar)
#
# ortacha=yigindi/soni
#
# print("yigindi:",yigindi)
# print("arifmetik o'rtacha:",ortacha)
#3-topshiriq
# n=int(input("n sonini kiriitng"))
#
# kvadratlar={}
# for x in range(1,n+1):
#     kvadratlar[x]=x * x
#
# print(kvadratlar)
#4-topshiriq
# kalitlar =['ism', 'yosh', 'shaxar']
# qiymatlar = ['ali', 20, 'toshkent']
#
# lugat =dict(zip(kalitlar,qiymatlar))
#
# print(lugat)
#5-topshiriq
# lugat1 ={'a': 1, 'b': 2}
# lugat2={'c': 3, 'd': 4}
#
# lugat3=lugat1 | lugat2
# print(lugat3)

# daraja --- pro

#6-topshiriq

# mahsulotlar={
#    '23456':[
#        {"miqdori": 22, "narx":510},
#        {"miqdori":32, "narx":520}
#    ] ,
#
#       '34567': [
#           {"miqdori":2, "narxi":1200},
#           {"miqdori":1, "narxi":1150}
#       ] ,
#     '45678':[
#         {"miqdori":50, "narxi":100},
#         {"miqdori":12, "narxi":95},
#         {"miqdori":43, "narxi":97}
#     ]
# }
# for toifa, partiyalar in mahsulotlar.items():
#     jami_soni=0
#     jami_narxi=0
#
#     for partiya in partiyalar:
#         miqdor = partiya["miqdori"]
#
#         narx=partiya.get("narx") or partiya.get("narxi")
#
#         jami_soni+= miqdor
#
#         jami_narxi += miqdor * narx
#
#     print(f"toifa: {toifa}")
#     print(f"   - umumiy mahsulotlar soni: {jami_soni} ta")
#     print(f"   -mahsulotlarning umumiy narxi: {jami_narxi} so'm\n")
