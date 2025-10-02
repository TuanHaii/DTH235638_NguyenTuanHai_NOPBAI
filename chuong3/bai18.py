n = 5
# ve hinh chu nhat
# for i in range(0, n):
#     for j in range(0, n):
#         if(i == 0 or i == n-1 or j == 0  or j == n-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#hinh tam giac
# for i in range(n + 1):
#         print("  " * (n-i), end="")  # In khoảng trắng để cạnh dài bên phải
#         for j in range(i):
#                 print("* ", end="")
#         print()
for i in range(n):
    for j in range(i):
            print("*", end=" ")
    print()