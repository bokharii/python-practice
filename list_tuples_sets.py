### lists
courses = ['history', 'math', 'physics', 'biology']
print(courses)

# print(courses[0]) # access a index using []

# print(len(courses)) # get length uses len() fn

# print(courses[-2]) # use negative indexes start from the end

# print(courses[0:2]) # get items in the list from index 0 (inclusive) up to but NOT INCLUDING index 2
# if we just do courses[:2] it assumes we want to start at the beginning and go up to index 2
# similarly, if we do courses[2:] it assumes we want to start at index 2 and go all the way to the end of the list
# print(courses[2:])

## adding items to our list
# courses.append('art') # append adds item to the end of the list
# print(courses)
# courses.insert(0, 'art') # insert allows us to add the item at a specific index
# print(courses)

courses_2 = ['art', 'sports']
courses.extend(courses_2) # extend allows us to append a list's items to another list without adding that actual list
print(courses)

## removing items from our list
courses.remove('math') # remove method removes a specific item
print(courses)

popped = courses.pop() # pop method removes the last item in the list. popped item can be saved in a variable
print(popped)

## sorting lists
courses.reverse() # reverses the list
print(courses)

courses.sort() # sorts the list (alphabetical if strings, ascending if numbers)
print(courses)