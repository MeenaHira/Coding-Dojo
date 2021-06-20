# 1. Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    list_num = []
    for n in range(num,0-1,-1):
        list_num.append(n)
    return list_num
# print(countdown(5))
# output--
# [5, 4, 3, 2, 1, 0]


# 2. Print and Return - Create a function that will receive a list with two numbers.
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def two_num(num_list):
    print (num_list[0])# print first value
    return num_list[1]# return second value
# print(two_num([8,10]))
#output--
# 8
# 10


# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(num_list):
    sum_first_value_and_list_length = num_list[0] + len(num_list) #sum of the first value in the list plus the list's length
    return sum_first_value_and_list_length # return sum 

# print(first_plus_length([10,2,31,25]))
#output--
#14


# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
def Values_Greater_than_Second(num_list):
    new_num_list = []
    num_list_second_value = num_list[1]
    for index in range(0,len(num_list),1):
        print(num_list[index])
    print("#####")
        # if num_list[] > num_list[1]:
        #     new_num_list.append(num_list[])
        # return new_num_list
        # elif

Values_Greater_than_Second([5,2,3,2,1,4])

# 5. Example: values_greater_than_second([3]) should return False
# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]