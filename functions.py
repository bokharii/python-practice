# ### functions defined using def
# def hello_func():
#   pass # syntactic placeholder that literally does nothing when executed. useful for when you want to sketch out your fn

# print(hello_func) # need () to execute the fn

# def hello_func():
#   print('Hello Function!')


# def hello_func():
#     return "Hello Function!"


# yo = hello_func().lower()
# print(yo)


def hello_func(name = 'person'): # allow for a parameter. = allows for a default parameter if none is passed
  return f'Hello {name}!'

print(hello_func()) # pass in argument
print(hello_func('Saaquib'))