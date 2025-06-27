#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Q1)  What is the difference between a function and a method in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


ANS- A function is a standalone block of code that does a task. 
A method is a function that belongs to an object and acts on that object's data.


# In[1]:


def greet():  # Function
    print("Hello")

name = "Prakhar"
name.upper() Method (works on string object)


# In[ ]:


get_ipython().set_next_input('Q.2) Explain the concept of function arguments and parameters in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Ans-Parameters are the labels or names inside the parentheses when you create a function. They're like empty boxes waiting for something. Example: def greet(name): (Here, name is a parameter)

Arguments are the actual pieces of information you send to the function when you use it. They're the stuff you put into those boxes. 
Example: greet("Prakhar") (Here, "Prakhar" is an argument) 
    So, you define a function with parameters, and you call a function with arguments.


# In[2]:


def add(a, b):  # a and b are parameters
    return a - b

result = add(10, 3) # 10 and 3 are arguments
print(result)


# In[ ]:


get_ipython().set_next_input('Q.3)  What are the different ways to define and call a function in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Ans-Using def: This is the main way. You give your function a name, and then list any inputs it needs in parentheses.
*Using lambda: This is for very short, unnamed functions that do just one thing. Calling a Function:
Basic Call:   Just type the function's name followed by parentheses.
Positional Arguments: You put the inputs in the exact order the function expects them.
Keyword Arguments: You name each input when you pass it, so the order doesn't matter.
Default Arguments: Some inputs already have a preset value; you only provide them if you want a different one.
Arbitrary Arguments (*args and **kwargs):
args: Allows you to give the function any number of regular, unnamed inputs.
kwargs: Allows you to give the function any number of named inputs.


# In[3]:


# using def
def square(x):
    return x * x
print(square(4))

# Using lambda
square_lambda = lambda x: x * x
print(square_lambda(4))


# In[ ]:


get_ipython().set_next_input('Q.4) What is the purpose of the return statement in a Python function');get_ipython().run_line_magic('pinfo', 'function')


# In[ ]:


Ans-An Iterable is anything you can loop over (like a list, tuple, string, dictionary). 
It's a collection of items that can be gone through. You can get an iterator from it.


An Iterator is an object that keeps track of its current position and gives you the next item one by one when asked. 
It's the "navigator" that guides the loop through the iterable. 
Difference: An iterable is the collection, while an iterator is the tool that goes through that collection item by item.


# In[4]:


# Iterable
my_list = [25, 30, 50]

# Convert iterable to iterator
my_iter = iter(my_list)

# Use iterator
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# In[ ]:


get_ipython().set_next_input('Q-6) Explain the concept of generators in Python and how they are defined');get_ipython().run_line_magic('pinfo', 'defined')


# In[ ]:


Ans-What they are: Generators are special types of functions that allow you to create iterators in a simple way. 
    Instead of producing all results at once and storing them (which can use a lot of memory), generators produce results one at a time, only when requested. 
    They "generate" values on the fly. 
    How they are defined: You define a generator just like a normal function, but instead of using the return keyword to send a final result, you use the yield keyword. 
    Each time yield is encountered, the generator produces a value and pauses its execution, resuming from where it left off the next time a value is requested.
    What they are: Generators are special types of functions that allow you to create iterators in a simple way. 
        Instead of producing all results at once and storing them (which can use a lot of memory), generators produce results one at a time, only when requested. They "generate" values on the fly. 
        How they are defined: You define a generator just like a normal function, but instead of using the return keyword to send a final result, you use the yield keyword. 
        Each time yield is encountered, the generator produces a value and pauses its execution, resuming from where it left off the next time a value is requested.


# In[5]:


# example of generator :
def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count  # Yielding a value and pausing the function
        count += 1

# Using the generator
counter = count_up_to(3)

print(next(counter))
print(next(counter))
print(next(counter))
     


# In[ ]:


get_ipython().set_next_input('Q-7) What are the advantages of using generators over regular functions');get_ipython().run_line_magic('pinfo', 'functions')


# In[ ]:


Ans- Memory Efficiency: They don't store all results in memory at once. They produce values one by one, only when needed, which is great for large datasets or infinite sequences.
    
Performance (Lazy Evaluation): They generate values on demand, meaning computation only happens when you ask for the next item. This can make your code run faster if you don't need all results immediately.
    
Simplicity: They allow you to write elegant and concise code for creating iterators


# In[6]:


def first_n_numbers(n):
    """A regular function that returns a list numbers."""
    number = []
    for i in range(n):
        number.append(i)
    return number

def first_n_numbers_generators(n):
    """A generator function that yields numbers."""
    for i in range(n):
        yield i
# Using the regular function
large_list = first_n_numbers(1000000)
print(f"sum of large_list: {sum(large_list)}")

# Using a generator
large_generators = first_n_numbers_generators(1000000)
print(f"sum of large_generators: {sum(large_generators)}")


# In[ ]:


get_ipython().set_next_input('Q-8)  What is a lambda function in Python and when is it typically used');get_ipython().run_line_magic('pinfo', 'used')


# In[ ]:


Ans- A lambda function in Python is a small, anonymous function defined with a single expression. 
It's typically used for:
Simple, one-time tasks: When you need a quick function for a short operation.
    
As an argument to higher-order functions: Often used with functions like map(), filter(), sorted(), or functools.reduce() where a small function is needed temporarily.


# In[7]:


square = lambda x: x * x
print(square(5))


# In[ ]:


get_ipython().set_next_input('Q-9) Explain the purpose and usage of the map() function in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Ans- The map() function in Python is used to apply a given function to every item of an iterable (like a list or tuple) and return an iterator that yields the results. 
Purpose: It's a concise way to transform all items in a collection without writing an explicit loop. 
    Usage: You provide map() with the function you want to apply and the iterable you want to apply it to.


# In[8]:


# Squaring each element of a list
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))


# In[ ]:


get_ipython().set_next_input('Q-10)  What is the difference between map(), reduce(), and filter() functions in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Ans- Here's the difference between map(), reduce(), and filter():
map(): Transforms items. It applies a function to each item in a sequence and produces a new sequence of the results. 
    Think of it as a one-to-one conversion for every item.
    
filter(): Selects items. It builds a new sequence by including only those items from the original that satisfy a specific condition (i.e., for which a given function returns True). 
    It's about picking out relevant items.
    
reduce(): Aggregates items. It applies a function cumulatively to the items of a sequence, reducing the sequence to a single value. 
    Think of it as combining all items down to one result (like summing or finding a maximum). (Note: reduce is in the functools module).


# In[ ]:


# Map ()

numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))


# Filter ()

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))


# Reduce ()

from functools import reduce
numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)


# In[ ]:


Q-11) Using pen & Paper write the internal mechanism for sum operation using reduce function on this given list:[47,11,42,13]?


# Ans- ![WhatsApp%20Image%202025-06-27%20at%201.56.51%20PM.jpeg](attachment:WhatsApp%20Image%202025-06-27%20at%201.56.51%20PM.jpeg)

# In[ ]:


PRACTICAL QUESTIONS


# In[ ]:


get_ipython().set_next_input('Q-1) Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list');get_ipython().run_line_magic('pinfo', 'list')


# In[ ]:


Ans- def sum_even_numbers(numbers):
    total = 0  # Initializes a variable to store the sum
    for num in numbers:  # Iterates through each number in the input list
        if num % 2 == 0:  # Checks if the current number is even
            total += num  # Adds the even number to the total
    return total  # Returns the final sum.


# In[ ]:


Q-2) Create a Python function that accepts a string and returns the reverse of that string.?


# In[4]:


Ans)def reverse_string(s):
    return s[::-1]
Example-
print(reverse_string("hello"))
print(reverse_string("Python"))
print(reverse_string("12345"))


# In[ ]:


Q-3) Implement a Python function that takes a list of integers and returns a new list containing the squares of each number?.


# In[8]:


Ans)def square_numbers(numbers):
    return [num ** 2 for num in numbers]

* Example
print(square_numbers([1, 2, 3, 4]))


# In[ ]:


Q-4) Write a Python function that checks if a given number is prime or not from 1 to 200?


# In[9]:


Ans- def is_prime(n):
  if n < 2: return False
  for i in range(2, n):
    if n % i == 0: return False
  return True

for num in range(1, 201):
  if is_prime(num): print(num, end=",")


# In[ ]:


Q-5) Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms.


# In[ ]:


Ans)class FibonacciIterator:
    def _init_(self, num_terms):
        self.num_terms = num_terms
        self.a, self.b = 0, 1
        self.count = 0

    def _iter_(self):
        return self

    def _next_(self):
        if self.count < self.num_terms:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration
     


# In[ ]:


get_ipython().set_next_input('Q-6) Write a generator function in Python that yields the powers of 2 up to a given exponent');get_ipython().run_line_magic('pinfo', 'exponent')


# In[ ]:


Ans- def powers_of_2(max_exponent):
  """
  Generates powers of 2 up to a given exponent.

  Args:
    max_exponent: The maximum exponent to go up to (inclusive).

  Yields:
    The next power of 2.
  """
  for i in range(max_exponent + 1):
    yield 2**i

# Example usage:
# for power in powers_of_2(5):
  print(power)


# In[ ]:


get_ipython().set_next_input('Q-7) Implement a generator function that reads a file line by line and yields each line as a string');get_ipython().run_line_magic('pinfo', 'string')


# In[ ]:


def read_file_lines(filename):
       """
   A simple generator to read a file line by line.
   """
   with open(filename, 'r') as file:
       for line in file:
           yield line.strip('\n') # Yield each line, removing the newline character


# In[9]:


with open("my_document.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is line two.\n")
    f.write("Last line.\n")
    for line read_file_lines("my_document.txt"):
    print(line)


# In[ ]:


Q-8)  Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.


# In[3]:


Ans8) # Our list of tuples
data = [('apple', 3), ('banana', 1), ('cherry', 2)]
data.sort(key=lambda x: x[1])
# Sort the list based on the second element of each tuple
# x[1] refers to the second element (index 1) of each tuple x
print(data)


# In[ ]:


get_ipython().set_next_input('Que-9) Write a Python program that uses map() to convert a list of temperatures from Celsius to Fahrenheit');get_ipython().run_line_magic('pinfo', 'Fahrenheit')


# In[4]:


Ans9)def c_to_f(c):
  return (c * 9/5) + 32

celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(c_to_f, celsius_temps))

print("Celsius:", celsius_temps)
print("Fahrenheit:", fahrenheit_temps)


# In[ ]:


get_ipython().set_next_input('Que10) Create a Python program that uses filter() to remove all the vowels from a given string');get_ipython().run_line_magic('pinfo', 'string')


# In[5]:


Ans10) def is_not_vowel(char):
  """Checks if a character is not a vowel."""
  return char.lower() not in 'aeiou'

input_string = "Hello World"
filtered_chars = filter(is_not_vowel, input_string)
result_string = "".join(filtered_chars)

print("Original string:", input_string)
print("String without vowels:",result_string)


# In[ ]:


Que11)Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

Order Number - Book Title and Author - Quantity - Price per Item

34587 - Learning Python, Mark Lutz - 4 - 40.95

98762 - Programming Python, Mark Lutz - 5 - 56.80

77226 - Head First Python, Paul Barry - 3 - 32.95

88112 - Einführung in Python3, Bernd Klein - 3 - 24.99

Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and the product of the price per item and the quantity. The product should be increased by 10,- € if the value of the order is smaller than 100,00 €.

Write a Python program using lambda and map.


# In[6]:


Ans11) orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einführung in Python3, Bernd Klein', 3, 24.99]
]

result = list(map(lambda item: (item[0], item[2] * item[3] + 10) if item[2] * item[3] < 100 else (item[0], item[2] * item[3]), orders))

print(result)

