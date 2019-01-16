# Lab 2: Defining Functions and Testing Them

[Lab 1]:
    https://github.com/eecs230/lab1#testing-that-everything-works
    
This repository includes existing code that will test your understanding
of Python arithmetic and algebra as well as help you define your own functions.
Start by forking it to your own account and then cloning your
fork in PyCharm. Lab 1 includes [instructions][Lab 1] on how to do this,
so you should refer there if you do not remember how. (You can also
clone this repo without forking, but you won't be able to push any
changes you might make.)

Once you have opened the cloned Git repo in PyCharm, you may have to
edit a Python source file and wait a few seconds for PyCharm to
configure your Python environment. When it's settled down, you'll
be ready to move on. If you need help at any time, please ask your
Peer Mentors John Nguyen and Yingliao Wang.

Please review the following concepts from lecture 2 before starting this lab:
* Numbers, strings, booleans, and operations on those
* Tuples
* Defining and using your own functions

## A quick review of boolean algebra
* Boolean values are not strings!
    * They are surrounded by quotes
* True and False are the only values in the `bool` type
* Boolean expressions are expressions that evaluate to True or False

```    
x == y               # x is equal to y
x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y
```
* operators such as `and` or `or` are evaluated left-to-right
```
not x	        # Returns True if x is True, False otherwise
x and y	        # Returns x if x is False, y otherwise
x or y	        # Returns y if x is False, x otherwise
```
## A quick review or arithmetic operations
* Addition:   8 + 5
* Subtraction: 8 - 5
* Multiplication 8 * 5
* Division: 8 / 5
* Floor Division: 8 // 5
* Exponent: 8 ** 5
* Modulus: 8 % 5

## A quick review of tuples
Named tuples allow us to define data classes with type hinting. To create a named tuple,
use the following syntax:
```
from typing import NamedTuple  # >= Python.3.6.0

class Employee(NamedTuple):
  name: str
  department: str
  salary: int
  is_remote: bool = False  # >= Python.3.6.1
    
bob = Employee(name='Bob', department='IT', salary=10000, is_remote=True)
```
## Defining your functions
- First open `lab2`
- notice how the function full_name(first, mid, last) is defined
- fill in the code to define the function is_even
    - What operators do you need?
- Define the Position NamedTuple to represent the coordinates of a sphere
- Now define the volume of a sphere
    - Does order of operations matter? 
    - What arithmetic operations do you need?
- Now look at the `overlap` function 
    - What exactly is it asking you to define? Look at this [WolframMathWorld](http://mathworld.wolfram.com/Sphere-SphereIntersection.html)
    for some hints
    - To speed up your calculation, how would you account for the case in which r=R?
        - How would you implement this?
- Take some time to attempt to implement the other functions such as `contained_within` and `trilateration`
    - Hint: you can google 'True range multilateration' or 'trilateration'
    - What is `contained_within` returning? A str, bool, int?


## Testing your functions
We will be writing 
From the configuration drop-down (in the toolbar, just to the left of the run button),
choose either “Add Configuration…” or “Edit Configurations…” (whichever is available). 
In the window that opens, click the + sign in the upper left, find the “Python Tests” submenu, 
and select the “pytest” option. It's possible to change the configuration Target to “Custom.” 
Leave all the blank fields blank, and click OK. Now, the configuration you just created 
(probably named “pytest”) show appear in the configuration drop-down. Select and run it. 
If all goes well, you will see a summary of the passed tests, but if a test fails, 
pytest will print more information about what went wrong. Try modifying the examples 
in `test_lab` to see what a failing test looks like.