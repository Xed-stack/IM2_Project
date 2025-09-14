print("Hello, World!")
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")

# for y in range(1, 6):
#     print(" " * (6-y) + "*" * y)

name = input("enter your name: ")
print(f"Hello, {name}!")

#cases--------------------------------------------------
for i in name:
    print(i, end =" ")

    match i.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print(" is a vowel")
        case " ":
            print("")
        case _:
            print(" is a consonant")
#---------------------------------------------------------

#right triangle ------------------------------------------
rows = int(input("Enter the number of rows: "))
for i in range(1, (rows+1)):
    print("*" * i)
#---------------------------------------------------------

#invereted na right Triangle ------------------------------------------------------
baliktad = int(input("Enter the number of rows: "))
for y in range(1, baliktad+1):
    print(" " * (baliktad-y) + "*" * y )

print("\nInverted pa left")
for z in range(rows, 0, -1):
    print("*" * z)

print("Inverted pa right")
for a in range(rows, 0, -1):
    print(" " * (rows-a) + "*" * a)
#----------------------------------------------------------------------

#pyramid ----------------------------------------------------------
pyramid = int(input("Enter a number of rows for the pyramid: "))
for b in range(1, pyramid +1):
    print(" " * (pyramid - b) + "*" * (2 * b - 1))

print("Inverted")
for c in range(pyramid, 0, -1):
    print(" " * (pyramid-c) + "*" * (2 * c -1))