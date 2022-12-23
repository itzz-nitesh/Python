
unit=float(input("Enter Electricity Unit: "))


# For 0-100 Unit @3.7
a1=0
if(unit>100):
    a1=100           # here a1= No. of unit
elif(unit>=0):
    a1=unit
A=3.7*a1             # here A= Amount(Rs.) of slab 0-100


# For 101-200 Unit @3.9
b1=0
if(unit>200):
    b1=100         
elif(unit>=101):
    b1=(unit-100)
B=3.9*b1       


# For 201-400 Unit @5.3
c1=0
if(unit>400):
    c1=200           
elif(unit>=201):
    c1=(unit-200)
C=5.3*c1            


# For 401-600 Unit @6.3
d1=0
if(unit>600):
    d1=200           
elif(unit>=401):
    d1=(unit-400)
D=6.3*d1            


# For 601-above Unit @7.9
e1=0
if(unit>600):
    e1=(unit-600)         
elif(unit<=600):
    e1=0
E=7.9*e1          


print('''
 Electricity Bill Calculator

 Unit_Slabs    Rate     Amount
 ''')
print(" 0-100         3.7     ",A)
print(" 101-200       3.9     ",B)
print(" 201-400       5.3     ",C)
print(" 401-600       6.3     ",D)
print(" 601-above     7.9     ",E)

print("\n Total Amount for",unit,"units :", (A+B+C+D+E),"\n")
