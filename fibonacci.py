# fibonacci sequence solution in python 
def fibonacci(n):
    # handle base case
    if n <= 0:
        return 0 # fibonacci(0) = 0
    if n <= 1:
        return 1 # fibonacci(1) = 1
    
    # initialize the first two fibonacci numbers 
    prev, curr = 0, 1 

    # loop to calculate fibonacci numbers up to n 
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr # update previous and current values 

        return curr # return the nth fibonacci number 
    
    print(fibonacci(4)) # output: 3