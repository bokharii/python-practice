# print("hello world")

# m = """hi
# my name is "saaquib bokhari" whats
# up"""

message = "Hello World!"
print(len(message))

# print(m[0:2])
print(message[:5])

### string methods
print(message.lower())  # lowercase
print(message.upper())  # uppercase

print(message.count("l"))  # counts how many times something appears in a string

print(
    message.find("l")
)  # finds the first index of where the character/word appears in a string
print(message.find("p"))  # returns -1 if it doesn't exist in the string

# replaces the first argument with the second argument.
new_message = message.replace(
    "World", "Universe"
)  # needs to be saved to a new variable since the replacement does not happen in-place
print(new_message)


# string concatenation
name = "Saaquib"
# print(message + ' ' + name)

# with placeholders
concatenation = 'Hello {}! {}'.format(name, message)
# print('concatenated string: ', concatenation)

# new method using f strings
new_concatenation = f'Using f-strings. Hello {name.upper()}! {message}'
print(new_concatenation)

# dir() function returns the list of valid attributes/methods for a specified object
print(dir(name))

# help gives us info on those methods
# (print(help(str)))