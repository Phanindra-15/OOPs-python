'''from time import time

def func1():
    x=999**9999

def func2():
    l=[x for x in range(99999)]

def func3():
    x=(66*99999)**999999


start_time=time()

func1()
end_time=time()

print(f'func1 took {end_time-start_time} seconds')


start_time=time()

func2()
end_time=time()

print(f'func2 took {end_time-start_time} seconds')

start_time=time()

func3()
end_time=time()

print(f'func3 took {end_time-start_time} seconds')
'''

#using decorator solving the above example


from time import time

def my_decorator(fn):
    def mine():
        start_time=time()
        fn()
        end_time=time()

        print(f'{fn.__name__} took {end_time-start_time}seconds')
    return mine

def func1():
    x=999**9999

def func2():
    l=[x for x in range(99999)]

def func3():
    x=(66*99999)**999999

func1=my_decorator(func1)
func1()

func2=my_decorator(func2)
func2()

func3=my_decorator(func3)
func3()


