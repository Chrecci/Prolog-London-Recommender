# The code here will ask the user for input based on the askables. It will only ask the user where necessary.

# Import necessary packages
import tempfile
from pyswip.prolog import Prolog
from pyswip.easy import *

prolog = Prolog() # Global handle to interpreter

retractall = Functor("retractall")
known = Functor("known",3)

# Define foreign functions for getting user input and writing to the screen
def write_py(X):
    print(str(X))
    sys.stdout.flush()
    return True

'''def read_py(A,V,Y):
    print('read', A,V,Y)
    if isinstance(Y, Variable):
        response = input(str(A) + " is " + str(V) + "? ")
        print(f"User answered {str(A)} is {str(V)}.")
        Y.unify(Atom(response))
        print(Y, response)
        return True
    else:
        return False'''

input_str=['chill', 'yes', 'no']

# vibe can be drop down list
# value can be slider
# minutes can be slider

def read_py(A,V,Y):
    Y.unify(Atom(input_str[read_py.counter]))
    read_py.counter += 1
    return True

write_py.arity = 1
read_py.arity = 3

registerForeign(read_py)
registerForeign(write_py)
read_py.counter = 0
prolog.consult("KB.pl") # open the KB for consulting

call(retractall(known))

problem = [s for s in prolog.query("activity(X).", maxresult=1)]
# print('yo', list(prolog.query("activity(X).", maxresult=1)))
# print(problem)
print("Your problem is " + (problem[0]['X'] + "." if problem else "unknown."))