a=int(input())
for i in range(2,a):
    if a%i==0:
        print("Not a prime number")
        exit()
print("Prime Number")
