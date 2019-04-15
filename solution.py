number1, number2, number3 = input("Enter three integer numbers : ").split()
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
temp = 0

if number1 > number2:
    temp = number1
    number1 = number2
    number2 = temp
    
if number2 > number3:
    temp = number2
    number2 = number3
    number3 = temp
    
if number1 > number2:
    temp = number1
    number1 = number2
    number2 = temp

print("Numbers in descending order :", number3, number2, number1)
