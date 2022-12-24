from functools import wraps

def triple(fn):
   @wraps(fn)
   def mul(x):
       print("ugrhg")
       result = fn(x)
       result*=3
       print(result)
   return mul




@triple
def double(x):
    x = x*2
    return(x)

double(4)