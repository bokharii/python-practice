# https://www.youtube.com/watch?v=W8KRzm-HUcc
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

# courses.sort() # sorts the list (alphabetical if strings, ascending if numbers)
# print(courses)
numbers = [21, 25125, 11, 9, 85]
# numbers.sort()
numbers.sort(reverse=True) # reverse the order of the sorted list
print(numbers)

sorted_courses = sorted(courses) # sorted() fn returns a completely different sorted list, does not modify in-place like the .sort method
print(sorted_courses)

print(sum(numbers)) # sum, min, max functions all work with lists with numbers


## finding values in a list
print(courses)
print(courses.index('history')) # index method finds the index of the item we want in a list
print('art' in courses) # in allows us to see if a specified value is in the list. returns true/false

## looping values
for index, item in enumerate(courses): #enumerate allows us to get the index of the value in the loop
  print(index, item)

# to turn our list into a string of comma separated values...
course_str = ', '.join(courses) # use the join method
print(course_str)

# to turn our string back into a list...
course_list = course_str.split(', ')
print(course_list)


## Tuples
# lists are mutable, tuples are immutable
list1 = [231, 23, 1, 76, 9]
list2 = list1
# print(list1)
# print(list2)
list1[0] = 55 # changes the first element of BOTH list1 and list2 since they are mutable
print(list1)
print(list2)

# tuples use parenthesis instead of [] like lists
tuple_1 = (231, 23, 1, 76, 9)
tuple_2 = tuple_1

print(tuple_1, tuple_2)
# tuple_1[0] = 55 # results in TypeError because tuple elements are not mutable. thus a lot of normal list methods are not available to tuples
# print(tuple_1, tuple_2)


## Sets
# contains values that are unordered and have NO duplicates