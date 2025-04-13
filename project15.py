try:
    num1, num2=eval(input('enter two numbers, separate by a comma:'))
    result=num1/num2
    print('result is',result)
except ZeroDivisionError:
    print('division by zero is error!!')
except SyntaxError:
    print('comma is missing. enter number separate by comma like this 1,2')
except:
    print('wrong input')
else:
    print('no exceptions')
finally:
    print('this will execute no matter what')