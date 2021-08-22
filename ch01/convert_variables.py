the_age = input("What's your age?: ")

age_as_num = int(the_age)
age_as_num = age_as_num + 10

age_as_text = str(age_as_num)
print("Your age + 10 is " + age_as_text)

print(f"Your age + 10 is {age_as_num}")