# Global scope

name = "Robert"

# Local scope
def call(lastName):
  color = "Crimson"
  print(color)
  print(name)
  print(lastName)

call("Anderson")

count = 1

def global_count():
  # It is necessary to do this if you want to modify a global variable
  global count
  count += 1
  print(count)

  color = "rebeccapurple"

  def color():
    # It is necessary to do this if you want to modify a parent variable
    nonlocal color
    color = "royalblue"
    print(color)

  color()

global_count()