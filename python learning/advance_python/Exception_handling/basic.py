#expeption handling and common built in exptions are add in notes etc
#and give all the error which name and message
try:
    age=int(input("enter the age"))
    if age>=18:
        print("adults")

    else:
        print('not adult')

except:
    print("some error occured")

