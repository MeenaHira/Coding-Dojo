
# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello" , name, '!')  # with a comma
print ("Hello " +name) # with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello", name)	# with a comma
print( "Hello " + str(name))	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2} ." ) # with an f string

# BONUS-
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

#SORT-
new_list = ['a','e','b','d','c']
num_list = [4,1,8,3]
new_list.sort()
num_list.sort()
print(new_list)
print(num_list)
print(new_list, num_list)

#### ----DICTIONARY---- #####
example 1#
prices_lookup = {'apple':2.99, 'oranges':1.99, "milk":5.80}
print(prices_lookup['apple'])

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k3']['insideKey'])
print(d['k2'][2])

Dictionary buit-in Methods
x=("name","age","trick")
y=("Fido")
pet_info= dict.fromkeys(x,y)
print(pet_info)
pet_info = {"name": "Fido", "age": 4,"trick": "rolls over"}
x= pet_info.get("name")
print(x)
pet_info.fromkeys()
print (pet_info)


# ----LOOPS -------
#1 
for i in range(1, 10, 1):
    print(i)

#  output--
#  1
#  2
#  3
#  4
#  5
#  6
#  7
#  8
#  9

#2
for t in range(1, 10, 3):
    print(t)

#  output--
#  1
#  4
#  7

#3
for y in range(5):
    if y < 5:
        print(y)
    elif y == 3:
        print("y is 3")

#  output--
#  0
#  1
#  2
#  3
#  4

#4
for j in range(20, 1, -3):
    print(j) 

#  output--
#  20
#  17
#  14
#  11
#  8
#  5
#  2

#5
cities = ["London", "Paris", "Tokyo"]
for city in cities:
    print(city)

#  output--
#  London
#  Paris
#  Tokyo

#6
numbers = [7, 13, 8, 42]
for x in range(0, len(numbers)):
    print(x)
    print(numbers[x])
if numbers[len(numbers) - 1] == 42:
    print("The answer to life, the universe, and everything.")

#   output--
#     0
#     7
#     1
#     13
#     2
#     8
#     3
#     42
#     The answer to life, the universe, and everything  

#7
for num in range(10):
    if num % 2 == 0:
        print("Hello")
    elif num % 4 == 0:
        print("World")
    else:
        print(num)

# output--
# Hello
# 1
# Hello
# 3
# Hello
# 5
# Hello
# 7
# Hello
#9

#8
for num in range(10):
    if num % 4 == 0:
        print("Hello")
    elif num % 2 == 0:
        print("World")
    else:
        print(num)
# output--
# Hello
# 1
# World
# 3
# Hello
# 5
# World
# 7
# Hello
# 9

9
pet_info = {"name": "Fido", "age": 4,"trick": "rolls over"}
for key in pet_info:
    print(key)
    print(pet_info[key])

# output--
#  name 
#  Fido 
#  age 
#  4 
#  trick 
#  rolls over 

#10
things_to_remember = {"First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)

# output--
#  First, I will use the 20 minute rule and use the platform and other resources to find my answer
#  Second, I will ask my classmates for help, like how I would ask a fellow employee at my job
#  Fourth, I will ask an available instructor
#  Third, I will ask an available TA in a public setting, so everyone can benefit from my question
