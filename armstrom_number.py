n=123
num=n
length=len(str(num))
result=0

while num >0:
  last_digit=num % 10
  result= result + last_digit**length
  num=num // 10

if n==result:
  print("it an amstrong number")

else:
  print("it  is not an amstrong number")


