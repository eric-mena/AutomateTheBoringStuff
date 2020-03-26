#Q1. What are the two values of the Boolean data type? How do you write them?
#A1. True and False.

#Q2. What are the three Boolean operators?
#A2. # and, or, not.

#Q3. Write our the truth tables of each Boolean operator.
#A3. 
    True and True = True
    True and False = False
    False and True = False
    False and False = True
    True or True = True
    True or False = True
    False or True = True
    False or False = True

#Q4. What do the following expressions evaluate to?

    (5 > 4) and (3 == 5)
    not (5 > 4) 
    (5 > 4) or (3 == 5)
    not ((5 > 4) or (3 == 5))
    (True and True) and (True == False)
    (not False) or (not True)

#A4.

    False
    False
    True
    False
    False
    True

#Q5. What are the six comparison operators?
#A6. <,>,=,<=,>=,!=

#Q6. What is the difference between the equal operator and the assignment operator?
#A6. The equal operator is denoted '==' and verifies whether the expressions on both sides of it match.
#     The assignment operator is denoted by '=' and assigns the value on the right to the variable on the left.

#Q7. Explain what a condition is and where you would use one.
#A7. A condition is a clause, or argument, passed into a flow control statement such as IF, ELSE, WHILE, FOR, etc.

#Q8. Identify the three blocks in this code:

#A8. 

    #1
    spam = 0
    if spam == 10:
    print('eggs')
    #2
    if spam > 5:
    print('bacon')
    #3
    else:
    print('ham')
    print('spam')
    print('spam')
  
#Q9. Write code that prints 'Hello' if 1 is stored in SPAM, prints 'Howdy' if 2 is stored in SPAM, and print
#     'Greetings' if antyhing else is stored in SPAM.

#A9.

spam = input()

if spam == 1:
  print('Hello')
if spam == 2:
  print('Greetings')
else:
  print('Greetings')
