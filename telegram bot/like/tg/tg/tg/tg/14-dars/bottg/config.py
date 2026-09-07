CATEGORIES = {
    "Smartfonlar": "uz/product/telefony-i-gadzhety/smartfony",
    "Konditsionerlar": "uz/product/klimaticheskaya-tehnika/kondicionery",
    "Kitoblar": "uz/product/knigi"
}

def get_values(category_name):
    return CATEGORIES.get(category_name)