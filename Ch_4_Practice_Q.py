#Q1. What is []?
#A1. This is an empty list.

#Q2. How would you assign the value 'hello' as the third value in a list stored
#     in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
#A2. spam[2] = 'hello'

#Q3. For the following three questions, let’s say spam contains the list ['a',
#     'b', 'c', 'd']. 
#Q3. What does spam[int('3' * 2) / 11] evaluate to?
#A3. 'd'

#Q4. What does spam[-1] evaluate to?
#A4. 'd'

#Q5. What does spam[:2] evaluate to?
#A5. ['a','b']

#Q6. For the following three questions, let’s say bacon contains the list
#     [3.14, 'cat', 11, 'cat', True].
#    What does bacon.index('cat') evaluate to?
#A6. 1

#Q7. What does bacon.append(99) make the list value in bacon look like?
#A7. [3.14, 'cat', 11, 'cat', True, 99]

#Q8. What does bacon.remove('cat') make the list value in bacon look like?
#A8. [3.14, 11, 'cat', True]

#Q9. What are the operators for list concatenation and list replication?
#A9. +,*

#Q10. What is the difference between the append() and insert() list methods?
#A10. append() will add a variable to the end of a list, while insert() will add a variable 
#       to the index specified within the square brackets.

#Q11. What are two ways to remove values from a list?
#A11. del(), remove()

#Q12. Name a few ways that list values are similar to string values.
#A12. You can call specific locations within a list/string, you can use the length function, you
#       you can slice them.

#Q13. What is the difference between lists and tuples?
#A13. Lists are mutable, while tuples are immutable.

#Q14. How do you type the tuple value that has just the integer value 42 in it?
#A14. cheese = (42,)

#Q15. How can you get the tuple form of a list value? How can you get the list
#      form of a tuple value?
#A15. tuple(), and list().

#Q16. Variables that “contain” list values don’t actually contain lists directly.
#      What do they contain instead?
#A16. They contain references to list values.

#Q17. What is the difference between copy.copy() and copy.deepcopy()?
#A17. the methods differ in that copy() will duplicate a list with conventional variables, and
#       deepcopy() will duplicate lists that contain lists within them.
