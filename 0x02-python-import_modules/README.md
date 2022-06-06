#!/usr/bin/python3
a = 1
print(a)
a = "Hello"
print(a)
b = 2
s = 'Hello world'
print(a)
print(b)

# print(objecs, sep, end=, file=file, flush=)
# print(s, end="")



first_name = "Mohammed"
last_name = "Ali"

full_name = first_name + " " + last_name

print(full_name)
#print adds a line break by default 
#no concept of character or string in python '' and "" are the same.


#control flow statement 
#to find a range a numbers from 1 to 10

for x in range(1, 11):
    print(x, end=' ')
print()


#loop through a string 

s = "Hello world\n"
for c in s:
    print(c, end="")



#while loop

counter = 0

while counter < 10:
    print(counter, end="")
    counter += 1
    if counter == 10:
        break
print()


#if - else

age = 10
if age < 5:
    print("too young")
elif age == 5:
    print("This is a kid")
else:
    print('He is a grown boy')

