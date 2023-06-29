roll=int(input("enter your rollno"))
name=input("enter your name ")
ds={
    "roll":roll,
    "name":name
}
print(ds)
L = [roll,name]
print(L)
S={roll,name}
print(S)
t=(roll,name)
print(t)
del ds
del L
del  S
del t
print(ds)
print(L)
print(S)
print(t)