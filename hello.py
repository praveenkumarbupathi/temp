#edit it with python 
import os
try:
    os.system("cls");
except:
    os.system("clear");

print("hello world \n-----------------------------------------------------------------\n   1)add \n   2)subtraction \n   3)multiplication \n   4)division \n   5)exit")


while(n!=5):
    
    if(n==1):
        l=list(map(int,input("enter numbers:").split()))
        s=0
        for i in l:
            s+=i
        print("sum is ",s )
        input()
    
    elif(n==2):
        print("subtraction is:- ",input()-input())
    elif(n==3):
        l=list(map(int,input("enter numbers:").split()))
        s=0
        for i in l:
            s*=i
        print("multiplication is:- ",s)
        input()
    elif(n==5):
        exit()
    else:
            print(input("enter 2 values:")/input())