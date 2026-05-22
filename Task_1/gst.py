#accept the total bill of hotal and calculate the  cgst(18%) and sgst(18%)on total bill
total_bill = float(input('Eenter the Total amount :'))

sgst =  total_bill * 0.18

cgst = total_bill * 0.18

total_bill_with_gst = total_bill + sgst + cgst

print(f'the CGST on total bill is  {cgst}')
print(f'the SGST on total bill is {sgst}')

print(f'Total bill incldign GST {total_bill_with_gst}')
