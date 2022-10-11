#big.py
a=int(input("Enter Value of a:")) # 10 
b=int(input("Enter Value of b:")) # 4
big=a  if(a>b)   else  b   # This "if....else  is called Ternary Operator.
#print("big({},{})={}".format(a,b,big))
print("big({},{})={}".format(a,b,a if(a>b) else b))