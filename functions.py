from data import calories, combos



def calorie_counter(order):
    x=0
    for i in order:
        x = x + order[i]
    return x


def order_combo(combo_name):
    total_calories=0
    if combo_name in combos:
        combo_items = combos[combo_name]
        total_calories = sum(calories[item] for item in combo_items)
        print(f"Ordered {combo_name}:")
        for item in combo_items:
            print(f"- {item}: {calories[item]} calories")
        print(f"Total Calories: {total_calories} calories")
    else:
        print(f"Combo {combo_name} is not available.")
        return total_calories
    


def combo_calories_counter (ordered_item):
    total_calories=0
    for meal in ordered_item:
        if meal in calories:
            total_calories= total_calories + calories[meal]
        elif meal in combos:
            combo_items= combos[meal]
            total_calories= total_calories + sum(calories[item]for item in combo_items)
        else:
            print(f"{meal} is not in the calorie database or is not a valid combo.")
    return total_calories




def combo_calories_counter2 (ordered_item):
    total_calories=0
    for meal in ordered_item:
        try:
            if meal in calories:
               total_calories= total_calories + calories[meal]
            elif meal in combos:
                combo_items= combos[meal]
                total_calories= total_calories + sum(calories[item]for item in combo_items)
            else:
                raise KeyError
        except KeyError:
            print( print(f"The item '{meal}' is not on the menu."))
    return total_calories



def calculate_total_price(ordered_items, meals_dict, combos_dict):
    total_price = 0
    for item in ordered_items:
        try:
            if item in meals_dict:
                total_price += meals_dict[item]["price"]
            elif item in combos_dict:
                total_price += combos_dict[item]["price"]
            else:
                raise KeyError
        except KeyError:
            print(f"{item} is not in the menu.")
    return total_price

