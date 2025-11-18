#Greetings
print("Hello \nWelcome to Generator of mini-profiles")
#requesr for user's name
user_name = input("Enter your full name: ")
# Convert string to number
birth_year = input("Enter your year of birth: ")
#Calculate age
birth_year_int = int(birth_year)
#Age result
current_age = 2025 - birth_year_int

def generate_profile(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"

#create empty list for hobbies
hobbies = []
while True:
    hobby = input("enter your favourite hobby or enter 'stop' for finish: ")

    # check , does the user want to stop?
    if hobby.lower() == "stop":
        break  # exit the loop

    # enter hobby in list
    hobbies.append(hobby)

    #We use our function to determine the life stage
life_stage = generate_profile(current_age)

    #Create a dictionary with a user profile
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

#Result
print("\n---")
print("Profile summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life stage: {user_profile['stage']}")

#Processing the list of hobbies
if len(hobbies) == 0:  # If the list is empty
    print("You haven't specified any hobbies")
else:
    print(f"Favorite ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")
