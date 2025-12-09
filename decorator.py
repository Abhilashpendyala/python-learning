import time

def prepost(func):
    def wrapper(*args):
        print("can you think of the answer, i will give you 5 seconds to think ")
        time.sleep(5)
        ans=func(*args)
        print(ans)
        print("what are you thoughts, did you get that correct??")
    return wrapper

@prepost  # result=prepost(result)
def result(a,b):
    return a+b

result(4,5)