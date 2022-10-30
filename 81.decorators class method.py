def my_decorator(fn):
    def mine():
        print("hi good morning")
        fn()
        print("hello good evening")
    return mine
    

def func1():
    print("my name is phanindra")
    print("my name is sunil kumar")


def func2():
    for i in range(10):
        print(i,end=" ")
        

def func3():
    print("hello yuvan good morning")
    


func1=my_decorator(func1)

func1()

func2=my_decorator(func2)

func2()

func3=my_decorator(func3)

func3()
