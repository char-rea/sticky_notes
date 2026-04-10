# asking the user to input a sentence and obtaining different string methods to manipulate the string and print the results

str_manip = input("Please enter a sentence: ")    

print(len(str_manip)) 

print(str_manip[-1])  

str_manip = str_manip.replace("o", "@")
print(str_manip)  

print(str_manip[10:])

newbie = (str_manip[:3]) + (str_manip[-2:])
print(newbie)