D={}
while(True):
    Fullname=input("Give Full name of your Friend : ")
    if Fullname=='q' or Fullname=='Q':
        break
    Nick=input("Give Nick name of this Friend : ")
    if Nick=='q' or Nick=='Q':
        break
    D[Nick]=Fullname
    print("\nEnter q/Q any time to quit\n")

while(True):
    Nick=input("Enter nickname of your friend to get his full name : ")
    if Nick=='q' or Nick=='Q':
        break
    if Nick in D:
        print("{}'s fullname is {}".format(Nick,D[Nick]))
    else:
        print("Sorry,we dont have anybody of name {} in our database".format(Nick))

    print("\nEnter q/Q any time to quit\n")

    

"""
Output:
Give Full name of your Friend : Sandeep Padhi
Give Nick name of this Friend : sandy

Enter q/Q any time to quit

Give Full name of your Friend : Prashant Mishra
Give Nick name of this Friend : Abhay

Enter q/Q any time to quit

Give Full name of your Friend : Saurabh Bhagat
Give Nick name of this Friend : prosoft

Enter q/Q any time to quit

Give Full name of your Friend : Ajay Singh
Give Nick name of this Friend : Tanker

Enter q/Q any time to quit

Give Full name of your Friend : q
Enter nickname of your friend to get his full name : Tanker
Tanker's fullname is Ajay Singh

Enter q/Q any time to quit

Enter nickname of your friend to get his full name : Abhay
Abhay's fullname is Prashant Mishra

Enter q/Q any time to quit

Enter nickname of your friend to get his full name : Sandy
Sorry,we dont have anybody of name Sandy in our database

Enter q/Q any time to quit

Enter nickname of your friend to get his full name : jonny
Sorry,we dont have anybody of name jonny in our database

Enter q/Q any time to quit

Enter nickname of your friend to get his full name : q


"""