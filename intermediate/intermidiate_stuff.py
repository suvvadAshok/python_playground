import requests

# req = requests.get("https://dog.ceo/api/breeds/image/random")
# print(req.status_code)


# if the request is in JSON_String. we need to convert into JSON formate, for that
# import json

# variable_name = json.loads(variable_name)

# if we want the mutate data we have to use 
#    variable_name_1 = json.dumps(variable_name)

# to install pip --> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# and than run a command --> python get-pip.py to install pip

#we can install and uninstall different modules in pip 
 
# pip install module_name
# pip unistall module_name


# MUTABLE vs IMMUTABLE

# Strings, tuple are immutable in python.

# ENUMARATION.


#LIST_COMPREHENSION
# numbers = [num**2>10 for num in [1,3,5,7,9] if num**2>10]
# print(numbers) #[1, 9, 25, 49, 81]

# newList = [n**2 for n in [1,3,5,7,9] if n**2>10]
# print(newList) #[25, 49, 81]