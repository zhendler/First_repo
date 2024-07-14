
def caching_fibonacci(cache_size=10):

    cache = {}
    for i in range(cache_size):
        cache[i] = fibonacci_recursive(i)

    def fibonacci(n):
        if n <= 0:  
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    #fib_list=[num for num in cache.values()]
    #print(fib_list)
    return fibonacci

def fibonacci_recursive(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
  

fib = caching_fibonacci()
#fib_rec=fibonacci_recursive(10)


print(f'fib caching {fib(3)}')  
print(f'fib caching {fib(6)}')  
