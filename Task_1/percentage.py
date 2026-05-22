#accept the five sub marks and print total and percentage
m1 = float(input('Enter First subject marks:'))
m2 = float(input('Enter second subject marks:'))
m3 = float(input('Enter Thirdect marks:'))
m4 = float(input('Enter Fourth subject marks:'))
m5 = float(input('Enter Fifth subject marks:'))

total_marks = m1 + m2 + m3 + m4 + m5

percentage = total_marks / 5

print('Toal marks is ', total_marks)
print(f'Percntage {percentage}')

