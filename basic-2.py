print("Up to 1:03hrs in python tutorial")

#Lists

friends = ["Jhon", "Max", "Mazda", "x", "y"]
print(friends)
print(friends[0])
print(friends[1:3])
friends[0] = "Jackson"
print(friends.index("Max"))

random_numbers = [1, 2, 3, 6, 8, 4]
random_numbers.append(9) # add 9 to end of the list
random_numbers.insert(1, 6) #add in index 1 number 6 to list
random_numbers.remove(2) #remove from index 2 or number 2?
# remove full list with clear() random_numbers.clear()
random_numbers.pop() # remove value at end of the list
friends.extend(random_numbers) # add two lists together
random_numbers.count(1) # count number of times 2 in list
random_numbers.sort() # put in ascending order
random_numbers2 = random_numbers.copy() # create copy

#Tuples - immutable

coordinates = (4, 5)
print(coordinates[0])

#functions
def say_hi(name, role):
    print("hello " + name + ", my dude. You are a " + role)


say_hi("Max", "knight")

def cube(number):
    return number*number*number

print(cube(3))

#if statements

number = 5
if (number%2==0) or (1+1==3):
    print("Your number is even")
elif (number%2==1) and 1+1==2:
    print("you are odd")
else:
    print("you must be not odd or even")
