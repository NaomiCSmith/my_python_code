# advanced_lists_practice.py

# Practice different methods of dictionary filtering and list comprehension

passwords = [
    {"service" : "takeaway", "password" : "asdf", "added_on" : "21/03/22"},
    {"service" : "acebook", "password" : "password123", "added_on" : "22/03/22"},
    {"service" : "makersbnb", "password" : "qwerty789", "added_on": "22/03/22"}
]

### Are the passwords long enough?


# Version 1: Using a for loop to filter

def are_all_passwords_long_enough_1(passwords):
    for password in passwords:
        if len(password["password"]) < 8:
            return False
        return True

print(are_all_passwords_long_enough_1(passwords))


# Version 2: Using filter()

def is_too_short(password):
    return len(password["password"]) < 8

def are_all_passwords_long_enough_2(passwords):
    return len(list(filter(is_too_short, passwords))) == 0

print(are_all_passwords_long_enough_2(passwords))


# Version 2.1: Lambda integration

def are_all_passwords_long_enough_2_1(passwords):
    return list(filter(lambda password: len(password["password"]) < 8, passwords)) == []

print(are_all_passwords_long_enough_2_1(passwords))


# Version 3: Using list comprehensions

def are_all_passwords_long_enough_3(passwords):
    return len([password for password in passwords if len(password["password"]) < 8]) == 0

print(are_all_passwords_long_enough_3(passwords))



### Check if any passwords were added 21/03/24


# Version 1: Using a for loop to filter

def added_passwords_21_03_v1(passwords):
    for added_on in passwords:
        if added_on["added_on"] == "21/03/22":
            return True
        return False

print(added_passwords_21_03_v1(passwords))

# Version 2: Using filter()

def check_added_on_date(dates):
    return (dates["added_on"]) == "21/03/22"

def added_passwords_21_03_v2(passwords):
    return (list(filter(check_added_on_date, passwords))) != 0

print(added_passwords_21_03_v2(passwords))


# Version 2.1: Lambda integration

def added_passwords_21_03_v21(passwords):
    return (list(filter(lambda dates: (dates["added_on"]) == "21/03/22", passwords))) != []

print(added_passwords_21_03_v21(passwords))


# Version 3: Using list comprehensions

def added_passwords_21_03_v3(passwords):
    return [date for date in passwords if (date["added_on"]) == "21/03/22"] != 0

print(added_passwords_21_03_v3(passwords))


### Return a list of all passwords added 22/03/22


# Version 1: Using a for loop to filter

def list_passwords_22_03_v1(passwords):
    passwords_22_03 = []
    for added_on in passwords:
        if added_on["added_on"] == "22/03/22":
            passwords_22_03.append(added_on["password"])
    return passwords_22_03

print(list_passwords_22_03_v1(passwords))


# Version 2: Using filter()

def check_added_on_dates_22_03(password):
    return password["added_on"] == "22/03/22"

def list_passwords_22_03_v2(passwords):
    return list(password["password"] for password in (filter(check_added_on_dates_22_03, passwords)))

print (list_passwords_22_03_v2(passwords))


# Version 2.1: Lambda integration

def list_passwords_22_03_v21(passwords):
    return list(password["password"] for password in filter(lambda password: (password["added_on"] == "22/03/22"), passwords))

print(list_passwords_22_03_v21(passwords))


# Version 3: Using list comprehensions

def list_passwords_22_03_v3(passwords):
    return list(password["password"] for password in passwords if password["added_on"] == "22/03/22")

print(list_passwords_22_03_v3(passwords))


