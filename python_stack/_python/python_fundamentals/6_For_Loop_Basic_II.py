# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5] 
def biggie_size(num_list):
    # for val in num_list:
        # print(val)
    for idx in range (len(num_list)):
        # print(idx)
            if num_list[idx] > 0: # if index value of list is greater than 0, assign that number to "big"
                num_list[idx] = "big"
    return num_list
print(biggie_size([-1, 3, 5, -5]))


# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(num_list):
    # for val in num_list:
        # print (val)
    count = 0
    for idx in range(len(num_list)):
        if num_list[idx] > 0:
            count += 1 # count= count + 1
    num_list[idx]= count
    return num_list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))



# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(num_list):
    sum = 0 # variable sum to store sum of list of numbers
    for val in range (len(num_list)):
        sum = sum + num_list[val]
        # print(sum)
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# 4. Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average (num_list):
    sum = 0 # variable sum to store sum of list of numbers
    for val in range (len(num_list)):
        sum = sum + num_list[val]
        average = sum / len(num_list) # average calculation= sum of list of numbers divided by total numbers in list(length of num_list)
    return average
print(average([1,2,3,4]))
print(average([6,3,-2]))



# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0 
def length(num_list):
    return len(num_list)
print(length([37,2,1,-9]))
print(length([]))



# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(num_list):
    if len(num_list) == 0:# check firstly if empty list, then return False right away
            return False
    else:
        min_value = num_list[0]# can't do min_value = 0, as minimum should be part of the list. 0 is not part of list which we can compare with other values, otherwise for all positive number sin list it'll return 0 if we have set min_value= 0. setting min_value[0]will take  1st value in list and compare that with others
        for val in range(len(num_list)):
            if num_list[val] < min_value:
                min_value = num_list[val]
    return min_value

print(minimum([37,2,1,-9]))
print(minimum([]))


# 7. Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(num_list):
    if len(num_list) == 0:# check firstly if empty list, then return False right away
            return False
    else:
        max_value = num_list[0]# max should be part of list. Can't comapre with 0 if 0 is not part of list
    for val in range(len(num_list)):
        if num_list[val] > max_value:
            max_value = num_list[val]
    return max_value
print(maximum([37,2,1,-9]))
print(maximum([]))



# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(num_list):
    sum = sum_total(num_list)
    avg = average(num_list)
    min = minimum(num_list)
    max = maximum(num_list)
    len = length(num_list)
    analysis = {
        "sumTotal": sum,
        "average": avg,
        "minimum": min,
        "maximun": max,
        "length": len
    }
    return analysis
print(ultimate_analysis([37,2,1,-9]))
# output---->{'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximun': 37, 'length': 4}

# 9.Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(num_list):
    list_len = len(num_list)
    for idx in range(int(list_len/2)):
        # print (idx)
        temp = num_list[list_len-1-idx]
        num_list[list_len-1-idx] = num_list[idx]
        num_list[idx] = temp
        # print(num_list)
    return num_list
print(reverse_list([3,1,8,10,-5,6]))