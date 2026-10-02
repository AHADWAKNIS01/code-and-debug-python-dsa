#capturing the excetion

try:
    num1=int(input("enter the number"))
    num2=int(input("enter the number"))
    print(f"nums1/num2={num1/num2}")
except Exception as e:
    print(f"Error message ={e}")