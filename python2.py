def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print('please select the operator')
print('a.add')
print('b.subtract')
print('c.multiply')
print('d.divide')
choice=input('please enter choice (a/b/c/d):')
num_1=int(input('enter a number'))
num_2=int(input('enter a number'))
if choice=="a":
    print('addision is',add(num_1,num_2))
elif choice=='b':
    print(num_1,"_",num_2,"=",subtract(num_1,num_2))
elif choice=="c":
    print(num_1,"_",num_2,"=",multiply(num_1,num_2))
elif choice=="d":
    print(num_1,"_",num_2,"=",divide(num_1,num_2))
else:
    print('number is invaid')