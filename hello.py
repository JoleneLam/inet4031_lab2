#!/usr/bin/env python3
a = 2
b = 2
c = a + b
print("Python says: Hello, World!")
print("%s + %s = %s" % (a,b,c))
listOfUsers = ["User1", "User2", "User3"];
for i, user in enumerate(listOfUsers):
    if i == len(listOfUsers) - 1:
            print(user)
    else:
            print(user, end=', ')
