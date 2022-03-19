def dishes_dict(file):
    with open(file, encoding = 'utf-8') as f:
        file = f.readlines()
        dict = {}
        for i in range(file.count('\n')):
            index = file.index('\n')
            dish = file[:index]
            del(file[:index+1])
            dish_name = list(dish)[0]
            dish_name = dish_name[:dish_name.index('\n')]
            ingredients = dish[2:]
            dict[dish_name] = []
            for ingredient in ingredients:
                ingredient = ingredient.split('|')
                ingredient_name = ingredient[0]
                quantity = ingredient[1]
                measure = ingredient[2]
                measure = measure[:measure.index('\n')]
                dict[dish_name].append({'ingredient_name':ingredient_name, 'quantity':quantity, 'measure': measure})
    return dict

def get_shop_list_by_dishes(dishes, person_count):
    dict = {}
    for dish in dishes:
        if dish in dishes_dict('блюда.txt'):
            for ingridients in dishes_dict('блюда.txt')[dish]:
                ingridient = ingridients['ingredient_name']
                quantity = ingridients['quantity']
                measure = ingridients['measure']
                dict[ingridient] = {'quantity':int(quantity)*person_count,'measure': measure}
    return dict

print(dishes_dict('блюда.txt'))