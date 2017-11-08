########################################################################################################################################
#     File name : BankClass                                                                                                             #
#     Authors : Nyonyintono John Peter, Mutungi Lynette Kicoonco, Mpaata Charles Norman, Mudondo Chermaine Lipoto, Mulindwa Benedict    #
#                                                                                                                                       #
#########################################################################################################################################



import pickle
import os
"""

BANK CLASS


"""

class _bank(object):
    def __init__(self, bankid=int, bankname=str, banklocation=str, numberofcustomers=10, numberoftellers=3 ):
         self.bankid = bankid
         self.bankname = bankname
         self.banklocation = banklocation
         self.numberofcustomers = numberofcustomers
         self.numberoftellers = numberoftellers

"""

CUSTOMER CLASS


"""
class _customer(_bank):
    def __init__(self, accounttype, customerId, address, accountId):
        super().__init__()
        self.customerId = ""
        self.accountId = 0
        self.accounttype = ""

    def general_inquiry(self):
          print("Hello %s, you are welcome to %s",(self.customerId, self.bankid, self.banklocation))
    def balance(self,amount):
        pass
    def dep(self,amount):
        pass
    def draw(self,amount):
        pass
    def open_account(self):
        pass
    def delete_account(n):
        pass
    def apply_for_loan(self,amount):
        pass
    def request_card(self):
        print("please enter accountId ")
        accountId = int(input())
        if accountId == accountId  :
             print("please enter CustomerId ")
             CustomerId = int(input())
             print("please wait a while as we process your credit card")
        else:
            print("Account not known")


"""

TELLER CLASS

"""
class _teller(_customer,_bank):
    def __init__(self, tellerid=int, tellername=str):

        self.tellerid = tellerid
        self.tellername = tellername

    def balance(self,amount):
        pass
    def dep(self,amount):
        pass
    def draw(self,amount):
        pass
    def open_account(self):
        pass
    def close_account(n):
        pass
    def apply_for_loan(self):
        pass
    def issue_card(self):
        pass

"""
ACCOUNT CLASS
"""

class account(_teller, _customer, _bank):
    def __init__(self, accountId, customerId, deposit, accounttype):
        self.accountId=0
        self.customerId=""
        self.deposit=0
        self.accounttype=""

    def create_account(self):  #function to get data from user
        customerId=input("\n\nEnter the customerId of the account holder: ")
        self.customerId=customerId.capitalize()
        accounttype= input("\nEnter accounttype of the account (C/S): ")
        self.accounttype=accounttype.upper()
        self.deposit=input("\nEnter initial amount\n(>=500 for Saving and >=1000 for Current): ")

    def show_account(self):    #function to show data on screen
        print("\nAccount Id. :", self.accountId)
        print("\nAccount holder customerId: ", self.customerId)
        print("\nAccounttype of account", self.accounttype)
        print("\nBalance amount: ", self.deposit)

    def modify(self):          #function to get new data from user
        print("\nAccount Id. : ", self.accountId)
        self.customerId= input("\n\nEnter the customerId of account holder: ")
        accounttype= input("\n\nEnter accounttype of account (C/S): ")
        self.accounttype=accounttype.upper()
        self.deposit=input("\nEnter the amount: ")

    def dep(self,amount):           #function to accept amount and add to balance
        self.deposit+=amount

    def draw(self,amount):          #function to accept amount and subtract from balance amount
        self.deposit-=amount

    def report(self):          #function to show data in tabular format
        print ("%-10s"%self.accountId,"%-20s"%self.customerId,"%-10s"%self.accounttype,"%-6s"%self.deposit)

    def retaccountId(self):         #function to return account number
        return self.accountId

    def retdeposit(self):      #function to return balance amount
        return self.deposit

    def retaccounttype(self):         #function to return accounttype of account
        return self.accounttype


"""
                    FUNCTION TO GENERATE ACCOUNT NUMBER
"""


def gen_accountId():
    try:
        inFile=open("account2.dat","rb")
        outFile=open("text2.dat","wb")
        n=inFile.read()
        n=int(n)
        while True:
            n+=1
            outFile.write(str(n))
            inFile.close()
            outFile.close()
            os.remove("account2.dat")
            os.rename("text2.dat","account2.dat")
            yield n

    except IOError:
        print("I/O error occured")


"""
                    FUNCTION TO WRITE RECORD IN BINARY FILE
"""

def write_account():
    try:
        ac=account()
        outFile=open("account.dat","ab")
        ch=gen_accountId()
        ac.accountId=ch.next()
        ac.create_account()
        pickle.dump(ac,outFile)
        outFile.close()
        print ("\n\n Account Created Successfully")
        print ("\n\n YOUR ACCOUNT NUMBER IS: ",ac.retaccountId())
    except:
        pass


"""
                FUNCTION TO DISPLAY ACCOUNT DETAILS GIVEN BY USER
"""

def display_sp(n):
    flag=0
    try:
        inFile=open("account.dat","rb")
        print( "\nBALANCE DETAILS\n")
        while True:
            ac=pickle.load(inFile)

            if ac.retaccountId()==n:
                ac.show_account()
                flag=1

    except EOFError:
        inFile.close
        if flag==0:
            print( "\n\nAccount number not exist")

    except IOError:
        print ("File could not be open !! Press any Key...")


"""
                        FUNCTION TO MODIFY RECORD OF FILE
"""

def modify_account(n):
    found=0
    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retaccountId()==n:
                print (30*"-")
                ac.show_account()
                print (30*"-")
                print ("\n\nEnter The New Details of Account")
                ac.modify()
                pickle.dump(ac,outFile)
                print ("\n\n\tRecord Updated")
                found=1
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found ")

    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")


"""
                    FUNCTION TO DELETE RECORD OF FILE
"""

def delete_account(n):
    found=0

    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retaccountId()==n:
                found=1
                print ("\n\n\tRecord Deleted ..")
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found")

    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")


"""
                    FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
"""

def display_all():
    print ("\n\n\tACCOUNT HOLDER LIST\n\n")
    print( 60*"=")
    print ("%-10s"%"A/C No.","%-20s"%"CustomerId","%-10s"%"Accounttype","%-6s"%"Balance")
    print (60*"=","\n")
    try:
        inFile=open("account.dat","rb")
        while True:
            ac=pickle.load(inFile)
            ac.report()

    except EOFError:
        inFile.close()

    except IOError:
       print ("File could not be open !! Press any Key...")


"""
            FUNCTION TO DEPOSIT/WITHDRAW AMOUNT FOR GIVEN ACCOUNT
"""

def deposit_withdraw(n,option):
    found=0

    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retaccountId()==n:
                ac.show_account()
                if option==1:
                    print ("\n\n\tTO DEPOSIT AMOUNT")
                    amt=input("Enter the amount to be deposited: ")
                    ac.dep(amt)
                elif option==2:
                    print ("\n\n\tTO WITHDRAW AMOUNT")
                    amt=input("Enter amount to be withdraw: ")
                    bal=ac.retdeposit()-amt
                    if((bal<500 and ac.retaccounttype()=="S")or(bal<1000 and ac.retaccounttype()=="C")):
                        print ("Insufficient balance")
                    else:
                        ac.draw(amt)
                pickle.dump(ac,outFile)
                found=1
                print ("\n\n\tRecord Updated")
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found")

    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")


"""

LOAN CLASS

"""
class _loanCALCULATOR(_teller,_customer,_bank):

      Loan_amount = None # assigning none values
      Month_Payment = None # assigning none values
      Interest_rate = None #assigning none values
      Payment_period = None #assigning none values

      def apply_for_loan(self):#get the  value of loan amount
          self.Loan_amount = input("Enter The Loan amount(in shillings) :")

          pass

      def get_interest_rate(self):# get the value of interest rate
          self.Interest_rate = 25
          pass

      def get_payment_period(self):# get the payment period in months
          self.Payment_period = 24
          pass


      def calc_interest_rate(self):# To calculate the  interest rate"
          self.get_interest_rate()


          self.Interest_rate = (self.Interest_rate /100.0)




      def calc_loan(selfs):# To calculate the loan"

          try:

            selfs.apply_for_loan() #input loan amount
            selfs.get_payment_period() #input payment period
            selfs.calc_interest_rate() #input interest rate and calculate the interest rate

          except NameError:
              print("You have not entered Loan amount (OR) payment period correctly,Please enter and try again. ")

          try:
            selfs.Month_Payment = (selfs.Loan_amount*pow((selfs.Interest_rate/12)+1,
                                  (selfs.Payment_period))*selfs.Interest_rate/12)/(pow(selfs.Interest_rate/12+1,
                                  (selfs.Payment_period)) - 1)

          except ZeroDivisionError:
              print("ERROR!! ZERO DIVISION ERROR")
          else:
              print("Monthly Payment is : %r" % selfs.Month_Payment)



"""
                        INTRODUCTORY FUNCTION
"""

def intro():
    print ("\n\n\tBANKING")
    print ("\n\t SYSTEM")



"""
                        THE MAIN FUNCTION OF PROGRAM
"""

intro()

while True:
    print (3*"\n",60*"=")
    print( """MAIN MENU

    1. New Account
    2. Deposit Amount
    3. Withdraw Amount
    4. Balance Enquiry
    5. All Account Holder List
    6. Close An Account
    7. Modify An Account
    8. Apply For Loan
    9. Exit
    """)

    try:
        ch=input("Enter Your Choice(1~9): ")
        if (ch==1):
            write_account()

        if ch==2:
            num=int(input("\n\nEnter Account Number: "))
            deposit_withdraw(num,1)

        if ch==3:
            num=input("\n\nEnter Account Number: ")
            deposit_withdraw(num,2)

        if ch==4:
            num=input("\n\nEnter Account Number: ")
            display_sp(num)

        if ch==5:
            display_all()

        if ch==6:
            num=input("\n\nEnter Account Number: ")
            delete_account(num)

        if ch==7:
            num=input("\n\nEnter Account Number: ")
            modify_account(num)

        if ch==8:
            num=input("\n\nEnter Account Number:")
            _loanCALCULATOR.apply_for_loan()

        if ch==9:
            break


    except NameError:
        print ("Input correct choice...(1-9)")



        input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")





BankA = _bank(1111,'equitybank','wandegeya')
BankB = _bank(1112,'stanbic bank','katanga')

tellerA1 = _teller(11,'BankA_1')
tellerA2 = _teller(12,'BankA_2')
tellerA3 = _teller(13,'BankA_3')

tellerB1 = _teller(21,'BankB_1')
tellerB2 = _teller(22,'BankB_2')
tellerB3 = _teller(23,'BankB_3')
