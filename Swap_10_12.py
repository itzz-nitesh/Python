print('''
Given A=10 and B=12
''')

A=10
B=12

def codeA():             # codeA and codeB are independent function from each other
    A=B
    print("A=",A)

def codeB():
    B=A
    print("B=",B)

print('''
After swaping values are
''')
codeA()
codeB()
