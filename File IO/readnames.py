names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

 #Have to keep them 2 seperate things because we want to sort names, but
for name in sorted(names):
    print(f"Hello, {name}")

 