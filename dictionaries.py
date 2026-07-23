### dicts allow us to work with key-value pairs, like objects in js
students = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(students)

# can get a specific value we can use square brackets to specifiy the key
print(students["courses"])

# another way of accessing values using key - get method
print(
    students.get("hello", "Not Found")
)  # returns None if the key does not exist on the dict. for keys that don't exist we can pass in a second argument which makes that the default

## add/update new entry to dict
students["phone"] = "555-555-5555"
students["name"] = "Saaquib"
print(students)

# can also use the update method, which takes in a dictionary of everything we want to add/update with
students.update({'name': 'Bokhari', 'phone': '222-222-2222'})
print(students)

## delete an entry using a key
del students['age'] # using del
print(students)
# can also use pop method
courses = students.pop('courses')
print(students)
print(courses)

## looping through dictionary
print(len(students)) # gets length of dict
print(students.keys()) # gets all the keys
print(students.values()) # gets all the values
print(students.items()) # gets all key value pairs

for key, values in students.items(): # looping through a dict
  print(key, values)