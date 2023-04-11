# Functions

def hello():
  print("Hey, there!")

hello()


def sum(num1=0, num2=0):
  if (type(num1) != int or type(num2) != int):
    return 0
  return num1 + num2

print(sum(2, 4))
print(sum(2, "oi"))

# Just like javascript spread operator, but instead of "..." it uses "*"
def multiple_items(*args):
  print(args)
  # args type is a tuple
  print(type(args))

multiple_items("Oi", 5, True)

# kwargs means key word arguments
def mult_named_items(**kwargs):
  print(kwargs)
  print(type(kwargs))

mult_named_items(message="Oi", number=45)