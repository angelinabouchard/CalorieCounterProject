calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}







# EXERCISE 4

meals_list = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7
    },
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6
    },
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6
    },
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3
    },
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4
    },
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2
    },
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
    }
]














meals_list = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7
    },
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6
    },
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6
    },
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3
    },
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4
    },
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2
    },
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
    }
]

combos_list = [
    {
        "id": "combo-1",
        "name": "cheesy combo",
        "meals": ["meal-2", "meal-5", "meal-8"],
        "price": 11,
    },
    {
        "id": "combo-2",
        "name": "veggie combo",
        "meals": ["meal-3", "meal-5", "meal-7"],
        "price": 10,
    },
    {
        "id": "combo-3",
        "name": "vegan combo",
        "meals": ["meal-4", "meal-6", "meal-8"],
        "price": 10,
    }
]


meals_dict = {
	meals["id"]: meals
	for meals in meals_list
}


combos_dict = {
    combos["id"]: combos
    for combos in combos_list
}
