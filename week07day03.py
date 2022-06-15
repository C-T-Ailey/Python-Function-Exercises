from operator import index, indexOf

# Exercise 1

students = ["Jim", "Robbie", "Louis"]
print(students[1])
print(students[len(students)-1])

# Exercise 2

foods = ("coleslaw", "potato salad", "pizza")

for food in foods:
    print(f"{food.capitalize()} is a good food.")

# Exercise 3

for food in foods:
    if foods.index(food) in range(len(foods)-2,len(foods)):
        print(food)

# Exercise 4

home_town = {"city":"Shawnee","state":"Oklahoma","population":27165}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}.")

# Exercise 5

for key in home_town:
    print(f"{key} = {home_town[key]}")

# Exercise 6

cohort = []

for student in students:
    print(student)
    st_index = students.index(student)
    student_dict = {
        "student": student,
        "fav_food": foods[st_index]
    }
    cohort.append(student_dict)

for student in cohort:
    print(student)

# Exercise 7

awesome_students = [f"{student} is awesome!" for student in students]

for student in awesome_students:
    print(student)

# Exercise 8

for food in foods:
    if "a" in food:
        print(food)