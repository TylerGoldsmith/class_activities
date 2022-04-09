#1: arb_args - Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    for a in args:
        print("#1: The arguements are: " f"{a}")

arb_args("a", "b", "c")

#2: inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(x,y):
    def inner_1():
        return x + y
    def inner_2():
        return x - y
    print("#2: The sum of the functions inner_1 and inner_2 is: " + f"{inner_1() + inner_2()}")

inner_func(5,2)


#3: lunch_lady - Takes in two strings: a student's name and their lunch preference. 
# The function should print both strings. If a lunch preference is not given, 
# "Mystery Meat" should be printed instead.

def lunch_lady(name, lunch="Mystery Meat"):
    print("#3: The Lunch ladies name is: " + f"{name}"," & their lunch preference is: " f"{lunch}")
lunch_lady("Sam", "Corn")
lunch_lady("Sam")

#4: sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(x,y):
    return x+y, x*y
print("#4: The sum and product are: " + f"{sum_n_product(1,1)}")

#5: alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold 
# functions in Python just like they can in JS. Alternatively, you can call a function from 
# inside another function.

alias_arb_args = arb_args
alias_arb_args("d", "e", "f")

#6: arb_mean - Accepts any number of integers and prints their average.

def arb_mean(*args):
    total = 0
    for a in args:
        total += a
    print("#6: The mean is: " + f"{a/len(args)}")
arb_mean(1,5,10)

#7: arb_longest_string - Accepts any number of strings and returns the longest one.

def arb_longest_string(*args):
  long = 0
  longest = ""
  for a in args:
    if len(a) > long:
      long = len(a)
      longest = a
  return longest
print("#7: The longest string is: ", arb_longest_string("hello", "what", "no"))