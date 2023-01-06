'''
The main difference between them is, the return statement terminates the execution of the function. 
Whereas, the yield statement only pauses the execution of the function. 
Another difference is return statements are never executed. whereas, yield statements are executed when the function resumes its execution.
'''

def func(x):
    for i in range(x):
        return i


def funcy(x):
    for i in range(x):
        yield i
print(func(5))
print(funcy(5))


