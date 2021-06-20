#1
def a():
    return 15
# print(a())# print is out of function. On same level as a. It is invoking a()
# output--simply return15

# #2
def a():
    return 5
# print(a()+a())
# called a then after returning 5 in function a
# output--10

#3
def a():
    return 5 #only this will be printed. after first return any additional code is ignored under this return statement
    return 10
# print(a())
# output-- 5

#4
def a():
    return 5 #only this will be printed. after first return any additional code is ignored under this return statement
    print(10)
# print(a())
# output-- 5

# #5
# def a():
#     print(5)#initial print 5
# x = a()
# # print(x)# No return statement inside the 'a' statement. print whatever x is holding on to.return None when no explicit return statement. nothing is being sent back to 'a'
# # output-- 
# # 5
# # None

# 6
def a(b,c):
    print(b+c)
    return b+c # if we don't have this line it'll not return anything. without this there is Error-unsupported operand None + None and no output of 8 will be there
# print(a(1,2) + a(2,3))
#output--
# 3
# 5
# 8

# # 7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))# print 2 and 5 as the string 
# # output--
# 25 

# #8
# def a():
#     b = 100
#     print(b)# first this will be printed in output
#     if b < 10:
#         return 5 #False
#     else:
#         return 10 # This return will be executed and printed in output
#     return 7 # this return will be ignored
# print(a())
# #output--
# #100
# #10

# #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3)) # print output 7
# print(a(5,3)) # print output 14
# print(a(2,3) + a(5,3)) # print output 7+14
# # output--
# # 7
# # 14
# # 21

# #10
# def a(b,c):
#     return b+c # this will be returned and print 3+5
#     return 10
# print(a(3,5))
# # output--
# # 8

#11
b = 500
print(b)# Global- first print 500
def a():
    b = 300
    print(b)# through function-Third print b as 300
print(b)# Global-second print b as 300
a()# funtion a called
print(b)# Global-fourth print of b as 500 after function a called
# output--
# 500
# 500
# 300
# 500


#12
b = 500
print(b)# 1st-Global print of b=500
def a():
    b = 300
    print(b)# 3rd print of b=300 from function call
    return b
print(b)# 2nd-Global print of b=500
a()# function a called
print(b)# 4th print- Global b=500 after function call is done
# output--
# 500
# 500
# 300
# 500

#13
b = 500
print(b)# 1st-Global print of b=500
def a():
    b = 300
    print(b)# 3rd print of b=300 from function call
    return b
print(b)# 2nd-Global print of b=500
b=a()#function called and variblae b assigb=ned that value which is global now with b =300
print(b)#4th print- Global b=300 after function call is done and b changed
#  output--
# 500
# 500
# 300
# 300

#14 INVOKING Function b() within another function a()
def a():# step 1-function a() defined. step 4- a() will run
    print(1)# Step 5- 1st PRINT-->1
    b()# step 6- Invoking function b() from within function a()
    print(2)# LAST--> 3rd PRINT-->2
def b():# step 2-function b() defined. step 7- b()will run, after its been invoked from function a()
    print(3)# step8- 2nd PRINT-->3
a() # step 3-Function a() called
# output--
# 1
# 3
# 2

#15
def a():
    print(1) # 1st PRINT
    x = b() # function b() invoked from within function a() and variable x will get the value of function b()
    print(x)# 3rd PRINT value of x= 5 which is equal to return value through function b() invoke
    return 10 # return 10 to function a() which is equal to variable y
def b():
    print(3)# 2nd PRINT
    return 5# return 5 to function b() which is equal to variable x
y = a() #function a invoked and variable y gets the value of function a()
print(y)# LAST PRINT y=return value of a(), which is 10
#output--
# 1
# 3
# 5
# 10



