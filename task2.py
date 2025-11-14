def read_cook_book(filename):
    cook_book = {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            name = file.readline().strip()
            if not name:
                break
            
            ingredient_count = int(file.readline().strip())
            ingredients = []
            
            for _ in range(ingredient_count):
                ingredient = file.readline().strip().split(' | ')
                ingredient_name = ingredient[0]
                quantity = int(ingredient[1])
                measure = ingredient[2]
                
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            
            cook_book[name] = ingredients
            file.readline()
    
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book('food.txt')
    res = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for k in ingredients:
            qnt = 0
            if k['ingredient_name'] in res:
                qnt = res[k['ingredient_name']]['quantity']
            
            res[k['ingredient_name']] = {'measure': k['measure'], 'quantity': k['quantity'] * person_count + qnt}
            pass
        
        pass
    return res




print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))