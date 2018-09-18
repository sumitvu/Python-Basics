"""create simple tuple and print it"""

t1=(1,2,3,4,5,6)

print(t1)

"""create singleton tuple and print it"""

t2=('a',)

print(t2)

"""in-build tuple function"""
"""in-built tuple function takes only one argument"""
t=tuple('sumit')
print(t)

t3=tuple(range(6))
print(t3)

"""slicing the tuple"""

print(t[1:3])

print(t[1:-1])

"""using relational operators in tuple operations"""

"""Python starts by comparing
the first element from each sequence. If they are equal, it goes on to the next elements, and
so on, until it finds elements that differ. Subsequent elements are not considered (even if
they are really big)."""

if((0,1,2)<(0,3,4)):
    print('True')
else:
    print('False')

if((0,1,200000)<(0,3,4)):
    print('True')
else:
    print('False')


"""swapping tuple values"""

"""The left side is a tuple of variables; the right side is a tuple of expressions. Each value
is assigned to its respective variable."""
a=('sumit',)
b=('vu',)

a,b=b,a
print(a)
print(b)

"""tuple as return values"""

"""if you want to divide two integers
and compute the quotient and remainder, it is inefficient to compute x/y and then x%y. It
is better to compute them both at the same time.
The built-in function divmod takes two arguments and returns a tuple of two values, the
quotient and remainder. You can store the result as a tuple:"""

t4=divmod(7,3)
print(t4)

"""you can also use tuple assignment to store elements separately"""

quot,rem=divmod(7,3)
print(quot)
print(rem)

"""zip function"""

s = 'abc'
t = [0, 1, 2]
print(list(zip(s, t)))

"""If you need to traverse the elements of a sequence and their indices, you can use the built-in
function enumerate:"""

for index, element in enumerate('abc'):
    print(index,element)

"""The result from enumerate is an enumerate object, which iterates a sequence of pairs; each
pair contains an index (starting from 0) and an element from the given sequence."""

"""Dictionaries And Tuples"""

"""Dictionaries have a method called items that returns a sequence of tuples, where each
tuple is a key-value pair."""

d={'a':2,'b':3,'c':5}

t=d.items()
print(t)


t = [('a', 0), ('c', 2), ('b', 1)]
d=dict(t)

print(d)

"""Combining dict with zip yields a concise way to create a dictionary:"""

d=dict(zip('abc',range(3)))
print(d)


