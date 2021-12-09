


print("Enter the Number: ")
numuser= int(input())

p = 0
for x in range(2, numuser):
    if(numuser%x)==0:
        p = 1
        break

if p==0:
    print(" Prime Number")
else:
    print("\n not  a Prime Number")





   


