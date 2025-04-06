x=0
y=0
z=0
def maxi(x,y,z):
    if x>y and x>z:
        print('x is the maximum number')
    elif y>x and y>z:
        print('y is the maximum number')
    else:
        print('z is the maximum number')
maxi(x,y,z)