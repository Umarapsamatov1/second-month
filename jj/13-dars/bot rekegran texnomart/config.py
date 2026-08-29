CATEGORIES={
    "telefon 📱": "katalog/smartfony-apple/",
    "televizor 📺": "katalog/televizor-samsung/",
    "laptop 💻": "katalog/huawei-3/",
    "oyinchoqlar 🧸": "katalog/konstruktory"

}
def get_values(category):
 # return CATEGORIES.get(category)
   for key,value in CATEGORIES.items():
       if key==category:
           return value