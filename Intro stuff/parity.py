#x = int(input("What is x?"))

#if x % y ==0:
 #   print("x is Even")
#else:
  #  print("x is Odd")

def main():
    x = int(input("What is x?"))
    if is_even(x):
        print("X is even")
    else:
        print("X is odd")
        
        
def is_even(n):
#ITeration 1 
    #if n%2 ==0:
        #return True
    #else:
        #return False
# Iteration 2
    #return True if x % 2 == 0 else return False
    return  n % 2 ==0

main()
