# CommaCode.py

# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam 
# list to the function would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats']
cats = ['Fuzzy', 'Furry', 'Fluffy', 'Funky']
cheeses = ['gouda', 'muenster']
one = [1, 2, 3]

def edit(listToEdit):
    for i in listToEdit:
        if listToEdit.index(i) < len(listToEdit) - 1:
            print(str(i) + ', ', end='')
        else:
            print('and ' + str(i) + '.')

edit(spam)
edit(cats)
edit(cheeses)
edit(one)

# CommaCodeAlt.py

# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function 
# should be able to work with any list value passed to it.

def fun(aList):
    for i in aList:
        if aList.index(i) < len(aList) - 1:
            print(i + ', ', end='')
        else:
            print('and ' + i + '.')

inputs = []
while True:
    print('Enter a string or number. Enter a blank to stop.')
    response = input()
    if response == '':
        break
    elif response != '':
        inputs.append(response)
fun(inputs)
