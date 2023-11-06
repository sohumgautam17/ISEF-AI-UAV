def main():
    number = get_number()
    say(number)
    
def get_number():
    while True:
        n = int(input("What is your favorite number: "))
        if n > 0: 
            return n

def say(n):
    for _ in range(n):
        print ("Hello")
    
main()