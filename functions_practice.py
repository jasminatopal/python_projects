# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello():
    print("welcome user")

hello()
    

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack(x, y, z):
    return [x, y, z]

print(pack("x", "y", "z"))

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.

my_meal = ['salad', 'sandwich', 'cookie']

def eat_lunch(my_meal):
  if len(my_meal) == 0:
   print("My lunchbox is empty!")
  else:
    for i in range(len(my_meal)):
      if i == 0:
        print(f"First I eat {my_meal[0]}")
      else:
        print(f"Next I eat {my_meal[i]}")

eat_lunch(my_meal)


