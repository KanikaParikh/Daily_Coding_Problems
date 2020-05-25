#Cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair respectively.
def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(f):
    def first(a,b):
        return a
    return f(first)

def cdr(f):
    def last(a,b):
        return b
    return f(last)

#print(car(cons(7,9)),cdr(cons(7,9)))