# roll=int(input("enter your rollno"))
# name=input("enter your name ")
# ds={
#     "roll":roll,
#     "name":name
# }
# print(ds)
# L = [roll,name]
# print(L)
# S={roll,name}
# print(S)
# t=(roll,name)
# print(t)
# del ds
# del L
# del  S
# del t
# print(ds)
# print(L)
# print(S)
# print(t)
def ds(roll_no,name):
    p1 = [roll_no,name]#list
    p2 = (roll_no,name)#tuple
    p3 = {roll_no,name}#set
    p4 = {"roll no":roll_no,"name":name}#dictionary

    print(p1)
    print(p2)
    print(p3)
    print(p4)

    roll = int(input("Enter Roll no: "))
    name = input("Enter name: ")

    p1[0] = roll
    p1[1] = name
    p2 = (roll,name)
    p3 = {roll,name}
    p4["roll no"]= roll
    p4["name"]=name

    print("list:",p1)
    print("tuple:",p2)
    print("set:",p3)
    print("dictionary:",p4)

    del p1
    del p2
    del p3
    del p4

roll = int(input("enter roll no.: "))
name = input("Enter name: ")
ds(roll,name)