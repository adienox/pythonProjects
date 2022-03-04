#Collatz sequence

def collatz(num): #creating a function to produce collatz sequence
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    else:
        print(3*num+1)
        return 3*num+1

print('Enter a number: ', end='') #Getting number from user
number = input()

try: #Input validation
    number = int(number)
    while number != 1: #Running the loop until the ending number is 1
        number = collatz(number)

except ValueError: #Handeling ValueError
    print('Enter an integer')
