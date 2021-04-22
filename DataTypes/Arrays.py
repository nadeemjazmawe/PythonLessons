# List:
var = []  # create list
a = ['one', 2, 'orange']  # it's mutable

print(a[2])
a[1] = 'Hello World'
a.append(3214)
print(a)

# to remove from list , you can use one of these methods:
a[2] = []  # it onlu empties the contents card
a.remove(3214)
a.pop(0)

print(a)

# Tuples
b = ('one', 2, 'orange', '3214')  # it's immutable
print(b)

# Dictionaries
c = {}
d = {'first': 'one', 'fifth': 'orange', 'mike': 'josh'}
print(d)
print(d['fifth'])
print(d['mike'])
