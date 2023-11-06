names = input("What is ur name: ")
#use with so I dont ahve to say file.close
with open("names.txt", "a") as file:
    file.write(f"{names}\n")