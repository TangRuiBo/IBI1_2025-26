class FoodItem:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def daily_nutrition_summary(food_list):
    total_cal = 0
    total_pro = 0
    total_car = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_car += food.carbs
        total_fat += food.fat

   
    print("=" * 40)
    print("24-hour Nutrition Intake Statistics")
    print("=" * 40)
    print(f"total_cal：{total_cal} kcal")
    print(f"total_protein：{total_pro} g")
    print(f"total_carbohydrate：{total_car} g")
    print(f"total_fat：{total_fat} g")

    
    warning = []
    if total_cal > 2500:
        warning.append("⚠️ Calorie over limit（>2500）")
    if total_fat > 90:
        warning.append("⚠️ Fat over limit（>90g）")

    if warning:
        print("\nWanring：" + " | ".join(warning))
    else:
        print("\n✅ Nutrient intake is normal")

    return { "calories": total_cal,
             "protein": total_pro,
             "carbs": total_car,
             "fat": total_fat    }


if __name__ == "__main__":

    breakfast = FoodItem("Whole wheat bread and eggs", 450, 20, 50, 15)
    lunch = FoodItem("Rice Chicken and breast", 700, 40, 90, 10)
    dinner = FoodItem("Steak and Vegetables", 900, 50, 30, 45)
    snack = FoodItem("nut", 600, 15, 20, 50)

    daily_food = [breakfast, lunch, dinner, snack]

    daily_nutrition_summary(daily_food)
