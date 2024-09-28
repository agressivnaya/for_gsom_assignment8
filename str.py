list = [ 'fall', 9, True, 'summer', 6, False, 'spring', 3, False, 'winter', 11, False, 3.14]

counter = 0
for i in list:
    if type(i) == str:
        counter = counter +1
print ('There are', counter, 'strings in the list')