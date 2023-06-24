def view():
    o=open("Student.txt","r")
    n=o.read()
    print(n)
    o.close()

def add():
    o=open("Student.txt","a")
    add=input("Enter the name you want to add: ")
    add=add+'\n'
    o.write(add)
    print("Name added successfully")
    o.close()

def delete():
    o=open("Student.txt","a+")
    n=input("Enter the name you want to delete: ")
    n=n+'\n'
    o.seek(0)
    rn=o.readlines()
    if n in rn:
        rn.remove(n)
        print("Name deleted successfully")
        s=''
        s=''.join([str(i) for i in rn])
        f=open("Student.txt","w")
        f.write(s)
        f.close()
    else:
        print("Name not found")
    o.close()

def search():
    o=open("Student.txt","r")
    n=o.read()
    s=input("Enter the name you want to search: ")
    if(s in n):
        print("Name found")
    else:
        print("Name not found")
    o.close()
        
    
    
