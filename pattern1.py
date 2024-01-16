# for j in range(1, 4):
#     print("*")

# n = int(input("enter range for printing vertical(columnwise) pattern="))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print("*")
#     print()

# n = int(input("enter range for printing horizontal(rowwise) pattern="))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print("*", end="")
#     print(end=" ")

# n = int(input("enter range for printing matrix="))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print("*", end="")
#     print()

# row = int(input("enter range for row in matrix="))
# column = int(input("enter range for column in matrix="))
# for i in range(1, row + 1):
#     for j in range(1, column + 1):
#         print("*", end="")
#     print()

# row = int(input("enter range for row for printing incremental left triangle="))
# for i in range(1, row + 1):
#     for j in range(i):
#         print("*", end="")
#     print()


# row = int(input("enter range for row for printing decremental left triangle="))
# for i in range(1, row):
#     for j in range(row - i):
#         print("*", end="")
#     print()

row = int(input("enter range for row for printing incremental right triangle="))
for i in range(row + 1):
    for j in range(i, row):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()
