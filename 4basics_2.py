#INDEXING

#it starts with 0

# index -->     0      1       2        3
sample_list = ["one", "two", "three", "four"]
# -ve index--> -4     -3      -2       -1
            # [index_value] we can access the perticular value.
# print(sample_list[2])  #three
# can access with -ve indexes
# print(sample_list[-3]) #two


# SLICING --> can access multiple values.

     # [start_ind : end_ind] :- start_ind- included, end_ind- excluded
# print(sample_list[2:3]) # ['three']
     # [start_ind : end_ind] :- end_ind = length of list.
# print(sample_list[2:]) # ['three', 'four']
     # [start_ind : end_ind] :- start_ind = 0.
# print(sample_list[:3])  # ['one', 'two', 'three']

# print(sample_list[-3:]) # ['two', 'three', 'four']

# print(sample_list[:-2]) # ['one', 'two']

# print(sample_list[:]) # ['one', 'two', 'three', 'four']

# Accept input from user 
    #input() method helps take value
# name = input('enter your name') 
# print('helloo...!',name) 

# age = input('enter age: ') 
# print('my age is: ',age)

#it take input as string by default
# print(type(age)) #string 

prog_lang = "python"
desc = "to learn"
message = "{} is a friendly language {}".format(prog_lang, desc)  #old way

message = f"{prog_lang} is a friendly language {desc}" # simple and more understandable

# print(message)

#COMPARISION OPERATORS 

# < lessthan
# <= lessthan or equal
# > greaterthan
# >= greaterthan or equal
# == equal
# != not equal

#IF-ELSE

# if condtion:
#     .
#     .
# else:
#     .
#     .

#NESTED IF-ELSE

# if condition_1:
#     .
#     .
# elif condition_2:
#     .
#     .
# elif condition_3:
#     .
#     .
# else:
#     .
#     .

empt_list = {}

if empt_list: #empty list or empty tuple or empty set or `None` are false values.
    print("I'm true")
else:
    print("I'm false") #this block exicutes.