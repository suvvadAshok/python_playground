# comments --> helps to understand the code, these are not run by the interpriter.

# variable: a piecw of memory allocate to named association in computer.

var_name = "python"


# indentation represents blocks in python, should maintain correct indentation otherwise leads to errors.
# `pass` keyword helps to continue the flow of code.

if var_name == "python":
    pass #there nothing, we should `pass` the code otherwise no need.


# datatypes

string = "learning python" #write between quotation mark
integers = 3 #integers
floats = 3.14
list = [string, integers, floats] #multiple datatypes
tuple = (string, integers, floats) #similar to list but immutable
set = {string, integers, floats} #similar to list but not maintain order.
dictionary = {
    "key1" : "value1",
    "key2" : "value2"
} #similar JS object, key-value pair.
boolean = True #or False
none = None


#INTEGER --> numbers

quantity = 4 #int
price = 499.99 #float
total_price = quantity * price #multiplication
#print(total_price) #output is 1999.96

item = 10 #int
value = "na" #string
total = item * value #multipication
##print(total) #output is nananananananananana 


#STRING  --> sentences which surround with quotation mark

#we can write multilines using '''para...''' or """para..."""

par = """Life is a beautiful journey that is meant to be embraced to 
the fullest every day. However, that doesn't mean you always wake up 
ready to seize the day, and sometimes need a reminder that life is a great gift. """

#we have many function with strings.

#LIST --> collection of different data types. using `[]`

lst = [3, "python", ['learn', 4], 3.14]

lst.append("code") #add new element
#print(lst) #[3, 'python', ['learn', 4], 3.14, 'code']

copy_list = lst.copy() #return new original list
# print(copy_list) #[3, 'python', ['learn', 4], 3.14, 'code']

remove_list = copy_list.clear() # it returns `None` and also `mutate` original list
# print(remove_list)   # None
# print(copy_list) #[]

elemet_occurance = lst.count(3) # element occurances, return integer
# print(elemet_occurance) #1


#DICTIONARY --> key-value pair within in `{}` similar to JS object.

person = {
    "name": "python"
}

person["source"] = "google" 
person["practice"] = "VS code"

# print(person["practice"]) #get perticular filed

# print(person) #whole dictionary

#TUPLE --> Immutable data type. using `()`
animals = ("cat", "dog", "lion",3)

# SETS --> consists of unique values, it not follows the order. use `{}`

s = {"item1", "item2","item3" }

# BOOLEAN --> True or False.

#NONE --> nothing.