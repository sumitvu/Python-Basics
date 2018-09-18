"""using split function"""

c='sumit.vu@gmail.com'

uname,domain=c.split('@')

print(uname)
print(domain)

"""length of string"""
s='sinhgad college'

print(len(s))

"""string traversal"""

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)


print(s[:])


"""string find"""

word = 'banana'
index = word.find('a')

print(index)

index=word.count('a')
print(index)

