import numpy as np
class matrix_airthmatic:
    def __init__(self, m1, m2):
        self.m1=m1
        self.m2=m2
    def addition(self):
        return self.m1+self.m2
    def substraction(self):
        return self.m1-self.m2
    def multiply(self):
        return self.m1 @ self.m2

m1=np.array(list(map(int,input("Enter Elements of Matrix 1 : ").split()))).reshape(3,3)
m2=np.array(list(map(int,input("Enter Elements of Matrix 2 : ").split()))).reshape(3,3)
cal=matrix_airthmatic(m1,m2)
print(cal.multiply())