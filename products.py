# Здесь описаны напитки, которые можно приготовить и количество ингредиентов для их приготовления

def coffee(title):

    coffee_dictionary = \
        {
            'espresso': [1, 0, 0],
            'cappuccino': [1, 3, 0],
            'macchiato': [2, 1, 0],
            'viennese coffee': [1, 0, 2],
            'latte macchiato': [1, 2, 1],
            'con panna': [1, 0, 1]
        }

    key = title.lower()
    return coffee_dictionary[key]