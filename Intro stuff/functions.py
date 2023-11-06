def greet():
    name = input("Whats your name?")
    hello(name)
    ask = input("How are you doing?").lower()
    response(ask)


def hello(to = "Hello!"):
    print("Hello,", to)


def response(reply = "Great!"):

    print("Im glad you're", reply + "!")

greet()