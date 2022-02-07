#Print out hello world
print("Hello world \n")

#Print triangle
print("   /|")
print("  / |")
print(" /__| \n")

#Variable usage - when string and int concatonate use str(int)
name = "Mazda"
age = 19
print("hi my name is " + name)
print(name +  " is " + str(age) + " years old and like to play piano")
print(name + "will turn " + str(age+1) + " in a weeks time.\n")

#Using string functions(index at 0, word[0], len(), .upper(), str(int), index(), .replace( , ), .isupper()

word = "Strawberry"
print(word.upper())
print(word.upper().isupper())
print("Returns the length: " + str(len(word)))
print("Return index 2 of word variable: " + word[2])
print("Returns the index of \"a\" in word variable: " + str(word.index("a")))
print(word.replace("Straw", "Egg") + "\n")

#Using numbers also have ceil in math import and sqrt
print("*, /, -, +, %")
print("10 % 3 = " + str(10 % 3))
my_num = -7
print("abs(int) when want positive value: " + str(abs(my_num)))
print("pow( , ) to put power x^y e.g. 3^2 = " + str(pow(3, 2)))
print("max(x, y) returns max value e.g. Max(3, 4) = " +str(max((3, 4))))
print("round() to get whole closest whole number e.g. round(2.6) = " + str(round(2.6)))
print("from math import *. To get math functions.")
from math import *
print("floor(3.1)=3 (get whole number rounded down) e.g. floor(3.99) = " + str(floor(3.99)) + "\n")

#Take inputs

name = input("What is your name mate? ")
print("Hey brother " + name + " good to have you.")

#Basic calculator use float for ints and decimal number not just int()
num_one = input("What is your first number: ")
num_two = input("What is your second number: ")
print("Your numbers " + str(num_one) + " and " + str(num_two) + " will now be added.")
print(float(num_one) + float(num_two))

#Mad libs
noun = input("Give me a noun: ")
smell = input("Give me a smell: ")
person = input("Give me a person : ")
print("You find a " + noun + " in the toilet.")
print("It smells like " + smell)
print(person + " find you in the toilet.")