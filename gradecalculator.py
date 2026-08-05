studname=input("enter student name:")
java=int(input("enter java marks:"))
math=int(input("enter math marks:"))
telugu=int(input("enter telugu marks:"))
social=int(input("enter social marks:"))
python=int(input("enter python marks:"))
total=java+math+telugu+social+python
percantage=total/5
print("total marks:",total)
print("percantage:",percantage)
if percantage>=90:
    print("your grade is:A+")
if percantage>=75 and percantage<90:
    print("your grade is:A")
    if percantage>=60 and percantage<75:
        print("your grade is:B")
        if percantage>=35 and percantage<60:
            print("your grade is:C")
            if percantage<35:
                print("your garde is:fail")


