####--- UPDATE VALUES IN DICTIONARIES AND LISTS---###

# 1) LIST OF LISTs--Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15 # check- print index 0 of index 1 which is 10, assign to 15
# print(x)
#output- [[5, 2, 3], [15, 8, 9]]

# 2) LIST OF DICTIONARIES--Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] ='Bryan' # 0 index last_name access
#print(students)
#Output- [{'first_name': 'Michael', 'last_name': 'Bryan'}, {'first_name': 'John', 'last_name': 'Rosales'}]
    
# 3) DICTIONARY OF LISTS-- In the sports_directory, change 'Messi' to 'Andres'.  
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]= 'Andres' # In soccer key, index 0 of list access and change to Andres
# print(sports_directory)
#output- {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer': ['Andres', 'Ronaldo', 'Rooney']}

# 4) LIST OF DICTIONARIES--Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y']= 30 # position 0 in list, then key y access, change to 30
#print(z)
# output-{'x': 10, 'y': 30}]


####---ITERATE THROUGH LIST OF DICTIONARIES--##  
#5) Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

def iterateDictionary(some_list): #parameter some_list 
    # print(some_list)
    for idx in range(len(some_list)):
        print('first_name -', some_list[idx]['first_name'], ',',' last_name -', some_list[idx]['last_name'])

students = [                       # argument student passed through parameter
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
# Output--
# first_name - Michael ,  last_name - Jordan
# first_name - John ,  last_name - Rosales
# first_name - Mark ,  last_name - Guillen
# first_name - KB ,  last_name - Tonel

# ANOTHER METHOD--
def iterateDictionary(some_list): #parameter some_list 
    for idx in range(len(some_list)):
        student_dict = some_list[idx] # build a string
        for key in student_dict:
            print(key, '-', student_dict[key]) # add to that string, print the string
students = [                       # argument student passed through parameter
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
# Output--
# first_name - Michael
# last_name - Jordan
# first_name - John
# last_name - Rosales
# first_name - Mark
# last_name - Guillen
# first_name - KB
# last_name - Tonel

3) Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
Michael
John
Mark
KB
# And iterateDictionary2('last_name', students) should output:
Jordan
Rosales
Guillen
Tonel

# 4)Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon