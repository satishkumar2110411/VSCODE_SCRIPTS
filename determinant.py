L = []
for i in range(1,4):
    for j in range(1,4):
        element = float(input(f'Enter element a{i}{j}: '))
        L+=[element,]

determinant = L[0]*(L[4]*L[8]-L[5]*L[7]) - L[1]*(L[3]*L[8]-L[5]*L[6]) + L[2]*(L[3]*L[7]-L[4]*L[6])

print(f'matrix is \n {L[0]} {L[1]} {L[2]} \n {L[3]} {L[4]} {L[5]} \n {L[6]} {L[7]} {L[8]}')
print(f'determinant = {determinant}')