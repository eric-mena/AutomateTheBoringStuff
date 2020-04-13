#Q1. What does the code for an empty dictionary look like?
#A1. emptyDict = {}

#Q2. What does a dictionary value with a key 'foo' and a value 42 look like?
#A2. {'foo':42}

#Q3. What is the main difference between a dictionary and a list?
#A3. The items in a list are ordered, while they aren't in a dictionary.

#Q4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
#A4. You will get a KeyError error.

#Q5. If a dictionary is stored in spam, what is the difference between the
#   expressions 'cat' in spam and 'cat' in spam.keys()?
#A5. No difference.

#Q6. If a dictionary is stored in spam, what is the difference between the
#   expressions 'cat' in spam and 'cat' in spam.values()?
#A6. The latter checks to see if there is a value 'cat' in spam.

#Q7. What is a shortcut for the following code?
#   if 'color' not in spam:
#   spam['color'] = 'black'
#A7. spam.setdefault('color','black')

#Q8. What module and function can be used to “pretty print” dictionary
#   values?
#A8. pprint.pprint()
