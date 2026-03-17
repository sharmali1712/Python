print("Welcome to the Interactive Personal Data Collector!\n")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height : "))
favorite_number = int(input("Please enter your favorite number: "))
current_year = 2026
birth_year = current_year - age
future_age = age + 5
print("\nPersonal Data")
print("Name:", name)
print("Age:", age)
print("Height:", height, "meterBhaveshs")
print("Favorite Number:", favorite_number)
print("\nBirth Year:", birth_year)
print("Your age after 5 years will be:", future_age)
print("\nThank you for using the Personal Data Collector!")
