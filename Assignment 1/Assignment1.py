# Question 1
print('Hello My name is "Kaustabh". I love Coding')
print("This is 'my first program'.")

x = input("x = ")
print(x)
y = input("y = ")
print(y)
z = input("z = ")
print(z)

print('User entered x=' + x + ', y=' + y + ', z=' + z)
print('Output: Value1 =' + x + ', Value2 =' + y + ', Value3 =' + z)

print('Type of Value1 ', type(x))
print('Type of Value2 ', type(y))
print('Type of Value3 ', type(z))

# Question 2
print('Hello! My name is Kaustabh')
print('"Hello I am a candidate"')
print('"234.56"')
print('"34"')
print('a + 3j')


# Question 3
x = 10+20*(45+67.0)
print(x)
print("Type of x: ", type(x))

x = (True and False) or False
print(x)
print("Type of x: ", type(x))

x = (True or True) and (not False and True)
print(x)
print("Type of x: ", type(x))

x = (3>89) or (34>32)
print(x)
print("Type of x: ", type(x))

x = not True and False
print(x)
print("Type of x: ", type(x))

# Question 4
x = int(input('Enter a number: '))
print(x)

if (x%2 == 0) and (x%5 == 0):
	print("Hurray it is what I am looking for")

else: 
	print("wrong input")

# Question 5
a = range(10, 50)
x = int(input("Enter a number: "))

if x in a:
	print("Yes I am in the range")

else:
	print("Oops")