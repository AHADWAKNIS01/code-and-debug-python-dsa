#take age and check wher leigible for vote and check senior citizen

age=int(input("enter your age"))

if age>=18 and age>=60:
    print("your are eligible for the vote and your senior citizen")

elif age>=18 and age<=60:
    print("your are eligible forthe vote but your are not an senioor citizen")

else:
    print("your not eligible for the vote and yor are not senior citizen")
