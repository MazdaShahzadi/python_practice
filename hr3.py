""""
#basic calculator
num1 = float(input("What is your first number: "))
num2 = float(input("What is your second number: "))
operation = input("What operations \"x\", \"-\", \"+\" : ")

if operation == "x":
    print("Doing multiplication - result = " + str(float(num1)*float(num2)))
elif operation == "-":
    print("Doing subtraction - result = " + str(float(num1) - float(num2)))
elif operation == "+":
    print("Doing addition - result = " + str(float(num1) + float(num2)))
else:
    print("invalid input mate")
"""

#Dictionaries
"""
roleConversion = {
    "kn" : "knight",
    "qu" : "queen",
    "ki" : "king",
    "sl" : "solider"
}

print(roleConversion["kn"])
print(roleConversion.get("egg", "not a valid key"))

#while loop

i = 1
while i <= 10:
    print(i)
    i += 1
"""

"""
#word game
secret_word = "egg salad"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lost")
else:
    print("you win")
"""

"""
#for loop
odd_num = [3, 5, 7, 1, 9]
for letter in "egg salad":
    print(letter)
print()
for num in odd_num:
    print(num)
print()
for index in range(3, 10):
    print(index)
    len(odd_num)
"""

"""
#exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))
"""

"""
#2D grid
num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7]
]

print(num_grid[0][1])

for row in num_grid:
    for column in row:
        print(column)
"""

#transalator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))