#Example taking multiple input from user
a = input("Enter your name: ") #get the string input from user
print(a)
b = int(input("Enter yor age: "))#get the int input from user
print(b)
c = float(input("Enter your CGPA: "))#get the float input from user
print(type(c))

#Example Python input method for competitive programming:
#Example Vunlnerability in input() function -Python 2x:

k = input("Enter a number: ")#input() that allows you to get input from users
print("You entered:", k)
"""To avoid this risk,use a different function called raw_input() in Python 2.x.
k = raw_input("Enter a number: ")# it does not run in python 3x
print("You entered:", k)"""

#Example of To print a newline
print("MY ", end="")
print("age ", end="")
print("is ", end="")
print("20. ", end="")
print()
#Example of print() function
a = "Maryam"
b = 20
c = 3.3
print("Values of a, b, and c are:", a, b, c)

#Example of sep and end print()function
# end print()function
print("Hello ",end="")
print("world ")
# sep print()function
print("i am the student of: ","BSCS",sep='')
#Example of OUTPUT f ormating
name = "Ali"
age = 30
#Using String Modulo Operator(%)
name = "Ali"
age = 30
print("Name: %s, age: %d" % (name, age))#type of data is important
#Using {}
print("name:{} age:{}".format(name,age))#type of the data is not important
#Example of string
school ="elementry school"
#Example of tuple
t = (1, 2, 3, 'apple')
print(t)
#Example of sets
s = {1, 2, 2, 3, 4, 4}
print(s)
#Example of list
l = [1, 2, 3, 'banana']
print(l)
#Example of Arrays
a =["BMW","Ford","volvo"]
print(a)
#Example of dictonary
d ={'name': 'Ali', 'age': 30, 'city': 'ISLAMABAD'}
print(d)

#Example of output formating:
name = "kiran"
age = 20
salary =33000.0
#Approach 1 by simple print()function
print(name,age,salary)
#Approach 2 by % format output %s mean string, %d mean int, %f mean float.
print("name: %s age: %d salary: %f" %(name,age,salary))#type of data is importanat
#Approach 3 by dot format/ curly braces{}
print("name:{} age{} salary{}".format(name,age,salary))#type of the data is not important
