A=[[1,1,0],[1,0,1],[0,0,0]]

for i in range(len(A)):
    A[i]=list(reversed(A[i]))
    # print(A[i])
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]==0:
            A[i][j]=1
        elif A[i][j]==1:
            A[i][j]=0

B=[[1,1,0],[1,0,1],[0,0,0]]
for j in range(len(B)):
    B[j][:]=B[j][::-1]
print(B)



# A=[1,1,0]
# A=A[::-1]
# print(A)
