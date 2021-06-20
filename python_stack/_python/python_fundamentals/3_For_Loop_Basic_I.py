# 1. Basic - Print all integers from 0 to 150.
for int in range(0,150+1):
    # if int<=150:
        print(int)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001,5):#increment by 5
    print(x)

        # or
for x in range(5,1001): 
    if x % 5==0:
        print(x)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for int in range(1,101,1):
    if int % 10==0:#most specific.Check this before and print "Coding Dojo" if int is divisible by 10, instead of if divisble by 5 to just print"Coding" 
        print("Coding Dojo")
    elif int %5==0:# integers divisible by 5
        print("Coding")
    else:
        print(int)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for x in range (1,500000,2):
    sum += x       #sum + x  
print(sum) # It is outside for loop. if this print statement is indented(inside for loop), it'll print each added odd number sum in when it advance to next odd number

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num in range(2018,5000,4):# no stopping if we don't add ending number 5000. But since its not mentioned and counting down instead of counting up
    print(num)
        # or
for num in range(2018,0,-4):#counting down, ending 0 which is not ementioned in question when to stop
    print(num)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
# if we use for loop-for x in range(0,50,3):# This for loop would have rigid numbers 0, 50 and 3, instead we need variables for flexible counter
lowNum = 0
highNum = 50
mult = 3
for x in range(lowNum,highNum+2):
    if x % mult == 0:
        print(x)