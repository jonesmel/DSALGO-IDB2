'''
userInput=int(input("How Much money do you have?"))
wii=100
afford=int (userInput/wii)
mins = abs((userInput % wii)-wii)

print("You have ",userInput,"pesos")
print("You can buy wii", afford, "times")

if userInput < wii:
    print("You need ", mins,"more pesos if you are short")

'''

'''
sum = 0
for x in range(1, 11)
    print(sum, "Is the the sum of the numbers 1 - 10")
'''
'''
Input1=int(input("enter first number: "))
Input2=int(input("enter second number: "))
sum = 0

for x in range(Input1,Input2):
    sum = sum + x
print(sum, "is the total sum of ", Input1, " and ", Input2)
'''
'''
userInt=int(input("Enter a number: "))
factorial = 1
for x in range (1, userInt+1):
    factorial = factorial * x

print("The factorial of ", x, " is ", factorial)
'''

'''
userInput= int (input("Enter a number: "))
for x in range (1, userInput + 1):
    if userInput % x == 0:
        print(x)
'''
