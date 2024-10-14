#first decorators

def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

#declare use of decorator
@announce
#new function to run
def hello():
    print("Hello, World")

hello()