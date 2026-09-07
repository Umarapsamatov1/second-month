CATEGORIES = {
    'Smartfon 📱': 'katalog/smartfony-apple/',
    'HP 💻': 'katalog/noutbuki-hp/',
    'Artel 🖥': 'katalog/televizory-artel-shivaki/',
    "O'yinchoqlar 🧸": 'katalog/konstruktory/',
}


def get_values(category):
    for key, values in CATEGORIES.items():
        if key == category:
            return values
