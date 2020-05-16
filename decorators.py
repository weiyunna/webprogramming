def announce(f):
    def wrapper():
        print("about to the run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello World")

hello()
