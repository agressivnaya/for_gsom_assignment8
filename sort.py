a = int (input ('Enter the first number:'))
b = int (input ('Enter the second number:'))
c = int (input ('Enter the third number:'))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
    
print ('Sorted numbers:', a, b, c)