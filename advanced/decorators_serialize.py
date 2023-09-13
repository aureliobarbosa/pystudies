#!/usr/bin/python3 
#
#
#
#

def serialize(func):
    def wrapper(*args, **kwargs):
        print("Serializing")
        val = func(*args, **kwargs)
        print("End")
        return val
    return wrapper

@serialize
def increment(x,b=1):
    return x + b

# test = serialize(increment)

print( increment(1,3) )