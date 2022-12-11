my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

my_height_cm = round(my_height * 2.54)
my_weight_kg = round(my_weight * 0.45359237)

print(f"Let's talk about {my_name}.")
print(f"He's {my_height_cm} cm tall.")
print(f"He's {my_weight_kg} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height_cm + my_weight_kg
print(f"If i add {my_age}, {my_height_cm}cm, and {my_weight_kg}kg I get {total}.")
