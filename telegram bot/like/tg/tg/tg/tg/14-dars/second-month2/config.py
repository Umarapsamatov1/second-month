CATEGORIES={
    'smartphone ':'katalog/smartfon-samsung/',
    'kompyuter ':'katalog/vse-noutbuki',
    'konditsioner artel':'katalog/kondicionery-artel/'
}
def get_values(category):
    return CATEGORIES.get(category)