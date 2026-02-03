def my_function():
  print("Hello from a function")

my_function()

# Valid Function Name
# calculate_sum()
# _private_function()
# myFunction2()

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)