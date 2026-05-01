#operators

# Arithmatic Operators
# x= 10
# y=3
# print(x + y)
# print(x- y)
# print(x*y)
# print(x/y)
# print(x//y) #floor division
# print(x%y) #modulo
# print(x**y) #exponential or power

# Assignment operator

# n= 10
# n +=5
# print(n)
# n*=5
# print(n)
#
# n -=3
# print(n)
#
# n /=5
# print(n)
# n%=5
# print(n)
# n**=5
# print(n)

# Comparison Operator

a=5
b=10

print(a > b) #false
print(a < b) #true
print(a == b) #false
print(a != b) #true
print(a >= b) #false
print(a <= b) #true

#  Logical operators

c= True
d= False

print(c and d)
print(not c)
print(not d)
print(c or d)
print(not c)
print(not d)

# membership op

my_list= [1,2,3,4,5,6]
print(3 in my_list)
print(0 not in my_list)
print(4 not in my_list)

# Identity Op

xx=[1,2,3]
yy=[1,2,3]
zz=xx
print(xx is zz)
print(xx is not yy)
print(xx == yy)

import pyttsx3
engine= pyttsx3.init()
# engine.say("Hello Yunus")
# engine.runAndWait()
# engine.say("Khairyat se hai")
# engine.runAndWait()y7
engine.say("Alhamdulillah")
engine.runAndWait()
engine.say("Assalamu alaikum")

num= int(input("Enter number: "))
if 10 <= num <= 50:
    print("This number is between 10 and 50")
else:
    print("This number is not between 10 and 50")

