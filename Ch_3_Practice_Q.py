
#Q1. Why are functions advantageous to have in your programs?

#A1. Functions provide a means to: eliminate the need for reduncance in code, provide modularity and
#       segmentation, increase clarity, readily modify.


#Q2. When does the code in a function execute: when the function is
#       defined or when the function is called?

#A2. A function is executed when it is called.


#Q3. What statement creates a function?

#A3. def 


#Q4. What is the difference between a function and a function call?

#A4. A 'function' is the actual device used to execute a 'mini-program', while a 'function call' is 
#       a line of code which commands a fucnction to execute.


#Q5. How many global scopes are there in a Python program? How many
#       local scopes?

#A5. There is only 1 global scope in a Python program, while there are infinitely-many local scopes.


#Q6. What happens to variables in a local scope when the function call returns?

#A6. The local variables are 'destroyed'; that is to say, they no longer exist in memory.


#Q7. What is a return value? Can a return value be part of an expression?

#A7. A 'return value' is a value that is produced from a function and it can bed used in an expression.


#Q8. If a function does not have a return statement, what is the return value
#      of a call to that function?

#A8. None


#Q9. How can you force a variable in a function to refer to the global variable?

#A9. You can force a variable in a function to refer to a global variable by preceding it with 'global'.


#Q10. What is the data type of None?

#A10. It is a NoneType.


#Q11. What does the import areallyourpetsnamederic statement do?

#A11. It imports the module named 'areallyourpetsnamederic'.


#Q12. If you had a function named bacon() in a module named spam, how
#       would you call it after importing spam?

#A12. spam.bacon()


#Q13. How can you prevent a program from crashing when it gets an error?

#A13. 
    try:
        [condition1]
    except [error_code]:
        [condition2]
        
        
#Q14. What goes in the try clause? What goes in the except clause?

#A14. The code that you feel may cause a crash goes into the 'try' clause, and the error code,
#       along with the code you'd like to execute if there is an error are paired with the
#       'except' clause.
