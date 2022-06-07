#!/usr/bin/python3
#add strings and integers
age = 19
name = 'Jhon'

# message = 'The name is ' + name + " and is " + repr(age) + " years old"
# print(message)
#repr funtion returns something the represent an object in a string format


#formatted string - f-string
# message = f"The name is {name} and is {age} year old"
# print(message)


#formatted string - .format string
message = "The name is {:s} and is {:d} years old".format(name, age)
print(message)
#to specify the formats :s--- string   :d---integer
