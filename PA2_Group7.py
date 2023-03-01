#Group7
#Dean Tran, Edwin Rodriguez, Elisa Shukuru
#02/22/2023
"""the purpose of the programming assignment is to calculates a customer’s monthly bill. It should ask which package the customer has
purchased and how many minutes were used."""

APricePerMonth = 29.99
ATime = 250
AAddTime = 0.27
BPricePerMonth = 39.99
BTime = 500
BAddTime = 0.23
CPricePerMonth = 49.99
CTime = 750
CAddTime = 0.21
DPricePerMonth = 59.99
DTime = 1000
DAddTime = 0.19
EPricePerMonth = 69.99
ETime = 0
EAddTime = 0

loop = True
customerPackage = ""
customerTime = 0
monthlyBill = 0

customerPackage = input("Enter the package you have purchase: ")#Ask customer to enter the purchased package name

while loop:
    if (customerPackage != "A" and customerPackage != "B" and customerPackage != "C" and customerPackage != "D" and customerPackage != "E"):
        customerPackage = input("Invalid input. Please enter again (exampe: A, B, C, D, E): ")#Ask customer to enter again if the package name is invalid
    else:
        break

customerTime = int(input("How many minutes did you use?: "))#Ask customer to enter the number of minutes used

while loop:
    if customerTime < 0:
        customerTime = int(input("Number of minutes cannot be negative. Please enter again: "))#Ask customer to enter again if the number of minutes is negative
    else:
        break

if customerPackage == "A":#customer chooses package A
    if customerTime > ATime:#calculate monthly bill if the number of minutes used is larger than the provided minutes
        monthlyBill = APricePerMonth + (AAddTime * (customerTime - ATime))
    else:
        monthlyBill = APricePerMonth#calculate monthly bill if the number of minutes used is smaller than the provided minutes 
elif customerPackage == "B":#customer chooses package B
    if customerTime > BTime:#calculate monthly bill if the number of minutes used is larger than the provided minutes
        monthlyBill = BPricePerMonth + (BAddTime * (customerTime - BTime))
    else:
        monthlyBill = BPricePerMonth#calculate monthly bill if the number of minutes used is smaller than the provided minutes 
elif customerPackage == "C":#customer chooses package C
    if customerTime > CTime:#calculate monthly bill if the number of minutes used is larger than the provided minutes
        monthlyBill = CPricePerMonth + (CAddTime * (customerTime - CTime))
    else:
        monthlyBill = CPricePerMonth#calculate monthly bill if the number of minutes used is smaller than the provided minutes 
elif customerPackage == "D":#customer chooses package D
    if customerTime > DTime:#calculate monthly bill if the number of minutes used is larger than the provided minutes
        monthlyBill = DPricePerMonth + (DAddTime * (customerTime - DTime))
    else:
        monthlyBill = DPricePerMonth#calculate monthly bill if the number of minutes used is smaller than the provided minutes 
elif customerPackage == "E":#customer chooses package E
    monthlyBill = EPricePerMonth#calculate monthly bill

print(f"your monthly bill is: ${monthlyBill}")#Display the monthly bill


