## ---For loop--
for count in range(0,5):
    print("looping - ", count)
# looping -  0
# looping -  1
# looping -  2
# looping -  3
# looping -  4

## ---While Loop--
count = 0
while count < 5:
    print("looping - ", count)
    count += 1
# looping -  0
# looping -  1
# looping -  2
# looping -  3
# looping -  4

## ---Function--    
def say_hi(name):
    print("Hi, " + name)
# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
# o/p Hi, Michael
say_hi('Anna')
# Hi, Anna
say_hi('Eli')
# Hi, Eli

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

