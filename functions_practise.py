# File: functions_practise
# This file is for practising new functions!

# Adding two numbers together
def add_num(num1, num2):
    return (num1 + num2)

print(add_num(3, 4))
    # expected return = 7

# Adding three numbers together
def add_three_num(num1, num2, num3):
    return (num1 + num2 + num3)

print(add_three_num(4, 3, 2))
    # expected return = 9

# Concatenate names
def friends_names(friend1, friend2, friend3):
    return (friend1 + ", " + friend2 + ", " + friend3)

print (friends_names("Jessi", "Rose", "Sam"))
    # expected return = "Jessi, Rose, Sam"

# Calculate the number of seconds in x weeks (int)
def number_of_seconds_in_x_weeks(weeks):
    return ((((60*60)*24)*7)* weeks)

print (number_of_seconds_in_x_weeks(5))
    # expected return = 3024000

# Add 'super' to the variable
def superify(name):
    return ("super" + name)

dog_result = superify("dog")
print(f"Look, it's {dog_result}!")
    # expected print "Look, it's superdog!"

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}!")
    # expected print "Look it's supersupersupercat!"
    

