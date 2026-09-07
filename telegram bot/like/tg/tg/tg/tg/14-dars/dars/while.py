# i = 1
# while i :
#     print(i)
#     i += 1

# while True:
#     n =int(input("enter a number"))
#     if n==77:
#         print("siz 77 kiritdingiz va dasturni to'xtatdingiz")
#         break
#     print(f"siz {n} sonini kiritdingiz !")
products = ["banan ", "olma", "sichqoncha", "nok"]

while True:
    user_text = input(" mahsulot kiriting")
    if user_text.lower() == "stop":
        print(" siz dasturni toxtatdingiz")
        break

    if len(user_text.split(' ')) == 2:
        command, product = user_text.split(' ')

        if command == "add":
            if product in products:
                print(f"{product} bor {products}ni ichida")
            else:
              products.append(product)
            print(f"{product} qo'shildi {products}ni ichiga")

        if command == "delete":
            if product in products:
                products.remove(product)
                print(f"{product} olib tashlandi qolgan narsalar: {products}")
            else:
                print(f"{product} royhatni ichida yo'q")

