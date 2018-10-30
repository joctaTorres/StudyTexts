'''
This files contains multiple basic recursive functions and algorithms
'''

def RecurviseFactorial():
    def factorial(n):
        if n == 0:
            return 1
        
        value = n * factorial(n-1)
        return value
    
    typedValue = input('Type the value to calculated its factorial: ')
    print(typedValue, '! = ', factorial(int(typedValue)), sep='')


def FindFibonacciElement():
    def fibonacci(n):
        if n <= 1:
            return n
        
        return fibonacci(n-1) + fibonacci(n-2)
    
    typedValue = input('Type the what element of Fibonacci to calculate: ')
    print('F(', typedValue, ') = ', fibonacci(int(typedValue)), sep='')


FindFibonacciElement()