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
1. First open `lab2`
2. Notice how the function `full_name` is defined
    - Can you explain what is happening to the given Strings  
3. Fill in the code to define the function `is_even`
    - What operators do you need?
4. Define the Position NamedTuple to represent the coordinates of a sphere
5. Now define the volume of a sphere
    - Does order of operations matter? 
    - What arithmetic operations do you need?
6. Now look at the `overlap` function 
    - What exactly is it asking you to define? Look at this [WolframMathWorld](http://mathworld.wolfram.com/Sphere-SphereIntersection.html)
    for some hints
    - To speed up your calculation, how would you account for the case in which r=R?
        - How would you implement this?
7 Take some time to attempt to implement the other functions such as `contained_within` and `trilateration`
    - Hint: Notice that the parameters and return type for `trilateration` are empty
        - What would you fill in for the parameters and return given the description of what the function
        does in the comments. This one may be hard, so try to figure out what inputs and outputs the function
        would take. You don't have to attempt to implement it
        - Hint: you can google 'True range multilateration' or 'trilateration'
    - What is `intersect` returning?
        - How do we input two circles and receive the correct output?

## Testing your functions
After you have written a few functions and are ready to move on, we will be writing basic assertion tests.

Assertions are statements that assert or verify computations in your program. They are boolean expressions that evaluate to true or not. 

If the assertion is true, the program does nothing; however, if the assertion is false, the program stops and throws an error. 

Because assertions can stop a program and print a message, they may be useful to showing where program errors have occured.

Python has a built-in `assert` statement
```
assert <condition>
```
```
assert <condition>,<error message>
```

If the assert evaluates the false the Python program halts and gives us an `AssertionError`

1. Reference the short tests already written in `test_lab2`,
2. write some short assertion tests to verify that you program works. 
3. Run the following command in the `lab2` directory to run your tests. 
```
$ pipenv run pytest
```
If you encounter any errors you may have the wrong version of Python

Let us know if you have any questions. Once you've successfully written some
tests you are free to leave. 
