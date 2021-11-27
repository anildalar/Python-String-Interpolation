# Comment

name = "Anil"
name = 'Poonum' #overwrite
name2 = "Devendra"
name3 = 'Sokin'
name4 = 'Yogesh'
name5 = 'Rohit'

print("Hello "+name+", Welcome to PYthon Course")
print(f"Hello { name2 }, Welcome to PYthon Course")
print("Hello %s, Welcome to PYthon Course"%(name3))

# Str.format() Python Comment
print("Hello {}, Welcome to PYthon Course and {}".format(name4,name5))

# from something import someLibrary

from string import Template

name6='Aakash'
new = Template('Hello $name, Welcome to PYthon Course')
print(new.substitute(name=name6))

