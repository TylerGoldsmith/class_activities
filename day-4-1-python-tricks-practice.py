# 1: Write a lambda function to sort a list of tuples in ascending order 
# according to the number in the second position of each tuple.
# Unsorted list of tuples: 

ListQ1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 

sorted_grade = sorted(ListQ1, key = lambda x: x[1])

print('1: Sorted grades: ' + f'{sorted_grade}')
# Printed Result
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



# 2: Write a lambda function to cube every element of a list.
# #Original list: [3,6,9,2] List after lambda function: [27,216,729,8]

ListQ2 = [3,6,9,2]
cubed = lambda x: [i**3 for i in x]
print('2: List numbers: ' + f'{ListQ2}' + ' List numbers cubed: ' + f'{cubed(ListQ2)}')

# List after lambda function: [27,216,729,8]

# 3: Write a lambda function to determine whether a number is even or odd 
# (the function should return True or False), and then use the 
# function and a list comprehension to create a new list of booleans, 
# where even numbers are True and odd numbers are False.
# Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]

ListQ3 = [3,6,9,2]
even = filter(lambda x: x%2 ==0, ListQ3)
odd = filter(lambda x: x%2 ==1, ListQ3)

print('3: Even: ' + f'{list(even)}' + ' Odd: ' + f'{list(odd)}')


# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).

x = [i for i in range(1, 101)]
print('4: Numbers one to 100: ' + f'{x}')

# Use a dictionary comprehension to count the length of each word in a sentence.

# otuput: {'The': 3, 
# 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}

sentence = "The quick brown fox jumped over the fence."

print("5: 'Word' : Word Length",{word:len(word) for word in sentence.split()})
