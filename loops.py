x = 1
for i in range(0,9):
    print ("* " * x)
    if i >= 4:
        x-=1
    else:
        x+=1
print()

x = 5
for i in range(0,5):
    print("* " * x)
    x-=1
print()

x = 1
y = 8
for i in range(0,5):
    print((" " * y) + ("* " * x))
    x+=1
    y-=2
print()

x = 1
y = 5
for i in range(0,5):
    print((" " * y) + ("* " * x))
    x+=1
    y-=1
print()

x = 5
y = 1
for i in range(0,5):
    print((" " * y) + ("* " * x))
    x-=1
    y+=1
print()
