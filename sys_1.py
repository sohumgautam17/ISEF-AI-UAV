import sys

#check for errors 
if len(sys.argv) <2:
    sys.exit ("Too few arguments")

for name in sys.argv[1:]:
    print("Hello, my name is", name)
