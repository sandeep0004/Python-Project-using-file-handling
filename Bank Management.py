print("_"*50)
print("\n********** Bank Management System **********")
print("_"*50)

detail=['Account number','Name','Address','Phone','ID','Account type','Amount']
detail2=[]
def new_acc():
    new_acc=int(input("Enter the new account number: "))
    detail2.append(new_acc)

def new_name():
    new_name=str(input("Enter new name: "))
    detail2.append(new_name)
    
def new_address():
    new_address=str(input("Enter the city: "))
    detail2.append(new_address)

def new_phone():
    new_phone=int(input("Enter new number: "))
    detail2.append(new_phone)
    
def id_proof():
    d=str(input("Enter govt: "))
    detail2.append(d)
    
def acc_type():
    acc_type=str(input("Enter account type: "))
    detail2.append(acc_type)

def b_amt():
    b_amt=int(input("Enter the amount for 1st deposit: "))
    detail2.append(b_amt)

def view():
    details=dict(zip(detail,detail2))
    print(details)
    
while True:
    print("_"*20)
    print("\nOptions: ")
    print("\n1. New customer")
    print("2. Existing customer")
    print("3. Exit")
    c=int(input("\nEnter your choice: "))
    if(c==1):
        new_acc()
        new_name()
        new_address()
        new_phone()
        id_proof()
        acc_type()
        b_amt()
        print("Account created successfully")
        view()
    elif(c==2):
        x=int(input("Enter account number: "))
        if(x in detail2):
            print('_'*20)
            print("\nSelect one option: ")
            print("1. Check balance")
            print("2. Withdraw")
            print("3. Deposit")
            print('_'*20)
            x=int(input("Enter your choice: "))
            if(x==1):
                print("Balance: ",detail2[6])
            elif(x==2):
                y=int(input("Enter the amount to withdraw: "))
                detail2[6]=detail2[6]-y
                print("Updated balance: ",detail2[6])
            elif(x==3):
                z=int(input("Enter the amount to deposit: "))
                detail2[6]=detail2[6]+z
                print("Updated balance: ",detail2[6])
        elif(x not in detail2):
            print("Account not found")
    elif(c==3):
        exit()
    else:
        print("Wrong input")
        break




          
          
    
    
    
    
    



