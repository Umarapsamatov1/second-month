#1-topshiriq
# numbers = [2, 4, 6, 8, 10]
#
# number=list(map(lambda x: x*2, numbers))
#
# print(number)
#2-topshiriq
# numbers = [1, 2, 3, 4, 5]
#
# number=list(map(lambda x: x**2, numbers))
#
# print(number)
from selectors import SelectSelector

#3-topshiriq
# names = ['ali', 'vali', 'hasan', 'husan']
#
# name=list(map(lambda x: x.upper(), names))
# print(name)

#4-topshiriq
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# number=list(filter(lambda x:x%2==0,numbers))
# print(number)

#5-topshiriq
# numbers = [-5, 3, -1, 8, 0, -7, 4]
# result=list(filter(lambda x:x>0,numbers))
# print(result)

#6-topshiriq
# words = ['olma', 'python', 'go', 'dasturlash', 'java']
#
# word=list(filter(lambda x: len(x)>5, words))
# print(word)

#7-topshiriq
# numbers = [5, 10, 15, 20]
#
# natija=list(map(lambda x:x+10, numbers))
# print(natija)
#------ standard daraja-------
#8-topshiriq
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# number=list(filter(lambda x:x%2==0,numbers))
# num=list(map(lambda x:x**2,number))
# print(num)
#9-topshiriq
#
# names = [' ali', 'VALI ', ' HaSaN ', 'husan']
# name=list(map(lambda x:x.strip().capitalize(),names))
# print(name)
#10-topshiriq

# products = [
#     {'name': 'Telefon', 'price': 3000000},
#     {'name': 'Sichqoncha', 'price': 150000},
#     {'name': 'Noutbuk', 'price': 7000000},
#     {'name': 'Klaviatura', 'price': 400000},
# ]
#
# product=list(filter(lambda x:x['price']>500000,products))
# resul=list(map(lambda x:{
#     'name':x['name'],
#     'price':int(x['price']*0.9)
# },product))
# print(resul)

#11-topshiriq
students = [
    {'name': 'Ali', 'score': 78},
    {'name': 'Vali', 'score': 45},
    {'name': 'Hasan', 'score': 92},
    {'name': 'Husan', 'score': 60},
    {'name': 'Sardor', 'score': 38},
]
res=list(filter(lambda x:x['score']>=60,students))
result=list(map(lambda x:{
    'name':x['name'],
    'score':x['score'],
    'grade':'A'if x['score']>=90 else
    'B'if x['score']>=70 else
    'C'
},res))
print(result)
