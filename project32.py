tuplex=(-5,3,4,2,1)
print(tuplex)
even=0
odd=0
for c in tuplex:
    if c%2==0:
        even+=1
    else:
        odd+=1
print('even',even)
print('odd',odd)
