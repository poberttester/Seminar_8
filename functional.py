import products
import inputProducts
# Здесь при наличии ингредиентов осуществляется приготовление напитков


ingredient = list(inputProducts.ingredients())


def choose_coffee(*preferences):
    global ingredient
    preference = list(preferences)


    for index, value in enumerate(preference):
        drink = products.coffee(value)
        new_product_list = []

        for index2, value2 in enumerate(ingredient):
            result = ingredient[index2] - drink[index2]
            new_product_list.append(result)

            if result >= 0:
                if index2 == len(ingredient)-1:
                    ingredient = new_product_list
                    return value
            else:
                break

    return 'К сожалению, не можем предложить Вам напиток'