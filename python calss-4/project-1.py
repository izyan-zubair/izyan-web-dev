
num = 23
print("table of 23")
for i in range(1, 11):
    mul = num*i
    print("23 x %d = %d" % (i, mul))

n = int(input("Enter a number of rows: "))
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end=" ")
    print("\n")

num = 1
sum = 0
while(num <= 10):
    sum = sum + num
    num = num+1
print("The sum of first 10 natural numbers :", sum)

num = int(input("Enter number to be checked :   "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prine number")
else:
    print(num, "is a prime number")