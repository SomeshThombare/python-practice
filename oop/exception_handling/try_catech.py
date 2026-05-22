print('Start')

try:
    # a = int('abc') #type error
    # print(a) 

    # arr = [1,2,3]
    # print(arr[10]) #indexError

    d = {1: 10, 2:20}
    print(d[55]) #key error


except(ValueError , TypeError):
    print('ValueErrro, TypeError')

except ZeroDivisionError as e:
    print('ZeroDivision Error Handles')

except IndexError as e:
    print('IndexError Handled')

except Exception as e:
    print(f'Excption handled , -->  ErrorName: {type(e).__name__}, ErrorMessage : {e}')

print('STOP')