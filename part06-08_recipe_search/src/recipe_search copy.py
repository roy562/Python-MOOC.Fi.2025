# Write your solution here
def read_file(filename: str):
    recipes = []
    recipe = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                recipes.append(recipe)
                recipe = []
                continue
            else:
                recipe.append(line)
        recipes.append(recipe)
    #print(recipes)
    return recipes 

def search_by_name(filename: str, word: str):
    file_recipes = read_file(filename)
    matched_recipe_names = []
    for row in file_recipes:
        if word.lower() in row[0].lower():
            matched_recipe_names.append(row[0])
    
    return matched_recipe_names

def search_by_time(filename: str, prep_time: int):
    file_recipes = read_file(filename)
    matched_recipe_names = []
    recipe_with_prep_time = ""
    for row in file_recipes:
        if int(row[1]) <= prep_time:
            recipe_with_prep_time = f"{row[0]}, preparation time {row[1]} min" 
            matched_recipe_names.append(recipe_with_prep_time)
    
    return matched_recipe_names

def search_by_ingredient(filename: str, ingredient: str):
    file_recipes = read_file(filename)
    matched_recipe_names = []
    recipe_with_prep_time = ""
    
    for row in file_recipes:
        ingredient_exists = False
        recipe_with_prep_time = f"{row[0]}, preparation time {row[1]} min" 
        
        for ing in row[2:]:
            if ingredient.lower() == ing.lower():
                ingredient_exists = True
        
        if ingredient_exists:
            matched_recipe_names.append(recipe_with_prep_time)
    
    return matched_recipe_names

#found_recipes = search_by_name("recipes1.txt", "cake")

#for recipe in found_recipes:
    print(recipe)

#found_recipes = search_by_time("recipes1.txt", 20)

#for recipe in found_recipes:
    print(recipe)

#found_recipes = search_by_ingredient("recipes1.txt", "eggs")

#for recipe in found_recipes:
    print(recipe)

#print(read_file('recipes1.txt'))