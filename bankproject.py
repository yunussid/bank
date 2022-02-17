import pickle
from datetime import datetime
def star() :
      print("*"*100)

def clr() :
      for i in range(22) :
            print("  "*50)
            
def Open_acc() :
    ch='y'
    with open("C:\\sskp\\banking\\master_file.dat","ab") as fobj :
        while ch=='y'or ch=='Y' :
            acno=input("Enter account Number : ")
            cname=input("Enter Customer name : ")
            fname=input("Enter Father's  name  : ")
            add=input("Enter Customer Address : ")
            bal=float(input("Enter Opening balance : "))
            dt=datetime.today()
            rec=[acno,cname,fname,add,dt,bal]
            print(rec)
            pickle.dump(rec,fobj)
            ch=input("Do you want to store more records  (Y/N) ? : ")

def view_rec() :
         with open("C:\\sskp\\banking\\master_file.dat","rb") as fobj :
           try:
                 while  fobj:
                     rec=pickle.load(fobj)
                     print("Account Number       : ",rec[0])
                     print("Customer name        : ",rec[1])
                     print("Father's  name          : ",rec[2])
                     print("Customer Address   : ",rec[3])
                     print("Date of opening account :",rec[4])
                     print("Acount        balance  :  ",rec[5])
                     print()
                     c=input(" Press any key to continue ")
           except EOFError :
                    c=input(" Press any key to continue ")

def withdrawl() :
       pos=found=0
       with open("C:\\sskp\\banking\\master_file.dat","rb+") as fobj :
             tacno=input("Enter account number :")
             try:
                   while fobj:
                         rec=pickle.load(fobj)   # rec =[1002, A,F1,Kpt,6000]
                         
                         if tacno== rec[0] :
                               
                               print("\n Account No              : ",rec[0])
                               print(" Name of customer   : ",rec[1])
                               print(" Balance in account  : ",rec[5])
                               c=input(" Press any key to continue ")
                               wamt=float(input("Enter amout to be withdrawn : "))   #  500
                               if wamt <rec[5] :
                                   rec[5]=rec[5]-wamt     #rec[4] =5500
                                   with open("C:\\sskp\\banking\\Trans_file.dat","ab") as fobj1 :
                                       dt=datetime.today()
                                       pickle.dump([ rec[0],dt,wamt,"W",rec[5] ],fobj1)
                                       print("Transaction is successfull ")
                                       print(" Your current balance is : ",rec[5])
                                       fobj1.close()
                                       fobj.seek(pos)
                                       pickle.dump(rec,fobj)
                                       found =1
                                       break
                               else :
                                      print(" Tansaction  declined as you have less balnce ")
                                      break
                         else :
                               pos =fobj.tell()
             except      EOFError :
                          if found==0 :
                                print(" The account ",tacno," Does not exsits ")
             c=input(" Press any key to continue ")
             fobj.close()

def deposit() :
       pos=found=0
       with open("C:\\sskp\\banking\\master_file.dat","rb+") as fobj :
             tacno=input("Enter account number :")
             try:
                   while fobj:
                         rec=pickle.load(fobj)   # rec =[1002, A,F1,Kpt,6000]
                         
                         if tacno== rec[0] :
                               
                               print("\n Account No              : ",rec[0])
                               print(" Name of customer   : ",rec[1])
                               print(" Balance in account  : ",rec[5])
                               c=input(" Press any key to continue ")
                               wamt=float(input("Enter amout to be deposited : "))   #  500
                               rec[5]=rec[5]+wamt     #rec[4] =5500
                               with open("C:\\sskp\\banking\\Trans_file.dat","ab") as fobj1 :
                                       dt=datetime.today()
                                       pickle.dump([ rec[0],dt,wamt,"D",rec[5] ],fobj1)
                                       print("Transaction is successfull ")
                                       print(" Your current balance is : ",rec[5])
                                       fobj1.close()
                                       fobj.seek(pos)
                                       pickle.dump(rec,fobj)
                                       found =1
                                       break
                         else :
                               pos =fobj.tell()
             except      EOFError :
                          if found==0 :
                                print(" The account ",tacno," Does not exsits ")
             c=input(" Press any key to continue ")
             fobj.close()

def get_name(tacno) :
       with open("C:\\sskp\\banking\\master_file.dat","rb") as fobj :
           try:
                 while  fobj:
                     rec=pickle.load(fobj)
                     if rec[0]==tacno :
                        return rec
                        break
           except EOFError :
                    c=input(" Press any key to continue ")
                    print(" Account bdoes not exsists ")
                    fobj.close()
        
def pri_pass() :
      tacno=input(" Enter account number whose pass book U want to print ")
      trec=get_name(tacno) 
      with open("C:\\sskp\\banking\\Trans_file.dat","rb") as fobj1 :
            fobj1.seek(0)
            try :
                 
                  print("                                          STATE BANK OF INDIA          ")
                  star()
                  print("                                             PASS BOOK ENTRY          ")
                  star()
                  print("Account number : ",tacno," \t    Name of Customer : ",trec[1] )
                  star()
                  print(" Date of transaction                    Tran. Amount          W / D              Balance ")
                  star()
                  while fobj1 :
                      rec=pickle.load(fobj1) # [1002    8/6/2020   660  W     5000]  
                      if tacno == rec[0] :
                           print(rec[1], "               ",rec[2],"                    ",rec[3],"        ", rec[4])   
                
            except EOFError :
                     fobj1.close()
      star()
      print( " Current balance in customer account is ------------ >  ",rec[4])
      star()
      c=input(" Press any key to continue ")  

def pri_ledg() :
      print("                                          STATE BANK OF INDIA          ")
      star()
      print("                                             LEDGER STATUS          ")
      star()
      print("Account number :                         Name of Customer                  Balance " )
      star()
      tamt=0.0
      with open("C:\\sskp\\banking\\master_file.dat","rb") as fobj :
           try:
                 while  fobj:
                     rec=pickle.load(fobj)
                     tamt=tamt+rec[5]
                     print("  ",rec[0],"                                            ",rec[1],"                                      ",rec[5])
                     
           except EOFError :
                    fobj.close()
      star()
      print( "                Total Deposit in Bank is  ------------ >  ",tamt)
      star()
      c=input(" Press any key to continue ")
     
# ******************** MAIN PROGRAM *************************
ch=0
while ch != 7:
   clr()  
   star()
   print("                     STATE BANK OF INDIA WELCOMES YOU        ")
   star()
   print("                                  1. Open account        ")
   print("                                  2. View Record        ")
   print("                                  3. Withdrawl     ")
   print("                                  4. Deposit     ")
   print("                                  5. Print pass book    ")
   print("                                  6. Print Ledger   ")
   print("                                  7. For Exit program        ")
   ch=int(input("\n                 Enter your choice (1-7) ? : "))
   if ch==1 :
         clr()
         Open_acc()
   if ch==2 :
          clr()
          view_rec()
   if ch==3 :
          clr()
          withdrawl()
   if ch==4 :
          clr()
          deposit()
   if ch==5 :
          clr()
          pri_pass()    
   if ch==6 :
          clr()
          pri_ledg()
   if ch==7 :
         print(" Thanks for using this program . ")
         c=input(" Press any key to continue ")
