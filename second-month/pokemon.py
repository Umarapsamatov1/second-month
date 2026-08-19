import json
import requests

# Izlangan pokemonlar ro'yxatini saqlash uchun list
pokemons_list = []

print("=== Pokemon qidirish dasturi ===")
print("Dasturni to'xtatish uchun 'stop' deb yozing.\n")

while True:
    # 1. Foydalanuvchidan nom olish
    pokemon_name = input("Pokemon nomini kiriting: ").strip().lower()

    # 'stop' kiritilsa sikldan chiqish
    if pokemon_name == "stop":
        print("\nDastur to'xtatildi.")
        break

    # Bo'sh qiymat kiritilsa o'tkazib yuborish
    if not pokemon_name:
        continue

    # API manzili
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    try:
        # 2. API'ga so'rov yuborish
        response = requests.get(url)

        # Agar pokemon topilmasa (404 va b.), xatolik keltirib chiqarish
        response.raise_for_status()

        # JSON ma'lumotni lug'atga aylantirish
        data = response.json()

        # 3. Kerakli ma'lumotlarni ajratib olish
        name = data["name"].capitalize()
        poke_id = data["id"]
        height = data["height"]
        weight = data["weight"]

        # Turi (bir nechta turi bo'lishi mumkin)
        types = [t["type"]["name"] for t in data["types"]]
        types_str = ", ".join(types)

        # BONUS: Qobiliyatlari (abilities)
        abilities = [a["ability"]["name"] for a in data["abilities"]]
        abilities_str = ", ".join(abilities)

        # Konsolga chiqarish
        print(f"Nomi: {name}")
        print(f"ID: {poke_id}")
        print(f"Bo'yi: {height}")
        print(f"Og'irligi: {weight}")
        print(f"Turi: {types_str}")
        print(f"Qobiliyatlari: {abilities_str}\n")

        # 4. Natijani dict ko'rinishida shakllantirish va listga qo'shish
        pokemon_info = {
            "name": data["name"],
            "id": poke_id,
            "height": height,
            "weight": weight,
            "type": types_str,
            "abilities": abilities,
        }
        pokemons_list.append(pokemon_info)

    except requests.exceptions.HTTPError:
        print("❌ Bunday Pokemon topilmadi! Qaytadan urinib ko'ring.\n")
    except requests.exceptions.RequestException as e:
        print(f"❌ Tarmoqda xatolik yuz berdi: {e}\n")

# 5. Sikl tugagach, barcha ma'lumotlarni JSON faylga saqlash
if pokemons_list:
    with open("pokemons.json", "w", encoding="utf-8") as file:
        json.dump(pokemons_list, file, indent=4)
    print("✅ Barcha natijalar 'pokemons.json' fayliga saqlandi!")
else:
    print("Hech qanday ma'lumot saqlanmadi.")
