# 2133915
# Alan Do

class FoodItem():
    def __init__(self,item_name="None",grams_fat=0,grams_carbs=0,grams_protein=0):
        self.name = item_name
        self.fat = grams_fat
        self.carbs = grams_carbs
        self.protein = grams_protein

    def get_calories(self, num_servings):
    # Calorie formula
      calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
      return calories

    def print_info(self):
      print('Nutritional information per serving of {}:'.format(self.name))
      print('   Fat: {:.2f} g'.format(self.fat))
      print('   Carbohydrates: {:.2f} g'.format(self.carbs))
      print('   Protein: {:.2f} g'.format(self.protein))
     


if __name__ == "__main__":
   
   fooditem1 = FoodItem()
   item_name = input()
   amount_fat = float(input())
   amount_carbs = float(input())
   amount_protein = float(input())
   fooditem2 = FoodItem(item_name,amount_fat,amount_carbs,amount_protein)
   num_servings = float(input())
   fooditem1.print_info()
   print(f"Number of calories for {num_servings} serving(s): 0.00")
   print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, food_item2.get_calories(num_servings)))
