from countryinfo import CountryInfo
import json
country_data = []



while True:
    country_name = input("davlat nomini kiriting")
    if country_name =="stop":
        print("dasturni to'xtatdingiz")
        with open("information.txt", mode="a", encoding="utf-8") as file:
            json.dump(country_data, file, indent=4, ensure_ascii=False)
            break

    try:
        get_country=CountryInfo(country_name)
        data = get_country.info()
        # print(data)
        name=data["name"]
        area=data["area"]
        borders=data["borders"]
        capital=data["capital"]
        currencies=data["currencies"]
        region=data["region"]
        languages=data["languages"]
        timezones=data["timezones"]
        population=data["population"]

        print(f"{name}davlati haqida ma'lumot\n "
              f"{name} davlati {region} qitasida joylashgan\n"
              f"{name} davlati {area} hududiga teng\n"
              f"chegaralari {borders} lar bilan chegaradosh\n"
              f"{name} davlatining poytaxti {capital}hisoblanadi va\n"
              f"pul birligi esa {currencies}\n"
              f"qabul qilingan tillari {languages}\n"
              f"vaqt birligi esa {timezones}\n"
              f"aholisi esa {population}\n")

        country_data.append({
            "name":name,
            "region":region,
            "area":area,
            "borders":borders,
            "capital":capital,
            "currencies":currencies,
            "languages":languages,
            "timezones":timezones,
            "population":population

        })

    except:
        print("siz davlat nomini notori kiritiz manimcha")


