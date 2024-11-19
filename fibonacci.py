# fibonacci sequence solution in python 
def fibonacci(n):
    # handle base case
    if n <= 0:
        return 0 # fibonacci(0) = 0
    if n <= 1:
        return 1 # fibonacci(1) = 1
    
    # initialize the first two fibonacci numbers 
    prev, curr = 0, 1 