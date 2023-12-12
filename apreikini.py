a=int(input('a='))
b=int(input('b='))
darb=input('+,-, *, /:')
if darb == '+':
    c=a+b
elif darb == '-':
   c=a-b
elif darb == '*':
   c=a*b
elif darb == '/':
   c=a/b
else:
   c= 'Kļūda'
print('Atbilde ir:', c)

for i in range (0.5,-5,5):
 print(i, end=',')