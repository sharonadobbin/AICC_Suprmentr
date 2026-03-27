# Personalized Introduction Program

# Take user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your favorite hobby: ")

# Categorize age
if age < 13:
    age_group = "a child"
elif age < 20:
    age_group = "a teenager"
elif age < 60:
    age_group = "an adult"
else:
    age_group = "a senior"

# Print personalized message
print("\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are {age} years old, which means you are {age_group}.")
print(f"It's great that you enjoy {hobby}!")
print("Keep learning and having fun!")