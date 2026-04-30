print("hello world")

# name= input("Enter your name: ")
# profession= input("Enter your profession: ")
# age= input("Enter your age: ")

# print("Hello " + name + ", " + profession + ", " + age)

# celsius = float(input("Enter your celsius: "))
# fahrenheit = (celsius * 9 / 5) + 32
# print("Your fahrenheit is:", fahrenheit)

print("-------------------------------------------------------")
print("Basic Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")
if operator == "+":
    result = num1 + num2
    print("Your result is:", result)
elif operator == "-":
    result = num1 - num2
    print("Your result is:", result)
elif operator == "*":
    result = num1 * num2
    print("Your result is:", result)
elif operator == "/":
     if num2 != 0:
        result = num1 / num2
        print("Your result is:", result)
     else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

#Lucky number
f_name= input("Enter name: ")
day= input("Enter day: ")

lucky_number= ord(f_name[0]) + ord(f_name[-1]) + int(day)


print("Your lucky number is:", lucky_number)


from datetime import date
birthYear= int(input("Enter birth year: "))
month= int(input("Enter month: "))
day= int(input("Enter day: "))
age= date.today().year - birthYear
print("Your age is:", age)

#variables, DT, if else

