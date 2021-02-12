import math

even=[]
odd=[]
prime=[]



def checkprime(inp):
    i=2
    done=True
    for i in range(2,int(math.sqrt(inp))+1):
        if inp%i==0:
            done=False
            break
    if done:
        return True
    return False


while(True):
    inp=input("Enter the number")
    if inp=='q' or inp=='Q':
        break
    inp=int(inp)
    if checkprime(inp):
        prime.append(inp)
    elif inp&1:
        odd.append(inp)
    else:
        even.append(inp)

print("Output:")
print("Even:{}".format(even))
print("Odd:{}".format(odd))
print("Prime:{}".format(prime))


"""
Output:
Enter the number1
Enter the number2
Enter the number3
Enter the number4
Enter the number5
Enter the number6
Enter the number7
Enter the number8
Enter the number9
Enter the number10
Enter the numberq

Output:
Even:[4, 6, 8, 10]
Odd:[9]
Prime:[1, 2, 3, 5, 7]


"""