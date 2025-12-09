# classes : use them when you want statefulness
# multiple functions operating on same data, then use classes 
# if you want to store the state across the run time then use classes
# variables defined in functions are local to function and loses state once exited out of function
# objects create instances of the class, and stores the state in the object. 
# when you have multiple objects using same functions repeatedly, use classes
# functions only return single return value, classes can retrieve all functionalities of function for a particular function call, passed with parameters
# use classes when object has its real identity
# use classes when multiple independent objects are needed
# use classes when behavior and data belong together
# donot use classes just to group random functions

#--------------------------------------decorators-------------------------

# decorators decorate your main function by pre processing and post processing

### example ###

### understanding arguments to function and keyword arguments)

def call(*args):  # *args collects the inputs into tuple ,* converts input into list and stores to args
    print(type(args))
    for i in range(len(args)):
        print(f"{i},{args[i]}")

def call2(**kwargs):# **kwargs store the imput into dictionary of key value pairs, **convers input to dict
    for i in kwargs.keys():  # dict has keys and values method to retreive keys and values
        print(kwargs[i])

call("abhi","anvesh")
call2(abhi="abhicall2",anv="anvcall2")

### understanding decorators

def show(func):
    print("this is to just show off--> bofore main enters the party--> dec is responsible")
    func()

@show   ## decorater calls the decorator function and executed everything, it abstracts explicit calling of main function ----> similar to calling show(main)
def main():
    print("i have done this--> this comes from main functionality")

# show(main)---> optional way of calling a decorator
main()
##### how do you take control of this code ?? decorator is calling without your interference
#### hide the code in wrapper function
#### what does hidden function do ???
#### it doesn't get executed until called, functions are executed only when called
### when will it gets executed ?? and how the logic works
### inner function is only executed and returned when it is called explicitly
### how it is called ??

def show(func):
    def wrapper():
        print("this is to just show off--> bofore main enters the party")
        func()
    return wrapper 

@show   # main=show(main) called --> with wrapper function hiding the code
def main():
    print("i have done this--> this comes from main functionality")

#main()  ## decorator is called only when you call it now , unlike before