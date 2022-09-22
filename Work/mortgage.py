# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

#new variables to solve exercises 1.8 and 1.9
month = 0
extra_pmt = 1000
extra_pmt_start = 60
extra_pmt_end = 59+4*12

while principal > 0:
    #fixing the last month overpayment
    if payment > principal * (1+rate/12): payment = principal * (1+rate/12)
    
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    #Making extra payments if they're due
    if (month>=extra_pmt_start and month<=extra_pmt_end and principal>0):
        principal -= extra_pmt
        total_paid += extra_pmt
    month+=1
    
    print(f'{month: 3d} {total_paid: 10.2f} {principal: 10.2f}')

print('Total paid', round(total_paid,2))
print('Number of months taken', month)