# Task-3<br>
## Taking input in python:<br>
In Python, you can take input from the user using the input() function.<br>
As a parameter, we input the text we want to display to the user.<br>
Once the user presses “enter,” the input value is returned.<br>
## Taking input from console:<br>
When we work on project for client.When we take the input from user by the input() function<br> but this function is not enough to print value by console.<br>
then the question is raise why the console do not print anything?<br>
This situation occurrs when the console waiting for input and the user dont to know what he<br> <br>can do know,So as a programmer you need to do for user to promot to enter some values.<br>
## Pthon|output using print() function:<br>
In python we use print() function to display text on the screen.<br>
### for example:<br>
print(“strings”): When the string is passed to the function, the string is displayed as it is.<br>We can use single quotes or double quotes, but make sure they are together.<br>
## How to print without newline in python?<br>
In Python, you can print without a newline character by using the (end="") parameter of the print() function.<br>
By add this '\n' we get the new line so to change this behaviour we use 'end=""' to print without new line.<br>
<br>
### For example:<br>
print("Hello, world!", end="")<br>
## Introduction to Data Types:<br>
Python Data Types are used to define the type of a variable. It defines what type of data we are going to store in a variable. The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters.<br>
Types of data types:<br>
String,float,tuple,int,dictonary,list,bool.<br>
### String<br>
String is a collection of alphabets, words or other characters.characters enclosed in single (' ') or double (" ") quotes.<br>
### List<br>
Lists are used to store multiple items in a single variable. Examples: [1, 2, 3], ["apple", "banana", "cherry"].List enclosed in parentheses [].<br>
### Set<br>
Sets is an unordered collection data type that is iterable, mutable and has no duplicate elements.Set enclosed in parentheses {}.<br>
### Tuple<br>
Python Tuple is a collection of objects separated by commas.it is similar to list but it is immutable.Tuple enclosed in parentheses ().<br>
### dictonary<br>
In Python, dictionaries are mutable data structures that allow you to store key-value pairs. Dictionary can be created using the dict() constructor or curly braces' {}'. Once you have created a dictionary, you can add, remove, or update elements using the methods dict.<br>

### Arrays<br>
In Python, they are containers which are able to store more than one item at the same time.<br>
We can declare an array like x[100], storing 100 data in x. It is a container that can hold a fixed number of items,and these items should be the same type.<br>
## Python|end parameter in print():<br>
Python (end="") Parameter is used for the addition of any string at the end of the output of print().<br>
### for example:
print("Maraym", end=" ")<br>
print("khan", end=" ")<br>

## Python|sep parameter in print():<br>
In python (sep="") parameter is used to the separation of output by character or string in place of default space value.<br>
### for example:<br>
print("ali", "noreen", "uzma", sep=" ")<br>

## Python|output formating:<br>
In Python, you can format the output of your program in various ways using different techniques.<br>
In Python, there are several ways to present the output of a program. Data can be printed in a human-readable form, or written to a file for future use, or even in some other specified form.<br>
## Vulnerability in input() function python-2x:<br>
In Python 2.x, there's a potential security problem with the input() function. If you use input() without being careful, it can allow users to enter dangerous commands that can harm your computer or your program.<br>
To avoid this problem in Python 2.x, you should use raw_input() instead using simply input() function.<br>
In python 3x this problem is fixed you can safely and easily use input() function.<br>
## Python input methods for competitive programming:<br>

