def greet():
    print("Hello! Welcome to the currency converter.")

def convertCurrency(amount):
    
    piso = amount * 57.17
    yen = amount * 146.67
    return piso, yen

print()
greet()

currency = input("Enter amount in (USD): ")
cleaned = currency.split(",")
cleaned = [int(i) for i in cleaned]

print()
print("Dollar($)\tPeso(₱)\t\tYen(¥)")
for pera in cleaned:
    piso, yen = convertCurrency(pera)
    print(f"{pera}\t\t{piso:.2f}\t\t{yen:.2f}")
