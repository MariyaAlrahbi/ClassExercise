import re

mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
#compile the RE
r = re.compile(".*cat")
#use filter the check all items
#filter returns iterator, need to convert it to list for printing 
newlist = list(filter(r.match, mylist)) 
print(newlist)

newlist = list(filter(lambda animal: re.match(".*cat", animal), mylist))
length = list(map(lambda a: len(a) ,newlist))
print(newlist)
print(length)

