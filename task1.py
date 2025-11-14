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


cook_book = read_cook_book('food.txt')
print(cook_book)