# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# n=int(input("enter any number"))
# if n<=0:
#     print("not possible")

# else:
#     count=0
#     for i in(range(1,n+1)):
#         count=count+i
#     print(count)

def count_numofdigits(n):
    l=abs(n)
    return len(str(n))

n=-1234
digit_count= count_numofdigits(n)
print(f"num of digits is {n}:{digit_count}")


