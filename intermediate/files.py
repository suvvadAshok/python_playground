# r -> read
# w -> write
# a -> append

        #(file_path_name, mode of the file) as variable_name
# with open("./README.txt","r") as file:
    # print(file.read()) # print the content in readme.txt file, if file not exist it shows error.
    # content = file.read() #assign to the variable
# print(content) #print the variable

#we can read each line by method file.readlines() it returns list of the element where element = content in each line with superscript with `\n`


# with open("./writefile.py","w") as file: #if file exist it over-write the whole content else it create new file.
    # file.write("int a = 10") 

# with open("writefile.py","a") as file: #if file exist content append to the original file, else create new file as similar to write mode
#    file.write("\nprint(a)")

