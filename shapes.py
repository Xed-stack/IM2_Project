import math

# rows = int(input("Enter a number for rows: "))
rows = 5
for i in range(1, rows+1):
    print(" * " * rows)

print("Right triangle")
for j in range(1, rows+1):
    print("*" * j)

print("Left triangle")
for k in range(1, rows+1):
    print(" " * (rows - k) + "*" * k)

print("Inverted right triangle")
for l in range(rows, 0, -1):
    print(" " * (rows-l) + "*" *l)

print("Inverted left triangle")
for m in range(rows, 0, -1):
    print( "*" * m + " " * (rows - m) )

print("Pyramid")
for n in range(1, rows+1):
    print(" " * (rows-n) + "*" * (2*n-1))

print("Inverted pyramid")
for o in range(rows, 0, -1):
    print(" " * (rows - o) + "*" * (2*o -1))

# mess = "Python for beginners"
# print(mess.title())

# temp = 22
# if temp >= 30:
#     print("Enet")
# elif temp <= 20:
#     print("Lameg")
# else:
#     print("Normal")

# weight = int(input("Enter your weight: "))
# unit = input("(K)g or (L)bs: ").lower()
# if unit == 'k':
#     converted = weight / 0.45
#     print(f"You are {math.ceil(converted)} pounds")
# elif unit == 'l':
#     converted = weight * 0.45
#     print(f"You are {math.ceil(converted)} kilograms")
# else:
#     print("Invalid unit")

str = "Mike Acosta"
print(str[::-1])  # start:stop:step

# for x in range(1, 11):
#     for y in range(11, x-1, -1):
#         print(f"{y} ", end=" ")
#     print()

# for x in range(0, 10):
#     for y in range(0, 10):
#         if (x % 2):
#             print(f"{y} ", end=" ")
#         else:
#             print(f"{y*2} ", end=" ")
#     print()

while(True):
    num = int(input("enter a number: "))
    if num == 0:
        print("Exiting...")
        break