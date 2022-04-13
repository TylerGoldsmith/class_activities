#1: name_args - Accepts any number of named arguments and 
# prints them in the pattern key : value one at a time.

def name_args(**kwargs):
    for a in kwargs.keys():
        print(f"{a}:{kwargs[a]}")

name_args(a="a", b=12, bool=False, d="14")

#2: all_true - Returns True if all the elements in an 
# iterable are true. Hint: there is an existing 
# built-in function that could be very helpful here.

def all_true(iterable):
    return all(iterable)

print(all_true([True, True]))
print(all_true([True, False]))


#3: one_true - Returns True if one of the elements in 
# an iterable is true. Hint: there is an existing 
# built-in function that could be very helpful here.

def one_true(iterable):
    return any(iterable)

print(one_true([True, True]))
print(one_true([True, False]))
print(one_true([False, False]))



#4: recursive_factorial - Uses recursion to find the 
# factorial of an integer.

def recursive_factorial(n):
    if n <= 1:
        return 1
    else: 
        return n * recursive_factorial(n-1)

print(recursive_factorial(4))


#5: recursive_deduplicate - Recursively removes all 
# adjacent duplicate letters from a string.


def recursive_deduplicate(my_str,i=0):
  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    if my_str[i] == my_str[i+1]:
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
    else:
      return recursive_deduplicate(my_str,i+1)
      
print(recursive_deduplicate("aaadsfafsaa"))
print(recursive_deduplicate("aabasdfasfasa"))




#6: recursive_reverse - Uses recursion to reverse a
# string.

def recursive_reverse(str, i=0):
  if len(str)==0:
    return ""
  elif i == len(str)-1:
    return str[0]
  else:
    return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))


