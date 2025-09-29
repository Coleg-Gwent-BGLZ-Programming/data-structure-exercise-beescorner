# Step 1: Collect user info
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Step 2: Collect hobbies using a loop
hobbies = set()  # Using a set to ensure uniqueness
print("Enter your hobbies one by one. Type 'done' when finished:")
while True:
    hobby = input("Hobby: ")
    if hobby.lower() == 'done':
        break
    hobbies.add(hobby.strip())

# Step 3: Store fixed data in a tuple
birth_year = int(input("Enter your birth year: "))
current_year = 2025
year_data = (birth_year, current_year)  # Tuple for fixed data

# Step 4: Store user data in a dictionary
user_data = {
    "name": name,
    "age": age,
    "hobbies": list(hobbies),  # Convert set to list for display
    "birth_year": year_data[0],
    "current_year": year_data[1]
}

# Step 5: Display the data using formatted strings
print("\n User Summary:")
print(f"Name: {user_data['name']}")
print(f"Age: {user_data['age']}")
print(f"Hobbies: {', '.join(user_data['hobbies'])}")
print(f"Birth Year: {user_data['birth_year']}")
print(f"Current Year: {user_data['current_year']}")

