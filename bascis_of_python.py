# even number counter
a=int(input("enter a number : "))
count=0
for a in range(1,a):
    if a%2==0:
        count=count+1
print(count)

# multiplication table generator
num=int(input("enter a number:"))
print("Multiplication table:")
for i in range(1,11):
    print(num,"x",i,"=",num*i)

# exam score filter
marks=[]
n=int(input("enter a number:"))
for i in range(n):
    marks.append(int(input("enter marks:")))
print("Marks Above 50:")
for m in marks:
    if m>50:
        print(m)

# electricity bill generator
units=int(input("enter a number of units:"))
if units<=100:
    print("free")
elif units<=200:
    bill=units*3
else:
    bill=units*5
print("the electricity bill is=",bill)

# ATM withdrawal system
balance=int(input("enter a balance amount:"))
withdrawal=int(input("enter a withdrawal amount:"))
if withdrawal<=balance:
    balance=balance-withdrawal
    print("withdrawal is done sucessfully")
    print("the balance amount is :",balance)
else:
    print("sufficient balance is unavailable")

# login authentication
username=input("enter the username:")
password=input("enter the password:")
if username=="merunya":
    if password=="123456789":
        print("login successfully")
    else:
        print("incorrect password")
else:
    print("incorrect username")
    
#password strength checker
password=input("enter the password:")
letter=False
number=False
for i in password:
    if i.isalpha():
        letter=True
    if i.isdigit():
        number=True
if len(password)>=8 and letter and number:
    print("it is a strong password")
else:
    print("it is a weak password")

# temperature monitoring system
temperature=int(input("enter the temperature:"))
if temperature<=15:
    print("Its cold")
elif temperature>=15 and temperature<=30:
    print("Its normal")
else:
    print("Too hot") 

# student result analysis
mark=0
for i in range(1,6):
    n=int(input("enter a marks:"))
    mark=mark + n
average=mark/5
print("total marks:",mark)
print("the average:",average)
if mark<=35:
    print("fail")
else:
    print("pass")

# employee bonus calculation
salary=int(input("enter your salary:"))
if salary>=50000:
    bonus=salary+2000
elif salary>=40000:
    bonus=salary+1000
else:
    bonus=salary+100
final_salary=salary+bonus
print("bonus:",bonus)
print("final_salary:",final_salary)

# online shopping discount
amount=int(input("enter a amount:"))
if amount>=5000:
    discount=amount-200
elif amount>=3000:
    discount=amount-100
else:
    discount=amount-50
discount=amount-discount
final=amount-discount
rint("discount:",discount)
print("final_amount:",final)

# attendance eligibility checker
days=int(input("enter total working days:"))
present=int(input("enter days of prsent:"))
attendance=(present/days)*100
print("attendance percentage:",attendance)
if attendance>=75:
    print("eligibil for exam")
else:
    print("not eligibil for exam")

# restaurant billing system
bill=int(input("enter a bill amount:"))
GST=bill*18/100
final_amount=bill+GST
print("bill=",bill)
print("GST(5%)=",GST)
print("final amount=",final_amount)

# weekly sales report
weekly_sales=0
for i in range(7):
    sales=int(input("enter daily sales:"))
    weekly_sales+=sales
print("total weekly sales:",weekly_sales)

# employee attendance tracker
attendance=[]
n=int(input("enter number of employees:"))
for i in range(n):
    status=input("enter P for present/ A for absent:")
    attendance.append(status)
present=attendance.count("P")
print("present employees=",present)
print("absent employees=",n-present)

# monthly expense calculator
total=0
for i in range(1,13):
    amount=int(input("enter expense for month:"))
    total+=amount
print("total monthly expense=",total)

# student name management
names=[]
n=int(input("enter the number of students:"))
for i in range(n):
    name=input("enter student name:")
    names.append(name)
print("students list:",names)
remove_name=input("enter student name to remove:")
if remove_name in names:
    names.remove(remove_name)
    print("name removed successfully")
    print("final student list:")
    for name in names:
        print(name)
else:
    print("student name is not found")

# product price analysis
price=[]
n=int(input("enter the number of product:"))
for i in range(n):
    p=float(input("enter product price:"))
    price.append(p)
print("highest price=",max(price))
print("lowest price=",min(price))

# employee details
name=[]
department=[]
salary=[]
n=int(input("enter the number of employees:"))
for i in range(n):
    name.append(input("enter employee name:"))
    department.append(input("enter employee department:"))
    salary.append(int(input("enter employee salary:")))
print("employee details")
for i in range(n):
    print("name:",name[i])
    print("department:",department[i])
    print("salary:",salary[i])

# student result lookup
students = {
    "Shinchan": 85,
    "Kazhama": 90,
    "Boo": 78,
    "Mazavu": 95,
    "Naneii": 88
}
name = input("Enter student name: ")
if name in students:
    print("Student Name:", name)
    print("Mark:", students[name])
else:
    print("Student not found.")
