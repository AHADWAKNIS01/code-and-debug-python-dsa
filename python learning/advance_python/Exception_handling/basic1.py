try:
    num1=int(input("enter the number"))
    num2=int(input("enter the number"))
    print(f"nums1/num2={num1/num2}")

except ZeroDivisionError:
    print("can't divide by the zero")

except ValueError:
    print("pleasae enter proper integers")

except:
    print("some error happend")
        
