try:
    num1=int(input("enter the number"))
    num2=int(input("enter the number"))
    print(f"nums1/num2={num1/num2}")


#both error occurs
except (ZeroDivisionError,ValueError):
    print("can't divide by the zero")
