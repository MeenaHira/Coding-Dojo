# 1) 
# import random
# print (random.random()) #returns a random floating number 0.000 to 1.0000
# print (random.random()*50) #returns a random floating number 0.000 to 50.000
# print(random.random() * 25 + 10) #returns a random floating number between 10.000 and 35.000
# print(int(3.654)) # returns 3
# print (round(3.654)) # returns 4

# 2)
import random
def randInt(min=0 , max= 100 ):
    num = random.random() * (max-min) + min # without max it produces integer between 0.000 to 1.000
    return round(num) # without rounding of integer it produces float between 0.000 to 100.000  

print(randInt()) 	# should print a random integer between 0 to 100
print(randInt(max=50)) 	# should print a random integer between 0 to 50. Will overwrite default parameter max=100 to max=50
print(randInt(min=50)) 	# should print a random integer between 50 to 100. will overwrite default parameter min=0 to min=50
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500. Will overwrite both deafult parameter from min=0 to min=50 and max= 100 to max=500 argumnets
