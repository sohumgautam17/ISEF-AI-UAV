
# Saying hello to user
name = input("What is \'your\' name?").strip().title()

#Capitalze name 
# #name = name.title()

first, middle, last,  = name.split(" ")

#Using parameters sep="" and end = " "
print(f"Hello, {first}")


# {} - Format string (e.g. print(f"hello, {name}"))  -- Put an f at the begining



