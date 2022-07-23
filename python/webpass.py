# Generate a password for a website

website = input("WEBSITE PASSWORD GENERATOR \nWhat website will you be making a password for? \n")

while True:
    try:
        age = int(input("How old are you? \n"))
        break
    except ValueError:
        print("Invalid input")

while True:
    famMem = input("Who is older than 10 in your family? \n")
    try:
        famMemAge = int(input("How old is " + famMem + "? \n"))
        if famMemAge <= 10:
            print("Your family member needs to be older than 10. \n")
            continue
        break
    except ValueError:
        print("Invalid input")

age_char = {
    "0": ")",
    "1": "!",
    "2": "@",
    "3": "#",
    "4": "$",
    "5": "%",
    "6": "^",
    "7": "&",
    "8": "*",
    "9": "(",
}

# Return integer's equivalent in 'age_char'
def numGet(num):
    result = ""
    for char in num:
        result += age_char[char]
    return result

num1 = numGet(str(age))
num2 = numGet(str(famMemAge))

print("Your password for " + website + " is: " + website[0:4] + str(age) + str(famMemAge) + num1 + num2)
