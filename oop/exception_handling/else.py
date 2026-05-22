print('START')
try:
   print('try block')
#    print(10/0) # when comment thsi statement then exeucute the else block other wise execute except block

except Exception as e:
    print('Except block')
else:
    print('Else block')

print('STOP')