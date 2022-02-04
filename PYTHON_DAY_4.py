# CODE 1:
# command to take input number from user
num=int(input('enter a number: '))
# defined function factorial that take input number as arguement
def factorial(num):
    factorial = 1
    if num < 0:
        print('No factorial Exists')
    elif num==0:
        print('factorial is 1')
    else:
        for i in range(1,num+1):
          factorial=factorial*i
        print('Factorial of',num,'is',factorial)
# command to call function
factorial(num)

# CODE 2:
# command to take input number from user
num=int(input('enter a number: '))
# defined function factorial that take input number as arguement
def factorial(num):
    return 1 if num==0 or num==1 else num*factorial(num-1)
print('Factorial of',num,'is',factorial(num))
 
            
