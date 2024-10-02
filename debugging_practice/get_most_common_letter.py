# # Debugging exercise:
# original code:
# def get_most_common_letter(text):
#     counter = {}
#     for char in text:
#         counter[char] = counter.get(char, 0) + 1
#     letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
#     return letter


# print(f"""
# Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
# Expected: o
# Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
# """)

# My solution using discovery debugging method:

def get_most_common_letter(text):
    counter = {}
    # add in stripped so whitespace is removed! " " was highest.
    stripped = text.replace(" ", "")
    for char in stripped:
        counter[char] = counter.get(char, 0) + 1
    #changed [0][0] to [-1][0] so that we get highest value rather than lowest (sorted works in ascending)
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(counter)
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
