# Lab 2: Defining Functions and Testing Them

[Lab 1]:
    https://github.com/eecs230/lab1#testing-that-everything-works

This repository includes existing code that will test your understanding
Python arithmetic and algebra as well as help you define your own functions.
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

Please review the following concepts from lecture 2 before starting this lab
* Numbers, strings, booleans, and operations on those
* Tuples
* Defining and using your own functions

## Defining your functions
1. First open `lab2`
    - notice how 

## Testing your functions

From the configuration drop-down (in the toolbar, just to the left of the run button),
choose either “Add Configuration…” or “Edit Configurations…” (whichever is available). 
In the window that opens, click the + sign in the upper left, find the “Python Tests” submenu, 
and select the “pytest” option. It's possible to change the configuration Target to “Custom.” 
Leave all the blank fields blank, and click OK. Now, the configuration you just created 
(probably named “pytest”) show appear in the configuration drop-down. Select and run it. 
If all goes well, you will see a summary of the passed tests, but if a test fails, 
pytest will print more information about what went wrong. Try modifying the examples 
in `test_lab` to see what a failing test looks like.