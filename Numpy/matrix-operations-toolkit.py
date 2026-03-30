import numpy as np
class matrix_arithmetic:
    def __init__(self):
        pass
    def addition(self):
        n = int(input("Enter rows: "))
        m = int(input("Enter columns: "))
        m1=np.array(list(map(int,input("Enter Matrix 1 : ").split()))) 
        m2=np.array(list(map(int,input("Enter Matrix 2 : ").split())))
        if len(m1) != n*m and len(m2) != n*m:
            print("Invalid input size.")
        else :
            m3=m1+m2
            m3=m3.reshape((n,m))
            print(m3)
    def subtraction(self):
        n = int(input("Enter rows: "))
        m = int(input("Enter columns: "))
        m1=np.array(list(map(int,input("Enter Matrix 1 : ").split())))
        m2=np.array(list(map(int,input("Enter Matrix 2 : ").split())))
        if len(m1) != n*m and len(m2) != n*m:
            print("Invalid input size.")
        else :
            m3=m1-m2
            m3=m3.reshape((n,m))
            print(m3)
    def multiply(self):
        n = int(input("Enter rows of 1st matrix: "))
        m = int(input("Enter columns of 1st matrix: "))
        r = int(input("Enter row of 2nd matrix: "))
        m1=np.array(list(map(int,input("Enter Matrix 1 : ").split())))
        m2=np.array(list(map(int,input("Enter Matrix 2 : ").split())))
        if len(m1)!= n*m or len(m2) != m*r:
            print("Invlid Input Size.")
        else :
            m1=m1.reshape((n,m))
            m2=m2.reshape((m,r))
            m3=m1@m2
            print(m3)
    def transpose(self):
        n = int(input("Enter rows: "))
        m = int(input("Enter columns: "))
        data=list(map(int,input("Enter Elements of the matrix: ").split()))
        if len(data) != n*m :
            print("Invalid input size.")
        else :
            matrix=np.array(data).reshape(n,m)
            transpose=matrix.T
            print(transpose)
    def scalar_multiplication(self):
        n = int(input("Enter rows: "))
        m = int(input("Enter columns: "))
        k = int(input("Enter scalar number: "))
        data=list(map(int,input("Enter elements of The Matrix: ").split()))
        if len(data) != n*m :
            print("Invalid Input.")
        else :
            m1=np.array(data).reshape((n,m))*k
            print(m1)
    def det(self):
        n=int(input("Enter size of the matrix: "))
        data=np.array(list(map(int,input("Enter Elements of the matrix: ").split())))
        if len(data)!=n*n:
            print("Invalid Input.")
        else :
            m1=data.reshape((n,n))
            result=np.linalg.det(m1)
            if np.isclose(result, int(round(result))):
                result = int(round(result))
            print(result)
    def inverse(self):
        n=int(input("Enter size of the matrix: "))
        data=np.array(list(map(int,input("Enter Elements of the matrix: ").split())))
        if len(data)!=n*n or np.linalg.det(data.reshape((n,n)))== 0 :
            print("Invalid Input.")
        else :
            m1=data.reshape((n,n))
            result=np.linalg.inv(m1)
            print(result)
    def rank(self):
        n=int(input("Enter rows: "))
        m=int(input("Enter columns: "))
        data=np.array(list(map(int,input("Enter Elements of the matrix: ").split())))
        if len(data)!=n*m:
            print("Invalid Input.")
        else :
            m1=data.reshape((n,m))
            result=np.linalg.matrix_rank(m1)
            print(result)
    def trace(self):
        n=int(input("Enter size: "))
        data=np.array(list(map(int,input("Enter Elements of the matrix: ").split())))
        if len(data)!=n*n:
            print("Invalid Input.")
        else :
            m1=data.reshape((n,n))
            result=np.trace(m1)
            print(result)

def main():
    cal=matrix_arithmetic()
    __choice="y"
    while __choice in ("y","Y") :
        print("Matrix Operations Toolkit")
        print("")
        print("-------------------- Matrix Operations Toolkit --------------------")
        print("")
        print("""1.Matrix Addition
2.Matrix Subtraction
3.Scalar Multiplication of Matrix
4.Matrix Multiplication
5.Transpose of Matrix
6.Determinant of Matrix
7.Trace of Matrix
8.Rank of Matrix
9.Inverse  of Matrix
10.Exit""") 
        choice = int(input("Enter Your Choice(1/2/3/4/5/6/7/8/9/10): "))
        if choice == 1:
            cal.addition()
        elif choice == 2:
            cal.subtraction()
        elif choice == 3:
            cal.scalar_multiplication()
        elif choice == 4:
            cal.multiply()
        elif choice == 5:
            cal.transpose()
        elif choice == 6:
            cal.det()
        elif choice == 7:
            cal.trace()
        elif choice == 8:
            cal.rank()
        elif choice == 9:
            cal.inverse()
        elif choice == 10:
            print("Successfully out of the system.")
            return 
        else :
            print("Invalid Input.")
        __choice=input("do you want to do more operation(y/n): ")
    else :
        print("Successfully out of the system.")

if __name__ == "__main__":
    main()