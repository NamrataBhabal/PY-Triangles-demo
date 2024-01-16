# print("Left Incremental Triangle")
# row=int(input("enter rows="))
# for i in range(1,row+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# print("Left decremental Triangle")
# row=int(input("enter rows="))
# for i in range(1,row+1):
#     for j in range((row-i)+1):
#         print("*",end="")
#     print()

# print("Left decremental Triangle")
# row=int(input("enter rows="))
# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# print("Right decremental Triangle")
# row=int(input("enter rows="))
# for i in range(row):
#     for j in range(i):
#         print(' ',end="")
#     for j in range(i,row):
#         print("*",end="")
#     print()

# print("Right incremental Triangle")
# row=int(input("enter rows="))
# for i in range(row):
#     for j in range(i,row-1):
#         print(' ',end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()


print("Hill incremental Triangle")
row=int(input("enter rows="))
for i in range(row):
    for j in range(i,row-1):
        print(' ',end="")
    for j in range(i+1):
        print(" *",end="")
    print()



print("Hill decremental Triangle")
row=int(input("enter rows="))
for i in range(row,0,-1):
    for j in range(row,i,-1):
        print(' ',end="")
    for j in range(i):
        print(" *",end="")
    print()


print("Hill incremental Triangle")
row=int(input("enter rows="))
for i in range(row):
    for j in range(i,row+1):
        print(' ',end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()