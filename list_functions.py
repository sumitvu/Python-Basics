"""Syntax of list iterating through: mylist[from : to(excluded) : step(optional)]  """

first_list=[1,2,3,4,4,5,6,7,4]
"""count of a element of a list"""
cnt=first_list.count(4)
print(cnt)

"""finding a index of element"""
ind=first_list.index(4)
print(ind)

"""remove a element of a list"""
print(first_list.remove(4))

print(first_list)

"""adding a element to a list"""
first_list.append(9)

print(first_list)

"""sorting element of a list"""
first_list.sort()
print(first_list)

"""reverse order of a list element"""
print(first_list[::-1])

"""reverse order of a list element"""
first_list.reverse()

print(first_list)

"""counting length of a list"""

l=len(first_list)

print(l)

"""inserting a element at perticular index"""

first_list.insert(4,5)

print(first_list)

"""poping out a list element"""

first_list.pop(4)

print(first_list)

"""printing element of list from rear"""
print(first_list[3:-1])


print(first_list[-3:])

"""printing list element multiple times"""
second_list=first_list*2

print(second_list)

"""convert a string into list"""

s='spam'
t=list(s)
print(t)


"""The list function breaks a string into individual letters. If you want to break a string into
words, you can use the split method:"""

s = 'pining for the fjords'

t=s.split()

print(t)

s='pining-for-the-fjords'
delimiter='-'
t=s.split(delimiter)

print(t)

"""join is the inverse of split. It takes a list of strings and concatenates the elements. join is
a string method, so you have to invoke it on the delimiter and pass the list as a parameter:"""

t = ['pining', 'for', 'the', 'fjords']

delimiter=' '

s=delimiter.join(t)

print(s)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

""""

mylist[::] is the same as mylist[:] and mylist[::1] since it will give the whole array

mylist[::2] has step = 2 so it will take one every 2 from the array > ['a', 'c', 'e', 'g', 'i', 'k', 'm']"""

"""mylist[1::2] will start taking every two entries from index 1 (second entry) > ['b', 'd', 'f', 'h', 'j', 'l']"""

"""mylist[::-1] has step = -1 so it will output the whole array but in reverse order > ['m', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

mylist[::-2] will take one every two starting at the end in reverse order > ['m', 'k', 'i', 'g', 'e', 'c', 'a']"""