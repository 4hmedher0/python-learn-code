class A(object): #default is object
    def __init__(self):
        print('you are in A \n')
class B(A):
    pass
class C:
    def __init__(self):
        print("YOU ARE IN C")
class D(C,B):
    pass
d=D()
#print(d)
#a=A()
#print(a)
print(D.mro())
    
